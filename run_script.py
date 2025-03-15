import subprocess

fastapi_main = 'python -m backend.api.main'
bot = 'python -m backend.bot.bot'
docker = 'docker-compose -f docker/docker-compose.yml --env-file .env up --build'

# Запуск команд параллельно
try:
    print("Запуск FastAPI...")
    fastapi_process = subprocess.Popen(fastapi_main, shell=True)

    # print("Запуск Telegram Bot...")
    # bot_process = subprocess.Popen(bot, shell=True)

    print('Запуск Docker-compose...')
    docker_process = subprocess.Popen(docker, shell=True)

    # Ожидание завершения процессов
    fastapi_process.wait()
    # bot_process.wait()
    docker_process.wait()
except Exception as e:
    print(f"Ошибка при выполнении команды: {e}")