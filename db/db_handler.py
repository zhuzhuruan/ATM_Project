'''数据处理层'''

# 查看数据
import json
import os
from conf import settings

# 查看数据
def select(username):
    # 1)接收接口层传过来的username，拼接用户json文件路径
    user_path = os.path.join(settings.USER_DATA_PATH, f'{username}.json')

    # 2)校验用户json是否存在
    if os.path.exists(user_path):
        # 3)打开数据，并返回给接口层
        with open(user_path, 'rt', encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic
        # 4)不return，默认返回None


# 保存数据
def save(user_dic):
    # 1）拼接用户的数据字典
    username = user_dic.get('username')
    user_path = os.path.join(settings.USER_DATA_PATH, f'{username}.json')
    # 2）保存用户数据
    with open(user_path, 'wt', encoding='utf-8') as f:
        # ensure_ascii=False：文件中的中文数据显示更加美观
        json.dump(user_dic, f, ensure_ascii=False)