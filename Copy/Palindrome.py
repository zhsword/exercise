string = input('请输入字符串：')
flag = True

for i in range(len(string)//2):
        if string[i] != string[len(string) -i - 1]:
            flag = False
            break
if flag:
    print ('是回文')
else:
    print ('不是回文')

#大神
str1 = input('请输入字符串：')
str2 = str1[::-1]
if str1 == str2:
    print ('是回文')
else:
    print ('不是回文')
    
#[::-1] 切片
#http://www.cnblogs.com/hiwuchong/p/8052502.html
