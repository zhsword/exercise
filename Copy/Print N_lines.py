#打印文件的前N行，方法1
file_name = input('请输入要打开的文件：')
file_lines = int(input('请输入要显示前几行：'))
count = 0

f1 = open(file_name)
for each in f1:
	count += 1
	if count <= file_lines:
		print(each)
	else:
		break

f1.close()

#打印文件的前N行，方法2
file_name = input('请输入要打开的文件：')
file_lines = int(input('请输入要显示前几行：'))

f1 = open(file_name)
for i in range(file_lines):
        print(f1.readline(), end = '')
f1.close()

#打印文件的任意N行
file_name = input('请输入要打开的文件：')
file_lines = input('请输入要显示的行数【格式如13:21】：')

while True:
    if ''.join(file_lines.split(':')).isdigit():
        break
    else:
        file_lines = input('您输入的内容有误，请重新输入：')

(begin, end) = file_lines.split(':')

if int(begin) <= 1:
    begin = 0
else:
    begin = int(begin) - 1
    
end = int(end)
f1 = open(file_name)
print(''.join(f1.readlines()[begin:end]).strip('\n'))

f1.close()
