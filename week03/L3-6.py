grade=eval(input("请输入你的成绩："))
if grade<60 and grade>=0:
    print("您的等级为不合格")
elif grade>=60 and grade<=74:
    print("您的等级为合格")
elif grade>=75 and grade<=89:
    print("您的等级为良好")
elif grade>=90:
    print("您的等级为优秀")
else:
    print("请重新输入成绩")