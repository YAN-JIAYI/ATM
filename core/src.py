from interface import user_interface
from interface import bank_interface
from interface import shop_interface
from lib import common


user_info = {'username': None}

def register():
    print('欢迎来到注册功能')
    while True:
        username = input('请输入用户名：').strip()
        pwd = input('请输入密码').strip()
        re_pwd = input('请再次输入密码').strip()
        if pwd == re_pwd:
            flag,msg = user_interface.register_interface(username,pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致，请重新注册')
            break


def login():
    print('欢迎来到登录功能')
    while True:
        username = input('请输入用户名：').strip()
        pwd = input('请输入密码').strip()
        flag, msg = user_interface.login_interface(username, pwd)
        if flag:
            print(msg)
            user_info['username'] = username
            break
        else:
            print(msg)


@common.login_auth
def check_balance():
    print('欢迎来到查看余额功能')
    balance = user_interface.check_balance_interface(user_info['username'])
    print(balance)


@common.login_auth
def withdraw():
    print('欢迎来到提现功能')
    while True:
        money = input('请输入提现金额').strip()
        if not money.isdigit():
            print('必须输入数字')
            continue
        money = int(money)
        flag, msg = bank_interface.withdraw_interface(user_info.get('username'), money)
        if flag:
            print(msg)
            break
        else:
            print(msg)


@common.login_auth
def repay():
    print('欢迎来到还款支付功能')
    while True:
        money = input('请输入支付还款金额').strip()
        if not money.isdigit():
            print('必须输入数字')
            continue
        money = int(money)
        msg = bank_interface.repay_interface(user_info.get('username'), money)
        print(msg)
        break



@common.login_auth
def transfer():
    print('欢迎来到转账功能')
    while True:
        to_user= input('请输入目标用户：')
        money = input('请输入转账金额').strip()
        if not money.isdigit():
            print('必须输入数字')
            continue
        money = int(money)
        flag, msg = bank_interface.transfer_interface(user_info.get('username'),to_user, money)
        if flag:
            print(msg)
            break
        else:
            print(msg)



@common.login_auth
def check_flow():
    print('欢迎来到查看流水功能')
    flow_list = bank_interface.check_flow_interface(user_info['username'])
    if flow_list:
        for flow in flow_list:
            print(flow)


@common.login_auth
def shopping():
    print('欢迎来到购物功能')
    good_list = [
        # 商品名, 价格
        ['巨大鸡腿', 50],
        ['红烧羊排', 1000],
        ['清蒸中华鲟', 5000],
        ['西柚炖猪蹄', 1000],
        ['山药排骨汤', 500],
        ['蛋黄小龙虾', 2000],
        ['聚宝盆烧烤', 200],
    ]

    shopping_car = {}
    cost = 0
    user_balance = user_interface.check_balance_interface(user_info.get('username'))
    while True:
        for ind,goods in enumerate(good_list):
            print(ind,goods)
        choice = input('请输入商品编号退出请按q：').strip()
        if choice == 'q':
            break
        if not choice.isdigit():
            print('必须输入数字')
            continue
        choice = int(choice)
        good_name,good_price = good_list[choice]

        if user_balance >= good_price:

            if good_name in shopping_car:
                shopping_car[good_name] += 1

            else:
                shopping_car[good_name] = 1

            cost += good_price


        else:
            print('用户金额不足！')

        if not cost:
            print('没有选择商品')

        # 6.开始结算, 先调用购物车接口, 再通过购物车接口去调用支付接口
    sure = input('是否确认购买，输入y/n').strip()
    if sure == 'y':
        flag, msg = shop_interface.shopping_pay_interface(user_info.get('username'), shopping_car, cost)
        if flag:
            print(msg)

        else:
            print(msg)

    elif sure == 'n':
        # 添加购物车功能
        flag, msg = shop_interface.shopping_car_interface(user_info.get('username'), shopping_car)



@common.login_auth
def shopping_car():
    print('欢迎来到查看购物车功能')
    msg = shop_interface.check_shopping_car_interface(user_info.get('username'))
    print(msg)


def logout():
    print('欢迎来到购注销功能')
    if user_info['username' ]:
        msg = user_interface.logout_interface(user_info.get('username'))
        print(msg)

func_dict = {
    '1':register,
    '2':login,
    '3':check_balance,
    '4':withdraw,
    '5':repay,
    '6':transfer,
    '7':check_flow,
    '8':shopping,
    '9':shopping_car,
    '10':logout,
}





def run():
    while True:
        print('''
        1.注册
        2.登录
        3.查看余额
        4.提现
        5.还款支付
        6.转账
        7.查看流水
        8.购物
        9.查看购物车
        10.注销        
        ''')


        choice = input('请输入你需要的功能编号，退出请按q：').strip()

        if choice == 'q':
            break
        if not choice.isdigit():
            print('请输入纯数字')
            continue
        else:
            choice = func_dict.get(choice)()



