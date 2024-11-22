# Restaurant Booking

Проект представляет собой веб-приложение для управления бронированием столиков в ресторане. Разработано на Django с использованием Bootstrap для интерфейса.

## Структура проекта

- **accounts/** — Приложение для управления пользователями (регистрация, авторизация, профили).
- **booking_app/** — Основное приложение для обработки бронирований.
- **config/** — Конфигурационные файлы проекта Django.
- **media/** — Каталог для пользовательских медиафайлов.
- **static/** — Каталог для статических файлов (CSS, JS, изображения).
- **manage.py** — Главный управляющий скрипт Django.
- **poetry.lock** и **pyproject.toml** — Файлы для управления зависимостями через Poetry.
- **Dockerfile** — Файл для сборки Docker-образа приложения.
- **docker-compose.yml** — Конфигурация для запуска контейнеров.

## Установка

1. Склонируйте репозиторий на локальную машину:
   ```bash
   git clone <URL репозитория>
   cd restaurant_booking

Установите зависимости с помощью Poetry:

poetry install

Скопируйте файл .env.sample в .env и настройте переменные окружения:

```bash
cp .env.sample .env
```

Выполните миграции базы данных:

python manage.py migrate

Создайте суперпользователя:

python manage.py createsuperuser



## Контейнеризация приложения с использованием Docker

### Установка и запуск

1. Убедитесь, что на вашем компьютере установлены **Docker** и **Docker Compose**.

2. Скопируйте файл `.env.sample` в `.env` и настройте переменные окружения для вашего проекта.

3. Соберите и запустите контейнеры:
   
   docker-compose up --build
   
4. Остановить контейнеры:

docker-compose down

5. Запуск миграций Django:
```
docker-compose run web python manage.py migrate

6. Создание суперпользователя Django:

docker-compose run web python manage.py createsuperuser

7. Запуск сервера Django:

docker-compose run web python manage.py runserver 0.0.0.0:8000