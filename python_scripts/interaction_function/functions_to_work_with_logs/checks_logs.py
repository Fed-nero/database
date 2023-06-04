def check_logins(user_login: str) -> bool:
    from Baza_constanti import PATH_LOGS, SEPARATION
    from os.path import exists
    if exists(PATH_LOGS):
        try:
            with open(PATH_LOGS, 'rt', encoding='utf-8') as logs:
                logs.seek(0)
                for line in logs:
                    line_without_space: str = line.strip()
                    login = line_without_space.split(SEPARATION)[1].strip()
                    if user_login == login:
                        return True
        except:
            return False
    return False