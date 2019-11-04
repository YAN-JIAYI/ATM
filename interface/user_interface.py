from db import db_handler
from core import src

#注册接口
def register_interface(username,pwd):

    user_dic = db_handler.select(username)
    if user_dic:
        return False,'用户已经存在'
    user_dic = {
        'username':username,
        'pwd':pwd,
        'balance':15000,
        'bank_flow':[],
        'shop_car':{}
    }
    db_handler.save(user_dic)
    return True,f'{username}注册成功'


#登陆接口
def login_interface(username,pwd):
    user_dic = db_handler.select(username)
    if not user_dic:
        return False, '用户不存在，请先注册'
    if user_dic:
        if user_dic.get('pwd')== pwd:
            return True,'登陆成功'

        else:
            return False,'密码不正确'


#查询余额接口

def check_balance_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('balance')


#注销接口
def logout_interface(username):
    src.user_info['username'] = None
    return '注销成功'









