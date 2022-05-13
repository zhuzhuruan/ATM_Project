'''用户视图层'''
from interface import user_interface
from lib import common


# 全局变量，用于记录用户是否已登录
login_user = None

# 1、注册功能
def register():
    while True:
        # 1）让用户输入用户名和密码进行校验
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()
        re_password = input('请确认密码：').strip()

        if password == re_password:
            # 2）调用接口层的注册接口，将用户名与密码交给接口层处理
            flag, msg = user_interface.register_interface(username, password)   # {False, '用户名已存在'}
            # 3）根据flag判断用户是否注册成功,用于控制break
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 2、登录功能
def login():
    while True:
        # 1）用户输入用户名和密码
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        # 2）调用接口层，将数据传给登录接口
        flag, msg = user_interface.login_interface(username, password)
        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        else:
            print(msg)


# 3、查看余额
@ common.login_auth
def check_balance():
    pass


# 4、提现功能
@ common.login_auth
def withdraw():
    pass


# 5、还款功能
@ common.login_auth
def repay():
    pass


# 6、转账功能
@ common.login_auth
def transfer():
    pass


# 7、查看流水
@ common.login_auth
def check_flow():
    pass


# 8、购物功能
@ common.login_auth
def shopping():
    pass


# 9、查看购物车
@ common.login_auth
def check_shop_car():
    pass


# 10、管理员功能
def admin():
    pass


# 创建函数功能字典
func_dic = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin
}


# 用户视图层主程序

def run():
    while True:
        print('''
        ===== ATM + 购物车 =====
            1、注册功能
            2、登录功能
            3、查看余额
            4、提现功能
            5、还款功能
            6、转账功能
            7、查看流水
            8、购物功能
            9、查看购物车
            10、管理员功能
        ========= end =========
        ''')
        choice = input('请输入功能编号：').strip()

        if choice not in func_dic:
            print('请输入正确的功能编号！')
            continue
        else:
            func_dic.get(choice)()          # func_dic.get('1')() ------> register()
