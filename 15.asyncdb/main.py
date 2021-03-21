import asyncio
import asyncpg
import aiohttp


async def get_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts') as response_posts:
            return await response_posts.json()


async def get_comments():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/comments') as response_comments:
            return await response_comments.json()


async def get_todos():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/todos') as response_todos:
            return await response_todos.json()


async def run():
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='my_db',
        host='127.0.0.1',
    )

    await conn.execute('''
        CREATE TABLE public.posts (id SERIAL PRIMARY KEY NOT NULL UNIQUE,
        userId INTEGER NOT NULL, title VARCHAR DEFAULT '', body VARCHAR DEFAULT '');
        ''')

    await conn.execute('''
        CREATE TABLE public.comments (id SERIAL PRIMARY KEY NOT NULL UNIQUE,
        postId INTEGER NOT NULL, name VARCHAR DEFAULT '', email VARCHAR DEFAULT '',
        body VARCHAR DEFAULT '');
        ''')

    await conn.execute('''
        CREATE TABLE public.todos (id SERIAL PRIMARY KEY NOT NULL UNIQUE,
        userId INTEGER NOT NULL, title VARCHAR DEFAULT '', completed BOOLEAN DEFAULT FALSE);
        ''')

    for i in await get_posts():
        await conn.execute(
            """
            INSERT INTO public.posts(userId, title, body)
            VALUES ($1, $2, $3);
            """,
            i["userId"],
            i["title"],
            i["body"],
        )

    for i in await get_comments():
        await conn.execute(
            """
            INSERT INTO public.comments(postId, name, email, body)
            VALUES ($1, $2, $3, $4);
            """,
            i["postId"],
            i["name"],
            i["email"],
            i["body"],
        )

    for i in await get_todos():
        await conn.execute(
            """
            INSERT INTO public.todos(userId, title, completed)
            VALUES ($1, $2, $3);
            """,
            i["userId"],
            i["title"],
            i["completed"],
        )

    await conn.close()


if __name__ == '__main__':
    asyncio.run(run())
    loop = asyncio.get_event_loop()
    loop.close()
