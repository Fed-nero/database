'''Main code.'''

from os.path import abspath


ABSOLUTEPATH: str = abspath(__file__)
CREATOR_ID:bool = False
user_id: int = 0

def main() -> None:
    '''Main function'''
    from Baza_constanti import DATA_BASE, LOGS_FILE, CODE_CREATE_CREATOR
    from file_func.file_base import check
    from identification.main_menu import identification_menue
    from typing import Union

    global user_id
    code_existance_creator: Union[bool, int]
    if all((code_existance_creator:= check(LOGS_FILE), check(DATA_BASE))):
        print('All fiells is loaded sucsessful')
        if not code_existance_creator == CODE_CREATE_CREATOR:
            user_id = identification_menue()
        print(f"User id-{user_id}")
    else:
        print('Program have succsesfuly ended')


if __name__ == '__main__':
    '''Checks that the program is launched but nod used like a module.'''
    main()