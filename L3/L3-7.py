x=int(input("请输入第一个正整数："))
y=int(input("请输入第二个正整数："))
gcd=1
for i in range (2,min(x,y)+1):
    if x%i==0 and y%i==0:
        gcd=i
    else:
        i+=1
print("最大公约数是%d"%gcd) 