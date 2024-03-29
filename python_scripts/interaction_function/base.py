'''This file is for functions for base.'''

def row_write(data: tuple) -> str:
    '''Converts tuples in to text for database'''
    from Baza_constanti import SEPARATION
    return SEPARATION.join(map(str, data))


def row_read(data: str) -> tuple:
    '''Converts from database text to tuples'''
    from Baza_constanti import SEPARATION
    return tuple(data.split(SEPARATION))


def create_user(id: int, role: str = 'User') -> tuple:
    '''Create a new user.'''
    from interaction_function.user import get_login, get_password
    user_id: int = id
    user_login: str = get_login()
    user_password: str = get_password()
    user_role: str = role
    return user_id, user_login, user_password, user_role


def create_records(id: int) -> str:
    from Main import CREATOR_ID, user_id
    from time import ctime, time
    from Baza_constanti import FEILDS_DESCRIPTION
    index_first_field_man: int = tuple(FEILDS_DESCRIPTION.keys()).index('DATATIME')
    time_now = ctime(time())
    record_id: int = id
    record: list = [user_id, record_id, time_now, ]
    for field in tuple(FEILDS_DESCRIPTION.keys()) [index_first_field_man:]:
        record.append(input(f'Введите <{FEILDS_DESCRIPTION[field]}>: '))
    return row_write(record)

def logs_update(logs, *users:tuple):
    from Baza_constanti import FEILDS_LOGS
    KEY_TITLE_LOG: int = 1
    KEY_TITLE_PAS: int = 2
    KEY_TITLE_ROLE: int = 3
    for user in users:
        id,log,pas,role = user
        logs[id] = {
            FEILDS_LOGS[KEY_TITLE_LOG]: log,
            FEILDS_LOGS[KEY_TITLE_PAS]: pas,
            FEILDS_LOGS[KEY_TITLE_ROLE]: role,
        }
    return logs