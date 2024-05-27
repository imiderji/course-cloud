bot_name = "Surf's Up"
kew_file_name = "key.json"

commands = {
    "tutorial": "/tutorial"
}

buttons = {

}

messages = {
    "greeting": f"\
                Добро пожаловать в {bot_name} !\
                \n\nЯ помогу вам в работе с данными о речных маршрутах ⚓\
                \n\nВы можете всегда узнать о моём функционале, используя команду: \n{commands['tutorial']}\
                ",
    "tutorial": f"\
                Возможности бота⚓\
                \n\nФункционал разработан для обмена данными в формате Excel.\
                \n\nПользователь может выбрать таблицу и внести в неё данные, либо получить данные.\
                \n\nВажно, чтобы название Excel файла совпадало с названием таблицы, в также, чтобы совпадали столбцы файла и таблицы в базе данных\
                \n\nДоступные таблицы\
                \n\nBerths (Причалы)\
                \nberth_id: int\
                \nberth_number: int\
                \nberth_letter: str\
                \n\nDocks (Доки)\
                \ndock_id: int\
                \ndock_name: str\
                \nberth_count: int\
                \ndock_address: str\
                \ndock_type: str\
                \nexploitation: str\
                \ndepartment: str\
                \nwork_start_time: datetime.time\
                \nwork_end_time: datetime.time\
                \ndock_description: str\
                \nlong: float\
                \nlat: float\
                \n\nRelation_dock_berth (Связь причалов с доками)\
                \nberth_id: int\
                \ndock_id: int\
                \n\nShips (Судна)\
                \nship_id: int\
                \nship_name: str\
                \nship_class: str\
                \nship_num: str\
                \nship_capacity: int\
                \nship_description: str\
                \nship_model: str\
                \nshipowner_id: int\
                \n\nShipowners (Владельцы суден)\
                \nshipowner_id: int\
                \nshipowner_name: str\
                \nshipowner_inn: str\
                \nshipowner_ogrn: str\
                \nshipowner_contacts: str\
                \nshipowner_url: str\
                \n\nRoutes (Маршруты)\
                \nroute_id: int\
                \nroute_name: str\
                \nroute_short_name: str\
                \nroute_active: bool\
                \nroute_type_id: int\
                \nroute_type_name: str\
                \nroute_travel_time: int\
                \nroute_color: str\
                \n\nLots (Лоты)\
                \nlot_id: int\
                \nroute_id: int\
                \nlot_name: str\
                \nlot_active: bool\
                \n\nTrips (Поездки)\
                \ntrip_id: int\
                \nlot_id: int\
                \nroute_id: int\
                \ntrip_name: str\
                \ntrip_active: bool\
                ",
    "db_work": f"\
                Выберите таблицу 📃\
                ",
    "menu": "Я помогу вам в работе с данными о речных маршрутах ⚓"
}