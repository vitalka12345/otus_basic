Чтобы поднять БД используй команду

> docker run -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=my_db -p 5432:5432 postgres

В домашнем задании создаётся таблица posts с колонками (id SERIAL PRIMARY KEY NOT NULL UNIQUE,
userId INTEGER NOT NULL, title VARCHAR DEFAULT '', body VARCHAR DEFAULT ''). С открытого апи
https://jsonplaceholder.typicode.com/posts выкачиваются посты пользователей и сохраняются в БД.
