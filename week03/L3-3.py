import re
id_number=input("请输入身份证号：")
m=re.match("(^\d{15}$)|(^\d{17}([0-9]|x)$)",id_number)
if m:
    print(m.group(0))
else:
    print("not match")
    