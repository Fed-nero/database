'''List of constants for the project'''

from os.path import split as filesplit, abspath
from Main import ABSOLUTEPATH

CODE_CONFIG_LOGS: int = 5
CODE_CONFIG_DB: int = 6
CODE_CREATE_CREATOR: int = 7

MIN_LOGIN_LENGHT: int = 3
MAX_LOGIN_LENGHT: int = 15

PRAVELNIE_SLOVA_DLYA_USER: str = 'YOU STUPID DUMB SHIT YOU MOM IS IN CANAVA AND DAD WENT FOR HLEB. YOU ARE SO DUMB THAT EVEN FEDYA IS SMARTER THAN YOU'

PASSWORD_LEN_MIN: int = 7
PASSWORD_LENLMAX: int = 15
PASSWOED_RPEAT_CHAR_MAX: int = 3

ABSPATH: str = abspath()
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
UNKNOWN: int = -1
UNKNOWN_STR: str = ''
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
    'ROLE',
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

KEY_LANG: str = UNKNOWN_STR

LANG_TO_CHOUSE: tuple[str] = (
    'Русский',
    'English',
    'Italiano',
    'Español',
    'Polski',
    '中國人',
    '日本',
    'հայերեն',
    'عرب',
    'Deutsch',
)