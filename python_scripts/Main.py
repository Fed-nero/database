'''Main code.'''

from os.path import abspath


ABSOLUTEPATH: str = abspath(__file__)
CREATOR_ID:bool = False
user_id: int = 0

def main() -> None:
    '''Main function'''
    from Baza_constanti import UNKNOW, DATA_BASE, LOGS_FILE
    from file_func.file_base import check
    from identification.main_menu import identification_menue
    if all((check(LOGS_FILE), check(DATA_BASE))):
        print('All fiells is loaded sucsessful')
        
        if not CREATOR_ID:
            user_id = identification_menue()
        print(f"User id-{user_id}")
    else:
        print('Program have succsesfuly ended')


if __name__ == '__main__':
    '''Checks that the program is launched but nod used like a module.'''
    main()