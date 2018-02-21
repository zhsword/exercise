import os
all_files = os.listdir(os.curdir)    #os.listdir() 返回指定的文件夹包含的文件或文件夹的名字的列表。 os.curdir() 返回当前目录。 os.getcwd() 返回当前工作目录
type_dict = dict()

for each_file in all_files:
	if os.path.isdir(each_file):    #os.path.isdir(path) 如果path是一个存在的目录，返回True，否则返回False
		type_dict.setdefault('文件夹', 0)
		type_dict['文件夹'] += 1
	else:
		ext = os.path.splitext(each_file)[1]    #os.path.splitext() 分离文件名和扩展名，默认返回（fname, fextension）元组  os.path.split(path) 将path分割成目录和文件名二元组返回
		type_dict.setdefault(ext, 0)    #dict.setdefault(key, default = None) 返回指定键的值，如果该键不存在，则会添加；default -- 键不存在时设置的默认键值
		type_dict[ext] += 1
for each_type in type_dict.keys():    #dict.keys() 以列表形式返回字典所有的键
	print('该文件下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))
