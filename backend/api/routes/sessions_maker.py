import uuid
from datetime import timedelta
from fastapi.responses import RedirectResponse
from fastapi import APIRouter, HTTPException

from redis_config import docker_off_redis_client

from ..api_constants import VUE_BASE_URL
from ...db_config.models import User

set_get_session_router = APIRouter(prefix="/set_get_session", tags=["Session settings"])

# Маршрут для перенаправления пользователя в веб-приложение
@set_get_session_router.get("/{session_maker_id}/{tg_username}")
async def set_get_session(session_maker_id: str, tg_username: str):
    # Проверяем, существует ли session_maker_id в Redis
    if not docker_off_redis_client.get(session_maker_id):
        raise HTTPException(status_code=401, detail="Недействительный ключ, попробуйте запросить ссылку у бота ещё раз")

    # Проверяем, есть ли уже сессия для данного tg_username
    session_id = docker_off_redis_client.get(tg_username)
    if not session_id:
        session_id = str(uuid.uuid4())
        # Сохраняем session_id в Redis
        docker_off_redis_client.setex(
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
    redirect_url = f"{VUE_BASE_URL}/{session_id}/{tg_username}"

    # Выполняем редирект
    return RedirectResponse(url=redirect_url)

@set_get_session_router.get("/check_session/{session_id}/{tg_username}")
async def check_session(session_id: str, tg_username: str):
    # Проверяем, существует ли tg_username в Redis
    if not docker_off_redis_client.exists(tg_username):
        return {"valid": False, "message": "User session not found"}

    # Получаем session_id из Redis
    existed_session_id = docker_off_redis_client.get(tg_username)

    # Сравниваем session_id из URL с session_id из Redis
    if session_id != existed_session_id:
        return {"valid": False, "message": "Invalid session ID"}

    # Если всё в порядке, возвращаем успешный ответ
    return {"valid": True, "message": "Session is valid"}