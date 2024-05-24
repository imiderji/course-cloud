from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import Router
from .messages import messages, buttons
from aiogram.fsm.context import FSMContext
from . import keyboards as kb


commands_router = Router()


@commands_router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(messages['greeting'], reply_markup=kb.main)


@commands_router.message(Command('tutorial'))
async def command_tutorial(message: Message):
    await message.answer(messages['tutorial'])