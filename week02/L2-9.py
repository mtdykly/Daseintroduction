#蒙特卡洛法求定积分
import random
import math
DARTS=1000*1000
hits=0.0
for i in range(1,DARTS+1):
    x=random.uniform(2,3)
    y=random.uniform(0,21)
    if y<=x**2+4*x*math.sin(x):
        hits=hits+1
result=(hits/DARTS)*21
print("定积分是：%.12f"%result)