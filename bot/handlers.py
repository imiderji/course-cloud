from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram import Router

from api.berths.crud import get_berths, get_berth_columns
from api.docks.crud import get_docks, get_dock_columns
from api.relations_dock_berth.crud import get_relations_dock_berth, get_relations_dock_berth_columns
from api.ships.crud import get_ships, get_ships_columns
from api.shipowners.crud import get_shipowners, get_shipowners_columns

from core.models.db_work import db_work
from aiogram.types import FSInputFile
from openpyxl import Workbook
from .messages import messages
from . import keyboards as kb
import os


handlers_router = Router()


@handlers_router.message(F.text == 'Туториал 💡')
async def tutorial(message: Message):
    await message.answer(messages['tutorial'], reply_markup=kb.in_tutorial)


@handlers_router.message(F.text == 'Работа с БД 📁')
async def work_with_db(message: Message):
    await message.answer(messages["db_work"], reply_markup=kb.tables)
    await message.answer("🌊", reply_markup=kb.in_tables_menu)


@handlers_router.message(F.text == 'Назад в меню ↩️')
async def tutorial(message: Message):
    await message.answer(messages['menu'], reply_markup=kb.main)


@handlers_router.message(F.text == 'К таблицам 📋')
async def tutorial(message: Message):
    await message.answer(messages["db_work"], reply_markup=kb.tables)
    await message.answer("🌊", reply_markup=kb.in_tables_menu)


# BERTHS ПРИЧАЛЫ


@handlers_router.callback_query(F.data == 'berths')
async def berths(callback: Message):
    await callback.message.delete()
    await callback.message.answer(f"Таблица berths (Причалы)\n\nВыберите действие 👇🏻", reply_markup=kb.berths_actions)
    await callback.message.answer(f"⚓", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'add_berths')
async def add_berths_handler(callback: Message):
    await callback.message.answer(f"Внесите файл с данными в формате json 👇🏻", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'get_berths')
async def get_berths_handler(callback: Message):

    berths_list = get_berths(db_work.get_session())
    wb = Workbook()
    ws = wb.active

    colums = get_berth_columns()[:len(get_berth_columns()) - 1]
    ws.append(colums)

    for berth in berths_list:
        ws.append([berth.berth_id, berth.berth_name, berth.berth_letter])

    file_path = "berths.xlsx"
    wb.save(file_path)

    await callback.message.answer_document(FSInputFile(file_path), caption="Файл с данными о причалах", reply_markup=kb.in_table_actions)

    os.remove(file_path)



# DOCKS ДОКИ


@handlers_router.callback_query(F.data == 'docks')
async def docks(callback: Message):
    await callback.message.delete()
    await callback.message.answer(f"Таблица docks (Доки)\n\nВыберите действие 👇🏻", reply_markup=kb.docks_actions)
    await callback.message.answer(f"⚓", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'add_docks')
async def add_docks_handler(callback: Message):
    await callback.message.answer(f"Внесите файл с данными в формате json 👇🏻", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'get_docks')
async def get_docks_handler(callback: Message):

    docks_list = get_docks(db_work.get_session())
    wb = Workbook()
    ws = wb.active

    colums = get_dock_columns()[:len(get_dock_columns()) - 1]
    ws.append(colums)

    for dock in docks_list:
        ws.append([dock.dock_id, dock.dock_name, dock.dock_count, 
                   dock.dock_address, dock.dock_type, dock.exploitation, 
                   dock.department, dock.work_start_time, dock.work_end_time, 
                   dock.dock_description, dock.long, dock.lat])

    file_path = "docks.xlsx"
    wb.save(file_path)

    await callback.message.answer_document(FSInputFile(file_path), caption="Файл с данными о доках", reply_markup=kb.in_table_actions)

    os.remove(file_path)



# relations_dock_berth


@handlers_router.callback_query(F.data == 'relations_dock_berth')
async def relations_dock_berth(callback: Message):
    await callback.message.delete()
    await callback.message.answer(f"Таблица relations_dock_berth (Привязка причалов к докам)\n\nВыберите действие 👇🏻", reply_markup=kb.relations_dock_berth_actions)
    await callback.message.answer(f"⚓", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'add_relations_dock_berth')
async def add_relations_dock_berth_handler(callback: Message):
    await callback.message.answer(f"Внесите файл с данными в формате json 👇🏻", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'get_relations_dock_berth')
async def get_relations_dock_berth_handler(callback: Message):

    relations_dock_berth_list = get_relations_dock_berth(db_work.get_session())
    wb = Workbook()
    ws = wb.active

    colums = get_relations_dock_berth_columns()[:len(get_relations_dock_berth_columns()) - 1]
    ws.append(colums)

    for relation_dock_berth in relations_dock_berth_list:
        ws.append([relation_dock_berth.dock_id, relation_dock_berth.berth_id])

    file_path = "relations_dock_berth.xlsx"
    wb.save(file_path)

    await callback.message.answer_document(FSInputFile(file_path), caption="Файл с данными о связях причалов с доками", reply_markup=kb.in_table_actions)

    os.remove(file_path)



# SHIPS Судна


@handlers_router.callback_query(F.data == 'ships')
async def ships(callback: Message):
    await callback.message.delete()
    await callback.message.answer(f"Таблица ships (Судна)\n\nВыберите действие 👇🏻", reply_markup=kb.ships_actions)
    await callback.message.answer(f"⚓", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'add_ships')
async def add_ships_handler(callback: Message):
    await callback.message.answer(f"Внесите файл с данными в формате json 👇🏻", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'get_ships')
async def get_ships_handler(callback: Message):

    ships_list = get_ships(db_work.get_session())
    wb = Workbook()
    ws = wb.active

    colums = get_ships_columns()[:len(get_ships_columns()) - 1]
    ws.append(colums)

    for ship in ships_list:
        ws.append([ship.ship_id, ship.ship_name, ship.ship_class, 
                   ship.ship_num, ship.ship_capacity, ship.ship_description, 
                   ship.ship_model, ship.shipowner_id])

    file_path = "ships.xlsx"
    wb.save(file_path)

    await callback.message.answer_document(FSInputFile(file_path), caption="Файл с данными о суднах", reply_markup=kb.in_table_actions)

    os.remove(file_path)



# SHIPOWNERS Владельцы суден


@handlers_router.callback_query(F.data == 'shipowners')
async def shipowners(callback: Message):
    await callback.message.delete()
    await callback.message.answer(f"Таблица shipowners (Владельцы суден)\n\nВыберите действие 👇🏻", reply_markup=kb.shipowners_actions)
    await callback.message.answer(f"⚓", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'add_shipowners')
async def add_shipowners_handler(callback: Message):
    await callback.message.answer(f"Внесите файл с данными в формате json 👇🏻", reply_markup=kb.in_table_actions)


@handlers_router.callback_query(F.data == 'get_shipowners')
async def get_shipowners_handler(callback: Message):

    shipowners_list = get_shipowners(db_work.get_session())
    wb = Workbook()
    ws = wb.active

    colums = get_shipowners_columns()[:len(get_shipowners_columns()) - 1]
    ws.append(colums)

    for shipowner in shipowners_list:
        ws.append([shipowner.shipowner_id, shipowner.shipowner_name, 
                   shipowner.shipowner_inn, shipowner.shipowner_ogrn, 
                   shipowner.shipowner_contacts, shipowner.shipowner_url])

    file_path = "shipowners.xlsx"
    wb.save(file_path)

    await callback.message.answer_document(FSInputFile(file_path), caption="Файл с данными о владельцах суден", reply_markup=kb.in_table_actions)

    os.remove(file_path)