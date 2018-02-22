import os

def search_file(star_dir, target):
	os.chdir(star_dir)    #os.chdir() 改变当前的工作目录
	
	for each_file in os.listdir(os.curdir): #os.listdir() 返回指定文件夹包含的文件或文件夹的名字
		if  each_file == target:
			print(os.getcwd() + os.sep + each_file)     # os.sep给出当前操作系统特定的路径分割符号
		if os.path.isdir(each_file):    #os.path.isdir() 判断路径是否为目录
			search_file(each_file, target)    #递归调用
			os.chdir(os.pardir)    #os.pardir() 上层目录
			
star_dir = input('请输入待查的初始目录：')
target = input('请输入需要查找的文件：')
search_file(star_dir, target)


# 如下返回视频格式的文件
import os

def search_file(start_dir, target) :
    os.chdir(start_dir)
    
    for each_file in os.listdir(os.curdir) :
        ext = os.path.splitext(each_file)[1]
        if ext in target :
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep) # os.linesep给出当前操作系统特定的行终止符
        if os.path.isdir(each_file) :
            search_file(each_file, target) # 切记是each_file，而不是star_dir
            os.chdir(os.pardir)

start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()

target = ['.mp4', '.avi', '.rmvb']
vedio_list = []

search_file(start_dir, target)

f = open(program_dir + os.sep + 'vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()
