# Task Manager

Веб-приложение для управления задачами на Django.
Команда СКБ231:
Мазитова Е.А., Раков Б.С., Стародубцев В.Ю.

## Установка и запуск

1. Клонируй репозиторий:
git clone <ссылка>
cd django_task_manager

2. Создай виртуальное окружение:
python3 -m venv venv
source venv/bin/activate # Ubuntu/macOS
или
venv\Scripts\activate # Windows

3. Установи зависимости:
pip install -r requirements.txt

4. Примени миграции:
python manage.py migrate

5. Запусти сервер:
python manage.py runserver
Открой в браузере: http://127.0.0.1:8000/

## Админка

Перейди на http://127.0.0.1:8000/admin/

Username: `pythononelove`
Password: `djangoforever`
