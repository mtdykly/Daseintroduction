#开平方 牛顿法
def Square_root():
    c=2
    g=c/4
    i=0
    while(abs(g*g-c)>0.00000000001):
        g=(g+c/g)/2
        i=i+1
        print("%d:%.13f"%(i,g))
Square_root()