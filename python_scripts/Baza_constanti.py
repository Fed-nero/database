'''List of constants for the project'''

from os.path import split as filesplit
from Main import ABSOLUTEPATH

CODE_CONFIG_LOGS: int = 5
CODE_CONFIG_DB: int = 6
CODE_CREATE_CREATOR: int = 7

PASSWORD_LEN_MIN: int = 7
PASSWORD_LENLMAX: int = 15
PASSWOED_RPEAT_CHAR_MAX: int = 3

PATH_DB: str = r'c:\Users\fmile\Desktop\BOT(Fedor)\database\python_scripts\DATABASE.txt'
PATH_LOGS: str = r'c:\Users\fmile\Desktop\BOT(Fedor)\database\python_scripts\LOGS.txt'
CONST_FILE_NAME: str = 'Baza_constanti.py'
DERFILE, NAMEFILE = filesplit(ABSOLUTEPATH)
NAMEDB: str = 'DATABASE.txt'
NAMELOGS: str = 'LOGS.txt'
POSITIVE: bool = True
NEGATIVE: bool = False
POSITIVE_LIST: tuple = ('да', 'ага', '+', 'yes', 'yep', 'ya', 'ofcourse', 'y', 'д' )
NEGATIVE_LIST: tuple = ('нет', 'не', '-', 'no', 'nope', 'nah', 'n', 'н' )
EXIT: int = NEGATIVE
UNKNOW: int = -1
DATA_BASE: dict = {
    'path': PATH_DB,
    'name': 'Database',
    'global_name': NAMEDB,
    'global_var_path': 'PATH_DB',
}

LOGS_FILE: dict = {
    'path': PATH_LOGS,
    'name': 'Logs file',
    'global_name': NAMELOGS,
    'global_var_path': 'PATH_LOGS',
}

FEILDS_DESCRIPTION: dict = {
    'ID': 'unice auntithicator',
    'ID_RECORD': 'Уникальный номер записи', 
    'TIME_CREATIVE': 'time of crating reminder', 
    'DATATIME': 'reminding time', 
    'DESCRIPTION': 'description', 
    'DURATION': 'duration', 
    'CLIENT': 'name of client', 
    'NOTIFICATION': 'how important it is', 
    'TEXT_NOTIFICATION': 'text of notification'
}
FEILDS_LOGS: tuple = (
    'ID',
    'LOGIN',
    'PASSWORD',
)
FEILDS_RECORDS: tuple = (
    'TIME_CREATIVE',
    'DATATIME',
    'DESCRIPTION',
    'DURATION',
    'CLIENT',
    'NOTIFICATION',
    'TEXT_NOTIFICATION',
)
SEPARATION: str = '\t' * 3