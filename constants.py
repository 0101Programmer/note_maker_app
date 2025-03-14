import os

from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

VUE_HOST='localhost'
VUE_PORT='5175'

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")