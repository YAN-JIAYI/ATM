from  interface import bank_interface
from db import db_handler

def shopping_pay_interface(username,shopping_car,cost):
    flag = bank_interface.repay_interface(username,cost)

    user_dic = db_handler.select(username)

    if flag:

        user_dic['shop_car'] = {}
        db_handler.save(user_dic)
        return True,'购物并支付成功'

    #若失败，保存购物车
    else:
        user_dic['shop_car'] = shopping_car
        db_handler.save(user_dic)
        return False,'支付失败，保存购物车'

#添加购物车接口
def shopping_car_interface(username,shopping_car):
    #1.获取当前用户
    user_dic = db_handler.select(username)

    #2.添加购物车
    if shopping_car:
        user_dic['shop_car'] = shopping_car
        db_handler.save(user_dic)
        return True,'添加购物车成功'

    else:
        return False,'购物车是空的'




#查看购物车接口
def check_shopping_car_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('shop_car')