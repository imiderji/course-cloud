from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from .messages import messages, buttons

commands_router = Router()


@commands_router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(messages['greeting'])


@commands_router.message(Command('tutorial'))
async def command_tutorial(message: Message):
    await message.answer(messages['tutorial'])