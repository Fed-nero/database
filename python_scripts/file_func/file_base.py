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


def feel(element: dict) -> None: #Сделать возможным принудительную регистрацию пользователя
    '''Felling select element.'''
    from interaction_function.user import answer
    import Main
    from interaction_function.base import (
        row_write,
        create_user,
        create_records
    )
    from Baza_constanti import (
        LOGS_FILE,
        UNKNOW,
        PATH_DB,
        PATH_LOGS,
        DATA_BASE,
        FIELDS_LOGS,
        FEILDS_DESCRIPTION
    )
    data: list
    if element == LOGS_FILE:
        global user_id
        data = [row_write(FIELDS_LOGS), ]
        if answer(
            'Логс файлы успешно созданы, желаете ли вы создать первого пользователя?'
        ):
            new_user: tuple = create_user(user_id:=0)
            data.append(row_write(new_user))
        with open(element['path'], 'wt', encoding='utf-8') as logs_file:
            print(*data, sep='\n', end='', file=logs_file)  
        Main.CREATOR_ID = True 
    elif element == DATA_BASE:
        data = [row_write(tuple(FEILDS_DESCRIPTION.keys())), ]
        if Main.CREATOR_ID and answer(
                'База данных успешно создана, хотите ли вы заполнить её записями?'
            ):
            records_amount: int = int(input('Введите колличество новых записей:'))#
            for i in range(records_amount):
                print(f'Создаём запись №{i + 1}:')
                data.append(create_records(i))
        with open(element['path'], 'wt', encoding='utf-8') as data_base_file:
            print(*data, sep='\n', end='', file=data_base_file)


def create(element: dict) -> bool:
    '''Creates a data base if it is not found.'''
    from interaction_function.user import answer
    from Baza_constanti import NEGATIVE, POSITIVE
    result_registration: tuple[bool, str]
    KEY_RESULT_REG: int = 0
    KEY_PATH: int = 1
    if answer(
        f'Do you wanna create {element["name"]}?',
        natification=f"App won't work with out {element['name']}"
    ) and (result_registration:= reg_path(element))[KEY_RESULT_REG]:
        element['path'] = result_registration[KEY_PATH]
        feel(element)
        print(f'{element["name"]} is created sucssesfuly')
        return POSITIVE
    return NEGATIVE


def check(element: dict) -> bool:
    '''Checks elements.'''
    from os.path import exists
    result_find =  exists(element['path'])
    print(f"{element['name']} is {('not ', '')[result_find]}found")
    if not result_find:
        result_create: bool = create(element)
        return result_create
    return result_find