from .commands import commands_router
from .handlers import handlers_router
from .bot_init import bot, dp


async def bot_poller():
    dp.include_router(commands_router)
    dp.include_router(handlers_router)
    await dp.start_polling(bot)