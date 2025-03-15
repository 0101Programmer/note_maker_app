import asyncio
import logging
import os
import uuid
from datetime import timedelta

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

from redis_config import redis_client

# Настройка логирования
logging.basicConfig(
    level=logging.INFO
)

# Инициализация бота и диспетчера
bot = Bot(
    token=os.getenv("TELEGRAM_BOT_TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # Устанавливаем parse_mode
)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: types.Message):

    # Получение tg_username из сообщения
    tg_username = message.from_user.username
    if not tg_username:
        await message.answer("У вас нет username в Telegram. Пожалуйста, установите его в настройках.")
        return


    # Базовый URL эндпоинта API /set_get_session/
    base_set_get_session_url = f"http://{os.getenv('FASTAPI_HOST')}:{os.getenv('FASTAPI_PORT')}/set_get_session/"
    session_maker_id = str(uuid.uuid4())
    # Сохраняем пару К/З в Redis
    redis_client.setex(
        session_maker_id,  # Ключ
        timedelta(seconds=10),  # Время жизни ключа
        1  # Значение
    )
    # Формируем полную ссылку
    full_auth_url = f"{base_set_get_session_url}{session_maker_id}/{tg_username}"

    # Создаем кнопку со ссылкой
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="Войти в приложение", url=full_auth_url)]
        ]
    )

    # Отправляем сообщение с кнопкой
    await message.answer("Привет! Нажмите на кнопку ниже для входа в приложение:", reply_markup=keyboard)

# Обработчик команды /help
@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer("Этот бот помогает управлять заметками.")

# Обработчик всех сообщений
@dp.message()
async def all_messages(message: types.Message):
    await message.answer("Для начала работы введите команду /start")

# Запуск бота
async def main():
    await dp.start_polling(bot, skip_updates=True)  # Пропуск накопленных апдейтов

if __name__ == '__main__':
    asyncio.run(main())