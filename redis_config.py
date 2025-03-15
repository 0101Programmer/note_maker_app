import redis

# Создаем подключение к Redis
redis_client = redis.StrictRedis(
    host='redis',  # Адрес сервера Redis
    port=6379,         # Порт Redis (по умолчанию 6379)
    db=0,              # Номер базы данных (по умолчанию 0)
    decode_responses=True  # Автоматически декодировать ответы в строки
)

# Аршинное подключение к Redis для FastAPI
docker_off_redis_client = redis.StrictRedis(
    host='localhost',  # Адрес сервера Redis
    port=6379,         # Порт Redis (по умолчанию 6379)
    db=0,              # Номер базы данных (по умолчанию 0)
    decode_responses=True  # Автоматически декодировать ответы в строки
)