import subprocess

fastapi_main = 'python -m backend.api.main'
bot = 'python -m backend.bot.bot'
docker = 'docker-compose -f docker/docker-compose.yml up --build'

# Запуск команд параллельно
try:
    print("Запуск FastAPI...")
    fastapi_process = subprocess.Popen(fastapi_main, shell=True)

    print("Запуск бота...")
    bot_process = subprocess.Popen(bot, shell=True)

    print('Запуск докера...')
    docker_process = subprocess.Popen(docker, shell=True)

    # Ожидание завершения процессов
    fastapi_process.wait()
    bot_process.wait()
except Exception as e:
    print(f"Ошибка при выполнении команды: {e}")