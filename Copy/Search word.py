import os

def file_key(key_word) :
     for each_file in os.listdir(os.curdir) : #查找所属的文件
        if os.path.splitext(each_file)[1] == '.txt':
            if key_word in open(each_file).read():
                key_path = os.getcwd() + os.sep + each_file
                print('在文件【%s】中找到关键字【%s】'%(key_path,key_word))
 
            f = open(each_file) #查找属于哪行
            row = 0
            for eachline in f:
                row += 1
                if key_word in eachline:
                    print('关键字出现在第 %d 行，'% row,end='')

                    pos = [] #查找属于行的哪个位置
                    begin = eachline.find(key_word)
                    while begin != -1: #str.find(str, beg=0, end=(str)) 如果包含字符串，则返回开始的索引值，否则返回-1
                        pos.append(begin+1) # 用户的角度是从1开始数
                        begin = eachline.find(key_word,begin+1)
                    print('第 %s 个位置。'% pos)
            f.close()
  
        if os.path.isdir(each_file) :
            os.chdir(each_file)
            file_key(key_word)
            os.chdir(os.pardir)

key_word = input('请将该代码放于待查找的文件夹内，请输入关键字：')
file_key(key_word)
