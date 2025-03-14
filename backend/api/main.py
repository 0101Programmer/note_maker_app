from dotenv import load_dotenv
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from .api_constants import DATABASE_URL, FASTAPI_HOST, FASTAPI_PORT
from .routes.users import users_router

# Загружаем переменные из .env файла
load_dotenv()

app = FastAPI()

# Подключаем маршруты
app.include_router(users_router)

# Регистрация Tortoise ORM
register_tortoise(
    app,
    db_url=DATABASE_URL,
    modules={"models": ["backend.db_config.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)