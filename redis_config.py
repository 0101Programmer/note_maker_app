import redis
import os

from dotenv import load_dotenv

# Создаем подключение к Redis
redis_client = redis.StrictRedis(
    host=os.getenv("REDIS_HOST"),  # Адрес сервера Redis
    port=os.getenv("REDIS_PORT"),         # Порт Redis (по умолчанию 6379)
    db=os.getenv("REDIS_DB"),              # Номер базы данных (по умолчанию 0)
    decode_responses=os.getenv("REDIS_DECODE_RESPONSES")  # Автоматически декодировать ответы в строки
)

# Временное подключение к Redis для FastAPI
docker_off_redis_client = redis.StrictRedis(
    host='localhost',  # Адрес сервера Redis
    port=6379,         # Порт Redis (по умолчанию 6379)
    db=0,              # Номер базы данных (по умолчанию 0)
    decode_responses=True  # Автоматически декодировать ответы в строки
)