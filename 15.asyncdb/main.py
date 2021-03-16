# Асинхронная работа с сетью
# Цель: В этом ДЗ вы напишите скрипт.
# написать скрипт, который при помощи асинхронного клиента обращается к открытому апи
# (например, jsonplaceholder) и выводит оттуда информацию
# создать модели для объектов, которые тянутся с открытого апи
# записать вытянутые модели в БД
# скрипт для стягивания данных и записи в БД реализован в асинхронном виде
# Критерии оценки: у моделей есть primary_key - 1 балл
# runны все миграции - 1 балл
# скрипт стягивает данные с API и складывает в БД - 1 балл
# обращение к API выполняется в асинхронном виде - 1 балл
# на асинхронный клиент применяется close при завершении работы - 1 балл
# запись в базу данных выполняется в асинхронном виде - 1 балл
# соединение с базой данных закрывается при завершении работы - 1 балл
# Рекомендуем сдать до: 26.02.2021
# docker run -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -e POSTGRES_DB=my_db -p 5432:5432 postgres
import asyncio
import asyncpg
import aiohttp


async def get_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts') as response:
            # print(await response.json())
            return await response.json()


async def fetch_elem():
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='my_db',
        host='127.0.0.1',
    )
    print(conn)
    post = await conn.fetchrow(
        """
        SELECT * FROM public.posts
        WHERE "userId" = $1;
        """,
        15,
    )
    print("post:", post)
    await conn.close()


async def insert_elem():
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='my_db',
        host='127.0.0.1',
    )
    print(conn)
    await conn.execute(
        """
        INSERT INTO public.posts("userId", title, body)
        VALUES ($1, $2, $3);
        """,
        15,
        'example title2',
        'example body2',
    )
    await conn.close()


async def run():
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='my_db',
        host='127.0.0.1',
    )

    for i in await get_posts():
        print("id: ", i["id"], "userId: ", i["userId"], "title: ", str(i["title"]),
              "body: ", str(i["body"]))
        await conn.execute(
            """
            INSERT INTO public.posts("userId", title, body)
            VALUES ($1, $2, $3);
            """,
            i["userId"],
            i["title"],
            i["body"],
        )
    await conn.close()


if __name__ == '__main__':
    # asyncio.run(insert_elem())
    # asyncio.run(fetch_elem())
    asyncio.run(run())
    # loop = asyncio.get_event_loop()
    # print(loop)
    # loop.run_until_complete(run())
