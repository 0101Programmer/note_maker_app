import redis

# Создаем подключение к Redis
redis_client = redis.StrictRedis(
    host='localhost',  # Адрес сервера Redis
    port=6379,         # Порт Redis (по умолчанию 6379)
    db=0,              # Номер базы данных (по умолчанию 0)
    decode_responses=True  # Автоматически декодировать ответы в строки
)

# Пример проверки подключения
if __name__ == "__main__":
    try:
        redis_client.ping()
        print("Подключение к Redis успешно!")
    except redis.exceptions.ConnectionError:
        print("Не удалось подключиться к Redis.")