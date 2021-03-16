import asyncio
import asyncpg
import aiohttp


async def get_posts():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://jsonplaceholder.typicode.com/posts') as response:
            return await response.json()


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
    await conn.close()


if __name__ == '__main__':
    asyncio.run(run())
    loop = asyncio.get_event_loop()
    loop.close()
