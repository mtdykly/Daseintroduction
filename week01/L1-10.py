str=input("请输入")
length=len(str)
count=0
for i in range(length-1):
    j=i+1
    if(str[j]==str[i]):
        count+=1
        break
if count==0:
    print("不存在")
else:
    print("存在")