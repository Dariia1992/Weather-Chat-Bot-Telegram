import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN_TG
from handlers import commands, echo, city, weather


bot = Bot(token=TOKEN_TG)
dp = Dispatcher()


async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_router(commands.router)
    dp.include_router(city.router)
    dp.include_router(weather.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())