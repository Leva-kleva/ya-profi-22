from . import execute, query


def get_user(*args, **kwargs):
    ans = execute(query.get_user, *args, **kwargs)
    return ans


def get_user_by_id(*args, **kwargs):
    ans = execute(query.get_user_by_id, *args, **kwargs)
    return ans

