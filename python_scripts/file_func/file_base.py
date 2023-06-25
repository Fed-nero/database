from typing import Union


def reg_path(element: dict) -> tuple[bool, str]:
    '''Registrade a path do the element file.'''
    from interaction_function.user import answer
    from os.path import exists, join
    from Baza_constanti import POSITIVE, NEGATIVE, DERFILE, CONST_FILE_NAME
    KEY_RESULT_REG: int = 0
    KEY_PATH: int = 1
    data: list = []
    result: list[bool, str] = [False, '']
    if not exists(element['path']):
        if answer(
            f"Do you want to create a {element['name']} file in the same plase with program?", 
            natification=f'If you say yes file will be loade in this directory:\n{DERFILE}'
            ):
            result[KEY_PATH] = join(DERFILE, element['global_name'])
        else:
            user_direcory: str = input("Enter derictory's full path")
            result[KEY_PATH] = join(user_direcory, element['global_name'])
            try:
                open(join(user_direcory, element['global_name']), 'wt', encoding='utf').close()
            except FileNotFoundError:
                print('Не удалось создать файл в нужной директории')
                result[KEY_RESULT_REG] = NEGATIVE
                return tuple(result)
        file_const_path: str = join(DERFILE, CONST_FILE_NAME)
        with open(file_const_path, 'rt', encoding='utf') as save_file:
            data = save_file.readlines()
        for index, row in enumerate(data):
            if f'{element["global_var_path"]}: str = r' in row:
                data[index] = f"{element['global_var_path']}: str = r'{result[KEY_PATH]}'\n"
                break
        with open(file_const_path, 'wt', encoding='utf') as save_file:
            print(*data, sep='', end='', file=save_file)
    result[KEY_RESULT_REG] = POSITIVE
    return tuple(result)


def feel(element: dict) -> Union[bool, int]: #Сделать возможным принудительную регистрацию пользователя
    '''Felling select element.'''
    from Baza_constanti import POSITIVE, CODE_CREATE_CREATOR
    from interaction_function.user import answer
    from interaction_function.base import (
        row_write,
        create_user,
        create_records
    )
    from Baza_constanti import (
        LOGS_FILE,
        DATA_BASE,
        FEILDS_LOGS,
        FEILDS_DESCRIPTION
    )
    data: list
    global creater_create
    if element == LOGS_FILE:
        creater_create = False
        data = [row_write(FEILDS_LOGS), ]
        if answer(
            'Логс файлы успешно созданы, желаете ли вы создать первого пользователя?'
        ):
            new_user: tuple = create_user(0, 'admin')
            creater_create = True
            data.append(row_write(new_user))
        with open(element['path'], 'wt', encoding='utf-8') as logs_file:
            print(*data, sep='\n', end='', file=logs_file)
        if creater_create:
            return CODE_CREATE_CREATOR
        return POSITIVE
    elif element == DATA_BASE:
        data = [row_write(tuple(FEILDS_DESCRIPTION.keys())), ]
        creater_create = False
        if creater_create and answer(
                'База данных успешно создана, хотите ли вы заполнить её записями?'
            ):
            records_amount: int = int(input('Введите колличество новых записей:'))#
            for i in range(records_amount):
                print(f'Создаём запись №{i + 1}:')
                data.append(create_records(i))
        with open(element['path'], 'wt', encoding='utf-8') as data_base_file:
            print(*data, sep='\n', end='', file=data_base_file)
    return POSITIVE


def create(element: dict) -> Union[bool, int]:
    '''Creates a data base if it is not found.'''
    from interaction_function.user import answer
    from Baza_constanti import NEGATIVE
    result_registration: tuple[bool, str]
    KEY_RESULT_REG: int = 0
    KEY_PATH: int = 1
    if answer(
        f'Do you wanna create {element["name"]}?',
        natification=f"App won't work with out {element['name']}"
    ) and (result_registration:= reg_path(element))[KEY_RESULT_REG]:
        element['path'] = result_registration[KEY_PATH]
        flag: Union[bool, int] = feel(element)
        print(f'{element["name"]} is created sucssesfuly')
        return flag
    return NEGATIVE


def check(element: dict) -> Union[bool, int]:
    '''Checks elements.'''
    from os.path import exists
    result_find =  exists(element['path'])
    print(f"{element['name']} is {('not ', '')[result_find]}found")
    if not result_find:
        result_create: Union[bool, int] = create(element)
        return result_create
    return result_find


def load_file(
        config_code: int,
        config_path: str
) -> Union[
    dict[
        int,
        dict[str, str]
    ],
    dict[
        int, dict[
            int, dict[
                str, Union[
                    str, 
                    int, 
                    __import__('datetime').datetime
                ]
            ]
        ]
    ]
]:
    '''This gets a code of config.'''
    from Baza_constanti import SEPARATION
    data: dict = {}
    ERROR: bool = False
    try:
        with open(config_path, 'rt', encoding='utf-8') as file_r:
            TITLE_ROW: int = 1
            data_file = map(lambda s: s.split(SEPARATION), file_r.readlines()[TITLE_ROW:])
    except:
        print(f'Error {config_path}')  
        ERROR = False 
    if not ERROR:
        match config_code:
            case 6:
                from Baza_constanti import FEILDS_RECORDS
                for (
                    id_user,
                    id_record_data,
                    *another
                ) in data_file:
                    if not id_user in data:
                        data[id_user] = {}
                    data[int(id_user)][int(id_record_data)] = dict(zip(FEILDS_RECORDS, another))
            case 5:
                from Baza_constanti import FEILDS_LOGS
                KEY_TITLE_LOGIN: int = 1
                KEY_TITLE_PAS: int = 2
                KEY_TITLE_ROLE: int = 3
                for id_data, log_data, pass_data, role_data in data_file:
                    data[int(id_data)] = {
                        FEILDS_LOGS[KEY_TITLE_LOGIN]: log_data, 
                        FEILDS_LOGS[KEY_TITLE_PAS]: pass_data.rstrip('\n'),
                        FEILDS_LOGS[KEY_TITLE_ROLE]: role_data.rstrip('\n').strip(),
                        }
            case _:
                print('Неизвестный код конфига')
    return data

def load_all(db_config, logs_config):
    from Baza_constanti import CODE_CONFIG_DB, CODE_CONFIG_LOGS
    db = load_file(CODE_CONFIG_DB,db_config['path'])
    logs = load_file(CODE_CONFIG_LOGS,logs_config['path'])
    return db, logs

def save_all(db, logs, db_path, logs_path):
    from Baza_constanti import FEILDS_LOGS, FEILDS_DESCRIPTION
    from interaction_function.base import row_write


    with (open(db_path, 'wt', encoding='utf-8') as db_file,
    open(logs_path, 'wt', encoding='utf-8') as logs_file): 
        print(row_write(FEILDS_LOGS), file=logs_file, end='')
        for user_id, user_congif in logs.items():
            print('', file=logs_file)
            print(row_write((user_id, *user_congif.values())), file=logs_file, end='')
        print(row_write(FEILDS_DESCRIPTION.keys()), file=db_file, end='')
        for user_id in db:
            for records_id, records_congif in db[user_id].items():
                print('', file=logs_file)
                print(row_write((user_id, records_id, *records_congif.values())),  file=db_file, end='')