import logging
import asyncio
from aiogram import Bot, Dispatcher
from handlers.basic_handlers import router

logging.basicConfig(level=logging.INFO)

bot = Bot(token="")
dp = Dispatcher()

async def main():
    
    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
