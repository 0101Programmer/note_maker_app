import os

from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

FASTAPI_HOST="127.0.0.1"
FASTAPI_PORT=8000

VUE_HOST='localhost'
VUE_PORT='5175'

DATABASE_URL = os.getenv("DATABASE_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")