import uuid
from datetime import timedelta

from fastapi import APIRouter, HTTPException

from redis_config import redis_client

set_get_session_router = APIRouter(prefix="/set_get_session", tags=["Session settings"])

# Маршрут для перенаправления пользователя в веб-приложение
@set_get_session_router.get("/{session_maker_id}/{tg_username}")
def set_get_session(session_maker_id: str, tg_username: str):
    if not redis_client.get(session_maker_id):
        raise HTTPException(status_code=401, detail="Недействительный ключ, попробуйте запросить ссылку у бота ещё раз")
    if not redis_client.get(tg_username):
        session_id = str(uuid.uuid4())
        # Сохраняем session_id в Redis
        redis_client.setex(
            tg_username,  # Ключ
            timedelta(seconds=30),  # Время жизни ключа
            session_id  # Значение
        )
        return {"new_session_id": redis_client.get(tg_username)}
    else:
        return {"old_session_id": redis_client.get(tg_username)}
