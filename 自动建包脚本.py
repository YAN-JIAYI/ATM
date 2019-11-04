import os

base_path = os.path.dirname(__file__)

dir_dict = {
    'core': ['src.py'],
    'lib': ['common.py'],
    'interface': ['user_interface.py', 'bank_interface.py', 'shop_interface.py'],
    'db': ['db_handler.py'],
    'log': [],
    'conf': ['setting.py']}

for dir, file_lis in dir_dict.items():
    if not os.path.exists(dir):
        os.mkdir(dir)
        dir_path = os.path.join(base_path,dir)
        for file in file_lis:
            f = open(os.path.join(dir_path,file),'w',encoding='utf8')
            f.close()
