def identification_menue(logs) -> int:
    '''This menue opens when user launched idenifies him and returns his id.'''
    from typing import Callable, Union
    from file_func.file_records import reg_new_user

    POINT_ACTION: dict[str, str] = {
        '1': 'Login',
        '2': 'Signup',
        '3': 'Setings',
        '4': 'Support',
        '5': 'Exit',
    }
    ACTION_FUNCTION: dict[str, Callable[[], Union[int, None]]]
    ACTION_FUNCTION = {
        'Login' : 1,
        'Signup' : reg_new_user,
        'Setings' : 3,
        'Support' : 4,
        'Exit' : exit,
    }

    print('\nMenue:\n')
    for menue_point, menu_description in POINT_ACTION.items():
        print(f'\t{menue_point}) {menu_description}\n')
    
    print('Choose a number')
    responce_user: str = ''
    while responce_user not in (tuple(POINT_ACTION.keys()) + tuple(POINT_ACTION.values())):
        responce_user = input('> ').strip().capitalize()
        if responce_user in POINT_ACTION.keys():
            return ACTION_FUNCTION[POINT_ACTION[responce_user]](logs)
        elif responce_user in ACTION_FUNCTION.values():
            return ACTION_FUNCTION[responce_user](logs)
        else:
            print('Incorect input')