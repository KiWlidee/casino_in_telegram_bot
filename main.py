from aiogram import Bot, Dispatcher

from asyncio import run as arun

from handlers import router
from data import TOKEN

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        arun(main())
    except KeyboardInterrupt:
        print("Бот остановлен")