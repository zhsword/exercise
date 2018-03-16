import easygui as g
import os

def search_file(star_dir):

    os.chdir(star_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            lines = calc_code(each_file)
            try:
                file_list[ext] += 1
            except KeyError:
                file_list[ext] = 1
                
            try:
                source_list[ext] += lines
            except KeyError:
                source_list[ext] = lines
                

        if os.path.isdir(each_file):
            search_file(each_file)
            os.chdir(os.pardir)

def calc_code(file_name):
    lines = 0
    with open(file_name) as f:
        print('正在分析文件：%s' % file_name)
        try:
            for eachline in f:
                lines += 1
        except UnicodeDecodeError:
            pass
    return lines

def show_result(star_dir):
    lines = 0
    total = 0
    text = ''

    for i in source_list:
        lines = source_list[i]
        total += lines
        text += "%s 源文件 %d 个，源代码 %d 行 \n" % (i, file_list[i], lines)
    title = '统计结果'
    msg = '您目前累计编写代码 %d 行，完成进度 %.2f %%\n' %(total, total/1000)
    g.textbox(msg,title, text)

target = ['.py']
file_list = {}
source_list = {}

g.msgbox('请打开您存放代码的文件夹', '统计代码量')
path = g.diropenbox('请选择您的代码文件夹')

search_file(path)
show_result(path)
