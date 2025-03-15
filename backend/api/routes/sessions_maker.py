import os
import uuid
from datetime import timedelta
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from redis_config import redis_client
from ...db_config.models import User

set_get_session_router = APIRouter(prefix="/set_get_session", tags=["Session settings"])

# Маршрут для перенаправления пользователя в веб-приложение
@set_get_session_router.get("/{session_maker_id}/{tg_username}")
async def set_get_session(session_maker_id: str, tg_username: str):
    # Проверяем, существует ли session_maker_id в Redis
    if not redis_client.get(session_maker_id):
        raise HTTPException(status_code=401, detail="Недействительный ключ, попробуйте запросить ссылку у бота ещё раз")

    # Проверяем, есть ли уже сессия для данного tg_username
    session_id = redis_client.get(tg_username)
    if not session_id:
        session_id = str(uuid.uuid4())
        # Сохраняем session_id в Redis
        redis_client.setex(
            tg_username,  # Ключ
            timedelta(seconds=30),  # Время жизни ключа
            session_id  # Значение
        )
    else:
        session_id = session_id

    # Проверяем, существует ли пользователь в базе данных
    user_exists = await User.filter(username=tg_username).exists()
    if not user_exists:
        # Если пользователя нет, создаём нового
        await User.create(username=tg_username)

    # Формируем URL для редиректа
    redirect_url = f"{os.getenv('VUE_BASE_URL')}/{session_id}/{tg_username}"

    # Выполняем редирект
    return RedirectResponse(url=redirect_url)


@set_get_session_router.post("/check_session")
async def check_session(request: Request):
    try:
        # Получаем JSON-данные из тела запроса
        data = await request.json()
        session_id = data.get("session_id")
        tg_username = data.get("tg_username")

        # Проверяем наличие обязательных полей
        if not session_id or not tg_username:
            return JSONResponse(status_code=400, content={"valid": False, "message": "Missing required fields"})

        # Проверяем, существует ли tg_username в Redis
        if not redis_client.exists(tg_username):
            return {"valid": False, "message": "User session not found"}

        # Получаем session_id из Redis
        existed_session_id = redis_client.get(tg_username)

        # Преобразуем байтовую строку в обычную строку
        if isinstance(existed_session_id, bytes):
            existed_session_id = existed_session_id.decode("utf-8")

        # Сравниваем session_id из тела запроса с session_id из Redis
        if session_id != existed_session_id:
            return {"valid": False, "message": "Invalid session ID"}

        # Если всё в порядке, возвращаем успешный ответ
        return {"valid": True, "message": "Session is valid"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"valid": False, "message": f"Internal server error: {str(e)}"})