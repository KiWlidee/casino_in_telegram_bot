from aiogram import Bot, Dispatcher

from asyncio import run as arun

from handlers import router
from handler.crash import crash_router
from handler.get_makasini import makasini_router
from data import TOKEN

async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(crash_router)
    dp.include_router(makasini_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        arun(main())
    except KeyboardInterrupt:
        print("Бот остановлен")