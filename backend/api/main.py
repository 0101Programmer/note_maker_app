import os
from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from dotenv import load_dotenv

from constants import FASTAPI_HOST, FASTAPI_PORT, DATABASE_URL

# Загружаем переменные из .env файла
load_dotenv()

app = FastAPI()

# Регистрация Tortoise ORM
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["backend.db_config.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# запуск FastAPI, Vue и телеграм бота
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)