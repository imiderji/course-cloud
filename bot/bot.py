from core.config import settings
from aiogram import Bot, Dispatcher


bot = Bot(settings.tg_token)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)