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

def correct_case(title_content: str, content: str) -> str:
    var: dict = {
        '1': content.capitalize(),
        '2': content.title(),
        '0': content,
    }
    content_perfect: str = ''
    content_capitalize: str = var['1']
    if content == content_capitalize:
        print('Не забывайте о том, что в {title_content} регистр имеет значение!')
        content_perfect = content
    else:
        print(f'У вас нестандартный регистр в поле ввода {title_content}')
        print('Вы можете изменить его при желании')
        for key, item in var.items():
            print(f'{key}) {item}')
        print('Выберите номер варианта:')
        key_var: str = input('> ')
        if key_var in var:
            content_perfect = var[key_var]
        else:
            print('Вы ввели некоректный ключ, вам будет присвоен {title_content}:')
            content_perfect = var['1']
            print(content_perfect)
    return content_perfect


def perfect_content(title_content: str):
    potent_content: str = content_without_space(title_content)
    return correct_case(title_content, potent_content)

def get_login() -> str:
    potent_login: str = perfect_content('login')
    ...


def get_password() -> str:
    potent_password: str = perfect_content('password')
    ...