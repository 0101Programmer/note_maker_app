import redis
import os

# Создаем подключение к Redis
redis_client = redis.StrictRedis(
    host=os.getenv("REDIS_HOST"),  # Адрес сервера Redis
    port=os.getenv("REDIS_PORT"),         # Порт Redis (по умолчанию 6379)
    db=os.getenv("REDIS_DB"),              # Номер базы данных (по умолчанию 0)
    decode_responses=os.getenv("REDIS_DECODE_RESPONSES")  # Автоматически декодировать ответы в строки
)