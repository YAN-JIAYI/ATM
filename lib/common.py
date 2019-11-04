from  functools import wraps

def login_auth(func):

    from core import src

    @wraps(func)
    def inner(*args,**kwargs):
        if src.user_info.get('username'):
            res = func(*args,**kwargs)
            return res
        else:
            print('未登录，请去登录')
            src.login()

    return inner




