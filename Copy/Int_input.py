def int_input(prompt=''):  #有默认参数你不用输入实际参也能调用函数，否则需要输入实参才能调，至于是''还是其他都无所谓
    while True:
        try:
            int(input(prompt))
            break
        except ValueError:
            print('出错，您输入的不是整数！')

int_input('请输入一个整数：')
