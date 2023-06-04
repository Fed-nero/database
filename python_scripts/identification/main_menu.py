def identification_menue(logs) -> int:
    '''This menue opens when user launched idenifies him and returns his id.'''
    

    def identify_user(logs) -> int:
        from typing import Callable
        from Baza_constanti import PATH_LOGS
        
        #Making a code more chetayemiy = refactoring

        def generate_function_parse_id(login: str, entered_password_hash: str) -> Callable[[str], int]:
            from Baza_constanti import SEPARATION
            def parse_id(row: str) -> int:
                print(row)
                user_id, user_login, user_pas_hash = row.split(SEPARATION)
                if login == user_login and entered_password_hash == user_pas_hash:
                    print(user_id)
                    return int(user_id)
                return -1
            return parse_id
        
        def make_request_user_login() -> str:
            '''This function returns True if user entered login or False if the user wants to cancel the login and return.'''
            candidate_login: str = '-'
            while candidate_login:
                candidate_login = input('Enter your login, but if you want to return to entering a password don\'t enter anything\n')#экранизация
                if check_logins(candidate_login):
                    return candidate_login
            return ''
        
        def check_db_password(check: Callable[[str], id]) -> bool:
            with open(PATH_LOGS, 'rt', encoding='utf-8') as log_file_tovarishi:
                    log_file_tovarishi.seek(0)
                    log_file_tovarishi.readline()
                    for row in log_file_tovarishi:
                        if (result := check(row)) != -1:
                            return result
                    return False
            
        def make_request_user_password(login: str) -> bool:
            '''This function returns True if user entered password or False if the user wants to cancel the password and rewrite login.'''
            from interaction_function.hash import get_hash
            candidate_password: str = '-'
            candidate_password_hash: str = ''
            while candidate_password:
                candidate_password = input('Enter your password, but if you want to return to entering a password don\'t enter anything\n')#экранизация
                candidate_password_hash = get_hash(candidate_password)
                check_functions_compare_password: Callable[[str], id] = generate_function_parse_id(login, candidate_password_hash)
                if id_user:=check_db_password(check_functions_compare_password):
                    return id_user
            return False
        
        from interaction_function.functions_to_work_with_logs.checks_logs import check_logins
        #visualnoye razdeleniye
        while login := make_request_user_login():#Making request to the user to get his login if user stops this operation then we return him to the main menue
            if iduser := make_request_user_password(login):#If user entered correct log in then we start making request about his password
                return iduser, logs#If user entered correct login and password from database then we return his id
        return ''

        
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
        'Login' : identify_user,
        'Signup' : reg_new_user,
        'Setings' : 3,
        'Support' : 4,
        'Exit' : exit,
    }

    while True:
        print('\nMenue:\n')
        for menue_point, menu_description in POINT_ACTION.items():
            print(f'\t{menue_point}) {menu_description}\n')
        
        print('Choose a number')
        responce_user: str = ''
        while responce_user not in (tuple(POINT_ACTION.keys()) + tuple(POINT_ACTION.values())):
            responce_user = input('> ').strip().capitalize()
            if responce_user in POINT_ACTION.keys():
                server_function_mujiki = (ACTION_FUNCTION[POINT_ACTION[responce_user]])
            elif responce_user in ACTION_FUNCTION.values():
                server_function_mujiki = ACTION_FUNCTION[responce_user]
            else:
                print('Incorect input')
            if server_function_mujiki and (result_function := server_function_mujiki(logs)):
                return result_function
