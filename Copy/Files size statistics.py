import os
all_files = os.listdir(os.curdir)
file_dict = dict()

for each_file in all_files:
	if os.path.isfile(each_file):      #os.path.isfile() 判断路径是否为文件  
		file_size = type_dict.path.getsize(each_file)    #os.path.getsize() #返回文件大小（byte)
		file_dict[each_file] = file_size

for each in file_dict.items():		#dict.items() 以列表返回可遍历的(键, 值) 元组数组
	print('%s的大小是 【%dBytes】 ' % (each[0], each[1]))
