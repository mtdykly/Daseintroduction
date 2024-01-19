x=eval(input("请输入一个数字"))
def fun(x):
    down=1
    up=x
    while up-down>1e-6:
        mid=(up+down)/2
        if mid**3<x:
            down=mid
        else:
            up=mid
    return mid
print(fun(x))