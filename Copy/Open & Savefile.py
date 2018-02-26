import easygui as g
import os

file_path = g.fileopenbox()
#fileopenbox()返回用户选择的文件名（带完整路径），如果用户选择Cancel则返回None

with open(file_path) as old_file:
    title = os.path.basename(file_path)
    msg = "文件【%s】的内容如下：" % title
    text = old_file.read()
    text_after = g.textbox(msg, title, text)

if text!= text_after[:-1]:  #textbox的返回值会追加一个换行符
    choice = g.buttonbox('检测到文件发生变化','警告', ('覆盖保存', '放弃保存', '另存为'))
    if choice == '覆盖保存':
        with open(file_path, 'w') as old_file:
            old_file.write(text_after[:-1])
    if choice == '放弃保存':
        pass
    if choice == '另存为':
        another_path = g.filesavebox()
#filesavebox()返回用户选择的文件名（带完整路径），如果用户选择Cancel则返回None
        if os.path.splitext(another_path)[1] != '.txt':
            another_path += '.txt'
        with open(another_path, 'w') as new_file:
            new_file.write(text_after[:-1])
