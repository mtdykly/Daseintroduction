A=input("请输入一个数组 用空格隔开:").split(' ')
A=[int(x) for x in A]
B=[0 for i in range(len(A))]
for i in range (len(A)):
    B[i]=1
    for j in range(len(A)):
        if i!=j:
            B[i]=B[i]*A[j]
print(B)