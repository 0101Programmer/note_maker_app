import os

from dotenv import load_dotenv
from tortoise.contrib.fastapi import register_tortoise

from .routes.sessions_maker import set_get_session_router
from .routes.users import users_router
from .routes.notes import notes_router


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Загружаем переменные из .env файла
load_dotenv()

app = FastAPI()

# Подключаем маршруты
app.include_router(users_router)
app.include_router(set_get_session_router)
app.include_router(notes_router)
# Настройка CORS
origins = [
    os.getenv("VUE_BASE_URL"),  # Разрешаем запросы с фронтенда
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Список разрешённых источников
    allow_credentials=True,  # Разрешаем отправку cookies и заголовков авторизации
    allow_methods=["*"],     # Разрешаем все HTTP-методы (GET, POST и т.д.)
    allow_headers=["*"],     # Разрешаем все заголовки
)

# Регистрация Tortoise ORM
register_tortoise(
    app,
    db_url=os.getenv("DATABASE_URL"),
    modules={"models": ["backend.db_config.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}