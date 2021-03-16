Чтобы поднять БД используй команду

> docker run -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=my_db -p 5432:5432 postgres

Для успешного записи в БД длинных строк нужно использовать тип varchar.
