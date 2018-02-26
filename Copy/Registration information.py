import easygui as g

msg = "请填写以下联系方式"
title = "账号中心"
fieldNames = [" *用户名", " *真实姓名", "  固定电话", " *手机号码", "  QQ", " *E-mail"]
fieldValues = []
fieldValues = g.multenterbox(msg,title, fieldNames)

while 1:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()
        if fieldValues[i].strip() == "" and option[0] == "*":
            errmsg += ('【%s】为必填项。\n\n' % fieldNames[i])
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

print("用户资料如下：%s" % str(fieldValues))


#糙版
import easygui as g

msg = '请输入账号信息(*是必填项)'
title = '账号中心'
field = ['*用户名', '*邮箱', ' 手机号']
values = g.multenterbox(msg, title, field)


while True:
    ermsg = ''
    for i in range(len(field)):
        if field[i].strip()[0] == '*' and values[i] == '':
            ermsg += ('【%s】必须填\n\n' %field[i])
    if ermsg == '':
        break
    
    values = g.multenterbox(ermsg, title, field, values)

print(str(values))
print(ermsg)
