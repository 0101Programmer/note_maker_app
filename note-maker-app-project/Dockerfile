# Базовый образ с Node.js для сборки
FROM node:18-alpine AS builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем .env файл
COPY ./.env ./.env

# Копируем package.json и package-lock.json
COPY ./note-maker-app-project/package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем остальные файлы проекта
COPY ./note-maker-app-project .

# Собираем проект
RUN npm run build

# Используем Nginx для обслуживания статических файлов
FROM nginx:alpine

# Копируем собранные файлы в Nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# Копируем конфигурацию Nginx
COPY ./note-maker-app-project/nginx.conf /etc/nginx/conf.d/default.conf

# Экспонируем порт 80
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]