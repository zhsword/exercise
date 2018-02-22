def file_write(file_name):
	f = open(('%s.txt' % file_name ) , 'w')
	print('请输入文件内容【单独输入“:c”保存退出】：')
	
	while True:
		write_content = input()
		if write_content != ':c':
			f.write('%s\n' % write_content)
		else:
			break			
	f.close()
	
file_name = input('请输入文件名：')
file_write(file_name)
