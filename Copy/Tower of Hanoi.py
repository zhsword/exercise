# 利用递归函数移动汉诺塔
def move(n, a, b, c):
  if n == 1:
   print (a, '-->', b)
  else:
    move(n-1, a, c, b) #将a的前n-1个盘子从a移动到b
    print (a, '-->', c) #将a最下面的圆盘移动到c
    move(n-1, b, a, c) #将b的n-1个盘子从b移动到c
   
n = int(input('请输入汉诺塔的层数：'))
move (n, 'A', 'B', 'C')
