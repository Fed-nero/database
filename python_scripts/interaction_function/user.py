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