x=eval(input("请输入第一个数"))
y=eval(input("请输入第二个数"))
z=eval(input("请输入第三个数"))
if x>y:
    x,y=y,x
if x>z:
    x,z=z,x
if y>z:
    y,z=z,y
print(x,y,z)