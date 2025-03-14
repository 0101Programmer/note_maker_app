import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command

from .bot_constants import TELEGRAM_BOT_TOKEN

# Настройка логирования
logging.basicConfig(
    level=logging.INFO
)

# Инициализация бота и диспетчера
bot = Bot(
    token=TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # Устанавливаем parse_mode
)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот для заметок.")

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