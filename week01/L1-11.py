# S=input("请输入一个字符串")
# temp=S.split()
# print("".join(temp))

s = input("请输入一个字符串：")
# 初始化一个空字符串，用于存储去掉空格后的结果
result_string = ""
# 遍历输入字符串的每个字符
for char in s:
    # 如果字符不是空格，则将其添加到结果字符串中
    if char != " ":
        result_string += char
# 打印去掉空格后的结果
print("去掉空格后的结果为:", result_string)