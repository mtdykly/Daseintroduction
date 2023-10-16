#蒙特卡罗法求π
'''from random import random
DARTS=1000*1000
hits=0.0
for i in range(1,DARTS+1):
    x=random()
    y=random()
    dist=pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits=hits+1
pi=4*(hits/DARTS)
print("圆周率是：%.10f"%pi)
#BBP公式法求π
pi=0
N=eval(input("请输入一个数"))
for k in range(N):
    pi+=1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print(pi)'''
#马青公式计算π
import math
import time
def pi():
    number=20
    time1=time.time()
    b=10**number
    x1=b*4//5
    x2=b//-239
    he=x1+x2
    number*=2
    for i in range(3,number,2):
        x1//=-25
        x2//=-57121
        x=(x1+x2)//i
        he+=x
    pi=he*4
    pi//=10**10
    pistring=str(pi)
    result=pistring[0]+str('.')+pistring[1:len(pistring)]
    return result
print(pi())