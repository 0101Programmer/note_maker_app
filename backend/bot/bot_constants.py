import os

from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")