'''This file is for functions for user.'''


def answer(
    request: str, 
    natification: str = ' ', 
    positive_list: tuple = tuple(), 
    negative_list: tuple = tuple()
) -> bool:
    '''Function for geting answers from users.'''
    from Baza_constanti import (
        POSITIVE, 
        NEGATIVE, 
        POSITIVE_LIST, 
        NEGATIVE_LIST
    )
    user_answer: str = ''
    if natification:
        print(natification)
    if not positive_list:
        positive_list = POSITIVE_LIST
    if not negative_list:
        negative_list = NEGATIVE_LIST
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


def input_int(request: str, min: str = '', max: str = '') -> int:
    NUBER_POSITIVE_MIN: int = 1
    NUBER_NEGATIVE_MAX: int = -1
    data: str = ''
    if min and max:
        request += f'(Number should be in the rande from {min} and {max})'
    else:
        if min == NUBER_NEGATIVE_MAX:
            request += f'(Number should be positive):'
        elif min:
            request += f'(Number should be bigger {min}):'
        elif max == NUBER_POSITIVE_MIN:
            request += f'(Number should be negative):'
        elif max:
            request += f'(Number should be smaler {max}):'
    while not ((
        data.isdigit() or
        (not min or int(data) > int(min)) or
        (not max or int(data) < int(max))
    )):
        print(request)
        data = input()
    return int(data)

def content_without_space(title_content: str) -> str:
    print(f'Enter your {title_content}:')
    content: str = input('> ')
    potent_content: str = content.strip()
    if not content == potent_content:
        print('Spaces will be deleted')
        content = potent_content
        print(f'Your {title_content} will look loke this: {content}')
    return content


def get_login() -> str:
    potent_login: str = content_without_space('login')
    ...


def get_password() -> str:
    from Baza_constanti import PASSWORD_LEN_MIN, PASSWORD_LENLMAX
    def check_len(user_password: str) -> bool:
        return PASSWORD_LEN_MIN <= len(user_password) <= PASSWORD_LENLMAX
    
    def check_chars_exist(user_password: str) -> bool:
        number_flag: bool = False
        spec_flag: bool = False
        letter_flag: bool = False
        for char in user_password:
            if char in '0123456789':
                number_flag = True
            elif char in '!@#$%^&*()_+-="№;:?\'\\|/<>,.~`':
                spec_flag = True
            else:
                letter_flag = True
            if all((number_flag, spec_flag, letter_flag)):
                return True
        return False
    
    def check_content_uniqe(user_password: str) -> bool:
        forbid_words:tuple[str] = (
            'qwe'
            'qwerty'
            'zxc'
            'abs'
            'asd'
            '123'
            '987'
            'pas'
            '12345678'
        )
        return not any((forbid_words in user_password for forbid_word in forbid_words))
    
    def check_case(user_password: str) -> bool:
        lower_case: bool = False
        upper_case: bool = False
        for char in user_password:
            if 'a' <= char <= 'z' or 'а' <= char <= 'я':
                lower_case = True 
            elif 'A' <= char <= 'Z' or 'А' <= char <= 'Я':
                upper_case = True 
            if all((lower_case, upper_case)): 
                return True
        return False
        
    def check_repeat_char(user_password: str) -> bool:
        from Baza_constanti import PASSWOED_RPEAT_CHAR_MAX
        char_before: str = user_password[0]
        counter_repeat_now: int = 1
        counter_repeat_global: int = 0
        for char in user_password[1:]:
            if char == char_before:
                counter_repeat_now += 1
            else:
                counter_repeat_global = max(counter_repeat_global, counter_repeat_now)
                counter_repeat_now = 1
            char_before = char
        counter_repeat_global = max(counter_repeat_global, counter_repeat_now)
        return counter_repeat_global <= PASSWOED_RPEAT_CHAR_MAX
    potent_password: str = ''
    while not (potent_password and all(result_check)):
        if potent_password:
            for index, value in enumerate(result_check):
                if not value:
                    match index:
                        case 0:
                            print(f'Длина пароля должна быть в дапазоне от {PASSWORD_LEN_MIN} до {PASSWORD_LENLMAX} символов.')
                        case 1:
                            print('Пароль должен содержать буквы, цифры и спец. символы.')
                        case 2:
                            print('Пароль не должен содержать частоиспользуемые сочетания символов.')
                        case 3:
                            print('Пароль должен содержать буквы разных регистров.')
                        case 4:
                            print('Too much of symbol repeating')
                        case _:
                            print('Unknown error')
        potent_password: str = content_without_space('password')
        result_check: tuple[bool] = (
            check_len(potent_password),
            check_chars_exist(potent_password),
            check_content_uniqe(potent_password),
            check_case(potent_password),
            check_repeat_char(potent_password)
        )
    print('the pasword is perfect!')
    return potent_password