from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Работа с БД 📁")],
    [KeyboardButton(text="Туториал 💡")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню"
)

in_tables_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Назад в меню ↩️")],
    [KeyboardButton(text="Туториал 💡")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню"
)

in_tutorial = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Назад в меню ↩️")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню"
)

tables = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="berths (Причалы)", callback_data='berths')],
    [InlineKeyboardButton(text="docks (Доки)", callback_data='docks')],
    [InlineKeyboardButton(text="relations_dock_berth (Привязка причалов к докам)", callback_data='relations_dock_berth')],
    [InlineKeyboardButton(text="ships (Судна)", callback_data='ships')],
    [InlineKeyboardButton(text="shipowners (Владельцы суден)", callback_data='shipowners')],
])

berths_actions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить данные", callback_data='add_berths')],
    [InlineKeyboardButton(text="Получить таблицу", callback_data='get_berths')],
])

docks_actions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить данные", callback_data='add_docks')],
    [InlineKeyboardButton(text="Получить таблицу", callback_data='get_docks')],
])

relations_dock_berth_actions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить данные", callback_data='add_relations_dock_berth')],
    [InlineKeyboardButton(text="Получить таблицу", callback_data='get_relations_dock_berth')],
])

ships_actions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить данные", callback_data='add_ships')],
    [InlineKeyboardButton(text="Получить таблицу", callback_data='get_ships')],
])

shipowners_actions = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Добавить данные", callback_data='add_shipowners')],
    [InlineKeyboardButton(text="Получить таблицу", callback_data='get_shipowners')],
])


in_table_actions = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="К таблицам 📋")],
    [KeyboardButton(text="Туториал 💡")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню"
)