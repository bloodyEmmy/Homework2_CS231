# Task Manager

Веб-приложение для управления задачами на Django.

**Команда СКБ231:** Мазитова Е.А., Раков Б.С., Стародубцев В.Ю.

## Установка и запуск

1. Клонируй репозиторий:
```bash
git clone https://github.com/yourusername/Homework2_CS231.git
cd Homework2_CS231
```

2. Создай виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# или
venv\Scripts\activate  # Windows
```

3. Установи зависимости:
```bash
pip install -r requirements.txt
```

4. Примени миграции:
```bash
python manage.py migrate
```

5. Запусти сервер:
```bash
python manage.py runserver
```

Открой в браузере: http://127.0.0.1:8000/

## Админка

Перейди на http://127.0.0.1:8000/admin/

**Username:** `pythononelove`  
**Password:** `djangoforever`
