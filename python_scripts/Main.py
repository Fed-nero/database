'''Main code.'''

from os.path import abspath

ABSOLUTEPATH: str = abspath(__file__)
CREATOR_ID:bool = False
user_id: int = 0

def main() -> None:
    '''Main function'''
    from Baza_constanti import DATA_BASE, LOGS_FILE, CODE_CREATE_CREATOR
    from file_func.file_base import check, save_all, load_all
    from identification.main_menu import identification_menue

    global user_id
    
    code_existance_creator: __import__('typing').Union[bool, int]
    if all((code_existance_creator:= check(LOGS_FILE), check(DATA_BASE))):
        print('All fiells is loaded sucsessful')
        db, logs = load_all(DATA_BASE, LOGS_FILE)
        if not code_existance_creator == CODE_CREATE_CREATOR:
            user_id, logs = identification_menue(logs)
        print(f'Wellcome {logs[user_id]["LOGIN"]}!')
        save_all(db, logs, DATA_BASE['path'], LOGS_FILE['path'])

    else:
        print('Program have succsesfuly ended')


if __name__ == '__main__':
    '''Checks that the program is launched but nod used like a module.'''
    main()