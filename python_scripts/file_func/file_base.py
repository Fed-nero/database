def reg_path(element: dict) -> bool:
    '''Registrade a path do the element file.'''
    from interaction_function import answer
    from os.path import exists, join
    from Baza_constanti import POSITIVE, NEGATIVE, DERFILE, CONST_FILE_NAME
    data: list = []
    if not exists(element['path']):
        if answer(
            f"Do you want to create a {element['name']} file in the same plase with program?", 
            natification=f'If you say yes file will be loade in this directory:\n{DERFILE}'
            ):
            globals()[element['global_var_path']] = join(DERFILE, element['global_name'])
        else:
            user_direcory: str = input("Enter derictory's full path")
            globals()[element['global_var_path']] = join(user_direcory, element['global_name'])
            try:
                open(join(user_direcory, element['global_name']), 'wt', encoding='utf').close()
            except FileNotFoundError:
                print('Не удалось создать файл в нужной директории')
                return NEGATIVE
        path: str = globals()[element['global_var_path']]
        file_const_path: str = join(DERFILE, CONST_FILE_NAME)
        with open(file_const_path, 'rt', encoding='utf') as save_file:
            data = save_file.readlines()
        for index, row in enumerate(data):
            if f'{element["global_var_path"]}: str = r' in row:
                data[index] = f"{element['global_var_path']}: str = r'{path}'\n"
                break
        with open(file_const_path, 'wt', encoding='utf') as save_file:
            print(*data, sep='', end='', file=save_file)
    return POSITIVE


def feel(element: dict) -> None: #Сделать возможным принудительную регистрацию пользователя
    '''Felling select element.'''
    from interaction_function.user import answer
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
        with open(PATH_LOGS, 'wt', encoding='utf-8') as logs_file:
            print(*data, sep='\n', end='', file=logs_file)   
    elif element == DATA_BASE:
        data = [row_write(tuple(FEILDS_DESCRIPTION.keys())), ]
        if not user_id == UNKNOW and answer(
                'База данных успешно создана, хотите ли вы заполнить её записями?'
            ):
            records_amount: int = int(input('Введите колличество новых записей:'))#
            for i in range(records_amount):
                print(f'Создаём запись №{i + 1}:')
                data.append(create_records(i))
        with open(PATH_DB, 'wt', encoding='utf-8') as data_base_file:
            print(*data, sep='\n', end='', file=data_base_file)


def create(element: dict) -> bool:
    '''Creates a data base if it is not found.'''
    from interaction_function.user import answer
    from Baza_constanti import NEGATIVE, POSITIVE
    if answer(
        f'Do you wanna create {element["name"]}?',
        natification=f"App won't work with out {element['name']}"
    ) and reg_path(element):
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