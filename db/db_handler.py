import json
import os
from conf import setting



def select(username):

    user_path = os.path.join(setting.DB_PATH,
                            f'{username}.json')
    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic



def save(user_dic):

    user_path = os.path.join(setting.DB_PATH,
                             f'{user_dic.get("username")}.json')

    with open(user_path, 'w', encoding='utf-8') as f:
        json.dump(user_dic, f)
        f.flush()