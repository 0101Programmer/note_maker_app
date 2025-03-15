import subprocess

# Команда для запуска Docker Compose
docker = 'docker-compose -f docker/docker-compose.yml up --build'

# Запуск приложения
try:
    print('Запуск Docker-compose...')
    docker_process = subprocess.Popen(docker, shell=True)

    docker_process.wait()
except Exception as e:
    print(f"Ошибка при выполнении команды: {e}")