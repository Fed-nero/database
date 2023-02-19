from os.path import abspath, exists, split as filesplit, join

ABSOLUTEPATH: str = abspath(__file__)
PATH_DB: str = r'c:\Users\fmile\Desktop\BOT(Fedor)\DATABASE.txt'
DERFILE, NAMEFILE = filesplit(ABSOLUTEPATH)
NAMEDB: str = 'DATABASE.txt'
POSITIVE: int = 1
NEGATIVE: int = 0
POSITIVE_LIST: tuple = ('да', 'ага', '+', 'yes', 'yep', 'ya', 'ofcourse', )
NEGATIVE_LIST: tuple = ('нет', 'не', '-', 'no', 'nope', 'nah', 'иди нафиг', )
EXIT: int = NEGATIVE
FEILDS: tuple = ('ID', 'DATATIME', 'DESCRIPTION', 'DURATION', 'AUTOR', 'NOTIFICATION', 'TEXT_NOTIFICATION')
SEPARATION: str = '\t' * 3


def input_int(request: int, min = '', max = '') -> int:
    data: str = ''
    if min and max:
        request += f'(Number should be in the rande from {min} and {max})'
    else:
        if min == -1:
            request += f'(Number should be positive):'
        elif min:
            request += f'(Number should be bigger {min}):'
        elif max == 1:
            request += f'(Number should be negative):'
        elif max:
            request += f'(Number should be smaler {max}):'
    while not all((
        data.isdigit(),
        (not min or int(data) > int(min)),
        (not max or int(data ) < int(max))
    )):
        data = input()


def answer(
    request: str, 
    natification: str='', 
    positive_list = POSITIVE_LIST, 
    negative_list = NEGATIVE_LIST
) -> int:
    '''Function for geting answers from users.'''
    user_answer: str = ''
    if natification:
        print(natification)
    while user_answer not in positive_list + negative_list:
        print(request)
        user_answer = input()
        if user_answer in positive_list:
            return POSITIVE
        elif user_answer in negative_list:
            return NEGATIVE
        else:
            print("I don't understand you :(")
            print('I only understand thees answers:')
            print(*(positive_list+negative_list), sep='\n')
        

def registor_path() -> int:
    '''Registrade a path do the database file.'''
    data: list = []
    global PATH_DB
    if not exists(PATH_DB):
        if answer(
            "Do you want to create a database file in the same plase with program?", 
            natification=f'If you say yes file will be loade in this directory:\n{DERFILE}'
            ):
            PATH_DB = join(DERFILE, NAMEDB)
        else:
            PATH_DB = join(input("Enter derictory's full path"), NAMEDB)
        try:
            with open(PATH_DB, 'wt', encoding='utf') as create_file:
                print('', end='', file=create_file)
        except:
            return NEGATIVE
        with open(ABSOLUTEPATH, 'rt', encoding='utf') as main_file:
            data = main_file.readlines()
        for index,row in enumerate(data):
            if 'PATH_DB: str = r' in row:
                data[index] = f"PATH_DB: str = r'{PATH_DB}'\n"
                break
        with open(ABSOLUTEPATH, 'wt', encoding='utf') as main_file:
            print(*data, sep='', end='', file=main_file)
        return POSITIVE


def row_feel(data: tuple) -> str:
    '''Converts tuples in to text for database'''
    return SEPARATION.join(map(str, data))


def row_read(data: str) -> tuple:
    '''Converts from database text to tuples'''
    return tuple(data.split(SEPARATION))


def feel_db() -> int:
    '''Koroche prosto na izi tipo zapolnayet bazu (eto baza!).'''
    login = input('введите свой <LOGIN>: ')
    password = input('введите свой <PASSWORD>: ')
    all_records: list = []
    amount: int = int(input())#input_int('Сколько записей вы желаете сейчас создать?', min = -1)
    for i in range(amount):
        record: tuple = [i, login]
        print(f'Создаём запись №{i + 1}:')
        for field in FEILDS[2:]:
            record.append(input(f'Введите <{field}>: '))
        all_records.append(row_write(tuple(record)))
    with open(PATH_DB, 'wt', encoding='utf-8') as DATABASE:
        print(row_write(FEILDS), file = DATABASE)
        print(*all_records, sep ='\n', end = '', file = DATABASE)
    print('Создание базы записей прошло успешно')



def create_db() -> int:
    '''Creates a data base if it is not found.'''
    if answer('Do you wanna create database?', natification="App won't work with out database"):
        registor_path()
        feel_db()
        return POSITIVE
    return NEGATIVE
        

def check_db() -> int:
    '''Checks database.'''
    if exists(PATH_DB):
        return POSITIVE
    print('Database is not found :(')
    return NEGATIVE


def main() -> None:
    '''Main function'''
    if check_db():
        print('Database is found')
    else:
        if create_db():
            print('Database is created sucssesfuly')
        else:
            print('Program have succsesfuly ended')
            return EXIT


if __name__ == '__main__':
    '''Checks that the program is launched but nod used like a module.'''
    main()