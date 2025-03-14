from fastapi import APIRouter

# Создаем маршрутизатор с префиксом "/users" и тегом "Users"
users_router = APIRouter(prefix="/users", tags=["Users"])

# Маршрут для получения списка пользователей
@users_router.get("/")
async def get_users():
    return {"message": "List of users"}

# Маршрут для создания нового пользователя
@users_router.post("/create_user")
async def create_user():
    return {"message": "User created"}