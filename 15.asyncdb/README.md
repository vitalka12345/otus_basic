Чтобы поднять БД используй команду

> docker run -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=my_db -p 5432:5432 postgres

В домашнем задании создаются таблицы posts, comments, todos с колонками, с открытого апи
https://jsonplaceholder.typicode.com/ выкачиваются данные пользователей и сохраняются в БД.
