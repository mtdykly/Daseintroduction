import math
a=eval(input("请输入一个整数："))
if a==1:
    print("不是质数")
elif a>1 and a<=3:
    print("是质数")
else:
    sqrt=int(math.sqrt(a))
    flag=0
    for i in range(3,sqrt+1,2):
        if a%2==0 or a%i==0:
            flag=1
            print("不是质数")
            break
    if flag==0:
        print("是质数")
            
    