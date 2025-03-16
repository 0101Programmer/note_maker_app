# 💻 Fullstack-приложение для создания и управления заметками через Telegram

# Стек технологий:
+ ### Backend: Python 3.13, Tortoise ORM, FastAPI, Aiogram, PostgreSQL, Docker, Redis
+ ### Frontend: Vue 3, Vite, Pinia, TypeScript, TailwindCSS

# Функционал:

## 1. Интеракция с ботом:
Пользователь пишет боту в Telegram, и бот отвечает сообщением с кнопкой, ведущей на страницу приложения.

## 2. Главная страница:
Здесь предоставляется возможность выбрать между созданием новой заметки и просмотром всех заметок

## 3. Страница создания заметки:
Для того, чтобы создать заметку указывается заголовок и описание, для сохранения заметки нужно нажать "сохранить"

## 4. Страница просмотра всех заметок:
На этой странице отображаются все заметки из базы данных для конкретного пользователя. Тут же есть возможность отредактировать заметку или удалить её

# Инструкция по развертыванию проекта:

## #1 Создание файла .env в корне проекта
(на уровне файла "start_app_script.py")

Со следующими переменными (и необходимыми значениями, исходя из своей конфигурации):
- Значения для базы данных
- DATABASE_URL
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- 
- Токен телеграм-бота
- TELEGRAM_BOT_TOKEN
- 
- Конфигурация FastAPI
- FASTAPI_HOST
- FASTAPI_PORT
- FASTAPI_BASE_URL
- 
- Конфигурация Vue
- VUE_HOST
- VUE_PORT
- VUE_BASE_URL
- 
- Конфигурация Redis
- REDIS_HOST
- REDIS_PORT
- REDIS_DB
- REDIS_DECODE_RESPONSES
- 
- Конфигурация Vite
- VITE_FASTAPI_HOST
- VITE_FASTAPI_PORT
- VITE_FASTAPI_BASE_URL

## #2 Создание виртуального окружения и активация (если оно не создано и не активировано)
> python -m venv .venv

> .venv\Scripts\activate


## #3 Установка зависимостей

> pip install -r requirements.txt

## #4 Запуск проекта через терминал (из корневой директории)

> python start_app_script.py


# Демонстрация функционала

## После запуска приложения напишем сообщение боту в телеграме
![Снимок экрана 2025-03-16 203023](https://github.com/user-attachments/assets/a24afcc6-cfb1-40bb-a457-4bb97289dcf2)

## Однако просто сообщение не подойдёт. Используем предложенную командку

![Снимок экрана 2025-03-16 203035](https://github.com/user-attachments/assets/4246669d-0ce5-4a7f-a533-6c9adc28131c)

## Нажимаем на кнопку и попадаем в веб-приложение
![Снимок экрана 2025-03-16 203050](https://github.com/user-attachments/assets/3cf55336-e8c5-4890-8455-c91d2f773101)

## Кстати, стартовая сессия с веб-интерфейсом длится 30 секунд, поэтому лучше сразу продлить её
![Снимок экрана 2025-03-16 203056](https://github.com/user-attachments/assets/5fdadcc0-6c93-4158-aaae-81b1fb5802d7)


![Снимок экрана 2025-03-16 203105](https://github.com/user-attachments/assets/64bb950b-5c52-484b-bc98-19df77377dc6)


![Снимок экрана 2025-03-16 203114](https://github.com/user-attachments/assets/c82bfa53-70a8-4a9e-a3c1-0abfb15682ee)

## Посмотрим все заметки
![Снимок экрана 2025-03-16 203142](https://github.com/user-attachments/assets/21585533-9741-4d88-8b1f-c5ce029f0cc9)


## Пока что тут пусто
![Снимок экрана 2025-03-16 203148](https://github.com/user-attachments/assets/93948a16-7951-46b9-93e9-f08c1acaaefd)

## Вернёмся назад, а потом сразу к созданию заметок
![Снимок экрана 2025-03-16 203156](https://github.com/user-attachments/assets/6c000d27-4b33-4b23-a744-6fc49374c4c4)

## Можно указать заголовок и описание
![Снимок экрана 2025-03-16 203202](https://github.com/user-attachments/assets/6c529a74-d45f-410e-ba62-31cfab467977)

## Потому что иначе ничего не выйдет
![Снимок экрана 2025-03-16 203224](https://github.com/user-attachments/assets/a08748a8-d5aa-4951-9038-98dd5b783306)


![Снимок экрана 2025-03-16 203237](https://github.com/user-attachments/assets/7c3cca41-9e86-4de5-9518-e20464e4c0ca)

## А вот теперь можно нажать на соответствующую кнопку
![Снимок экрана 2025-03-16 203252](https://github.com/user-attachments/assets/5ead969f-f7b4-40d3-8461-159ce9566dd5)

## Успешно. Для демонстрации создадим ещё несколько заметок
![Снимок экрана 2025-03-16 203258](https://github.com/user-attachments/assets/19cea835-86f3-435f-85a9-23cdf2e1b9c6)

## И вернёмся в главное меню
![Снимок экрана 2025-03-16 203400](https://github.com/user-attachments/assets/c312233e-2c41-4de2-b33d-9fdd84a7f1ea)

## Отсюда переходим на страницу всех заметок
![Снимок экрана 2025-03-16 203412](https://github.com/user-attachments/assets/348466e3-6da8-4aac-a2bc-007b95d6d4a5)

## Теперь здесь уже не так пусто
![Снимок экрана 2025-03-16 203420](https://github.com/user-attachments/assets/87d66736-68c5-48b3-a896-9382e64c3d29)

## Попробуем изменить заметку, удалим описание. Однако сохранить не получится

![Снимок экрана 2025-03-16 203507](https://github.com/user-attachments/assets/fa2de17a-b3c2-4348-8f38-d660c339ecaf)

## Тогда удалим заголовок. Тоже не выйдет
![Снимок экрана 2025-03-16 203540](https://github.com/user-attachments/assets/91255109-a8a8-4ad0-9a14-bf68c2f54ab0)

## Если соблюсти условия непустого заголовка и описания, то можно будет нажать на кнопку сохранения
![Снимок экрана 2025-03-16 203551](https://github.com/user-attachments/assets/0734e1b9-0791-4184-aeed-99f301efb304)


## Нажмём и увидим, что содержимое заметки поменялось, как и время обновления 
![Снимок экрана 2025-03-16 203604](https://github.com/user-attachments/assets/2755603c-1735-4287-ab07-97ec31c1107f)


## Заметки также можно удалять
![Снимок экрана 2025-03-16 203617](https://github.com/user-attachments/assets/d9c9790b-6f82-43d1-8413-545712a468e1)


![Снимок экрана 2025-03-16 203623](https://github.com/user-attachments/assets/e12cce34-7cea-42c4-95c0-6b7bf9543b99)


![Снимок экрана 2025-03-16 203632](https://github.com/user-attachments/assets/f43251c5-4d25-42bf-8397-0214b8a09196)

## В базу данных все изменения, само собой, тоже подгружаются
![Снимок экрана 2025-03-16 203655](https://github.com/user-attachments/assets/6c246327-d115-4ea6-bd00-fdd42dd4a3e1)

## Момент с временем сессии, если оно закончится — придётся получать у бота новую ссылку для авторизации
![Снимок экрана 2025-03-16 203746](https://github.com/user-attachments/assets/8420a37c-a15f-4b76-80c5-251056c0ac88)


![Снимок экрана 2025-03-16 203804](https://github.com/user-attachments/assets/3be7f61b-2dca-4c53-955d-5cfffd4b505d)



































