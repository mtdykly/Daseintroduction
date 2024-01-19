#c的三次方根牛顿迭代式
def cube_root():
    c=10
    g=c/3
    i=0
    while(abs(g**3-c)>0.00000000001):
        g=(2*g+c/(g**2))/3
        i=i+1
        print("%d:%.13f"%(i,g))
cube_root()
        