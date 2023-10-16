def decimal_to_binary_conversion(decimal):
    bins=[]
    while(decimal!=0):
        decimal=decimal*2
        if(decimal>=1):
            bins.append(1)
        else:
            bins.append(0)
        decimal=decimal-int(decimal)
    return bins
decimal=float(input("请输入一个十进制小数"))
print(decimal_to_binary_conversion(decimal))
