# Запуск

В папке /app создайте .env файл с параметрами подключения к БД, пример ниже

```
HOST = '192.168.0.1'

PORT = 5432

DB = 'postgre'

USER = 'postgre'

PASS = 'postgre'
```

Запустите сборку
```
docker compose up
```

Наслаждайтесь :)

Запросы для создания таблиц находятся в папке ___schema___
## Примечание
Относительно задания, не выполнен 4 пункт, а именно админка на Django.
