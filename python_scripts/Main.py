from os.path import abspath



ABSOLUTEPATH: str = abspath(__file__)


def main() -> None:
    '''Main function'''
    from Baza_constanti import UNKNOW, DATA_BASE, LOGS_FILE
    from file_func.file_base import check
    user_id: int = UNKNOW
    if all((check(LOGS_FILE), check(DATA_BASE))):
        print('All fiells is loaded sucsessful')
        ...
    else:
        print('Program have succsesfuly ended')


if __name__ == '__main__':
    '''Checks that the program is launched but nod used like a module.'''
    main()