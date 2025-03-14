import os

from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

FASTAPI_HOST = os.getenv("FASTAPI_HOST")
FASTAPI_PORT = int(os.getenv("FASTAPI_PORT"))
VUE_BASE_URL = os.getenv("VUE_BASE_URL")
DATABASE_URL = os.getenv("DATABASE_URL")
