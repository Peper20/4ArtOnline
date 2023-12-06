# 4ArtOnline

## Backend

### Запуск, установка, тестирование

Чтобы запустить бекэнд необходимо установить:
- Python 3.11+
- PostgreSQL
- requirements

Чтобы установить зависимости перейдите в исходники бекэнда (`src/backend`) и выполните:
```
python -m pip install -r requirements.txt
```

Далее нужно выполнить миграции, для этого перейдите в (`src/backend/drivens/database`) и выполните:
```
alembic upgrade head
```

Для запуска из корневой папки бекэнда (`src/backend`) и выполните с указанием драйвера:
```
python __main__.py --driver {driver}
```

Например:
```
python __main__.py --driver api
```
