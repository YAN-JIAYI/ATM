from db import db_handler

#提现接口
def withdraw_interface(username,money):
    user_dic = db_handler.select(username)
    withdraw_money = money*1.05
    if user_dic.get('balance') >=  withdraw_money:

        user_dic['balance'] -= withdraw_money
        # 记录流水
        msg= f'{username}提现{money}元成功'
        user_dic['bank_flow'].append(msg)

        db_handler.save(user_dic)
        return True,msg

    return False,f'钱不够，请充值或者重新输入'

#支付还款接口
def repay_interface(username,money):
    user_dic = db_handler.select(username)
    user_dic['balance'] += money
    msg = f'{username}支付还款{money}元成功'
    user_dic['bank_flow'].append(msg)
    db_handler.save(user_dic)
    return msg


#转账接口
def transfer_interface(current_user,to_user,money):
    to_user_dic = db_handler.select(to_user)
    current_user_dic = db_handler.select(current_user)

    if current_user_dic.get('balance') >= money:
        current_user_dic['balance'] -= money
        to_user_dic['balance'] += money
        # 记录流水
        msg= f'{current_user}向{to_user}转账{money}元成功'
        to_user_flow = f'{to_user}收到{current_user}转账{money}元成功'
        current_user_dic['bank_flow'].append(msg)
        to_user_dic['bank_flow'].append(msg)

        db_handler.save(to_user_dic)
        return True,msg
    return False, f'钱不够，请充值或者重新输入'


#查看流水接口
def check_flow_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('bank_flow')



