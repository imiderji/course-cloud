from aiogram import Bot, Dispatcher
from core.config import settings

bot = Bot(settings.tg_token)
dp = Dispatcher()

__all__ = ['bot', 'dp']