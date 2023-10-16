n=int(input("请输入一个数"))
n3=int(n/3)
n2=0
r=n%3
if r==1:
    n3=n3-1
    n2=2
elif r==2:
    n2=1
sum=pow(2,n2)*pow(3,n3)
print("正整数序列是%d个3和%d个2"%(n3,n2))
