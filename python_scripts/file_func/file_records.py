def reg_new_user(logs) -> int:
    '''Function creates a new user and returns his id.'''
    from interaction_function.base import create_user, logs_update
    if logs:
        last_id: int = max(map(int, tuple(logs.keys())))
        id_new_user: int = last_id + 1
    else:
        id_new_user: int = 0
    new_user: tuple[str, str,str] = create_user(id_new_user)
    logs = logs_update(logs, new_user)
    return id_new_user, logs
