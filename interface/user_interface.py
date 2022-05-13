'''用户登入注册接口'''

from db import db_handler
from lib import common

# 注册接口
def register_interface(username, password, balance=15000):
    # 1）查看用户是否存在
    ## 1.1）调用数据处理层中的select方法，会返回用户字典或者None
    user_dic = db_handler.select(username)

    # {user:user, pwd:pwd, ...} or None
    # 如果用户存在，则return，告知用户已存在，重新输入
    if user_dic:
        return False, '用户名已存在！'

    # 组织用户数据的字典信息
    # 密码加密
    password = common.get_pwd_md5(password)

    user_dic = {
        'username': username,
        'password': password,
        'balance': balance,
        'flow': [],  # 记录用户流水的列表
        'shop_car': {},  # 记录用户购物车
        'locked': False  # 记录用户是否被锁定
    }

    # 保存数据
    db_handler.save(user_dic)

    return True, f'{username} 注册成功！'


# 登录接口
def login_interface(username, password):
    # 1）先查看当前用户数据是否存在
    user_dic = db_handler.select(username)      # {用户字典} or None
    if user_dic:
        # 给用户输入的密码加密
        password = common.get_pwd_md5(password)
        # 2）校验密码
        if password == user_dic.get('password'):
            return True, f'用户：[{username}] 登录成功！'
        else:
            return False, f'密码错误'

    return False, '用户不存在，请重新输入！'