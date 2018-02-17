contracts = dict((('小萌萌',123),('张好人',222)))

def new_user():
    a = '请输入用户名：'
    while True:
        name = input(a)
        if name in contracts:
            a =  '此用户名已占用，请重新输入：'
            continue
        else:
            break
        
    password = input('请输入密码：')
    contracts[name] = password
    print('注册成功')
    

def old_user():
    a = '请输入用户名：'
    while True:
        name = input(a)
        if name not in contracts:
            a =  '此用户名不存在，请重新输入：'
            continue
        else:
            break
        
    b = ('请输入密码：')
    while True:
        password = int(input(b))
        if contracts[name] == password:
            print('欢迎进入系统')
            break
        else:
            b = '密码错误，请重新输入：'
            continue


print('''|--- 新建账号：N/n ---|
|--- 登录账号：E/e ---|
|--- 退出程序：Q/q ---|''')

c = ('请输入指令：')
while True:
    temp = input(c)
    if temp == 'N' or temp == 'n':
        new_user()
        break
    elif temp == 'E' or temp == 'e':
        old_user()
        break
    elif temp == 'Q' or temp == 'q':
        break
    else:
        c = '您输入的指令有错，请重新输入：'
