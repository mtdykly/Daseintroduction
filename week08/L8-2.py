import matplotlib.pyplot as plt
import numpy as np
# 中文乱码的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']# 设置微软雅黑字体
plt.rcParams['axes.unicode_minus'] = False # 避免坐标轴不能正常的显示负号

y=np.random.randn(100)
x=np.arange(100)

plt.figure(figsize=(10,10))
#创建画纸1
#折线图
ax1=plt.subplot(221)
plt.plot(x,y,color='r')
#坐标轴范围
#plt.axis([0,6,0,20])
#x轴文本
plt.xlabel('x值')
#y轴文本
plt.ylabel('y值')
#标题
# plt.title('标题')
#添加注释
#plt.annotate('我是注释',xy=(2,5),xytext=(2,10),arrowprops=dict(facecolor='black',shrink=0.02))
# #创建画板
# fig=plt.figure(1)
# plt.plot(x,y,color='r',marker='o',linestyle='dashed')

#选择画纸2
#散点图
colors=np.random.randn(100)
ax2=plt.subplot(222)
plt.scatter(x,y,
            #大小
            s=np.power(3*y,2),
            #颜色
            c=colors,
            #透明度
            alpha=0.9)


#选择画纸3
#简单垂直条形图
ax3=plt.subplot(223)
GDP = [36102,38700,14083,25002]
city = ['北京市', '上海市', '天津市', '重庆市']
plt.bar(city, GDP, align='center', color='steelblue', alpha=0.8)
plt.ylabel('GDP')
plt.title('2020年四大直辖市GDP条形图')
plt.ylim([10000, 42000])

# 为每个条形图添加数值标签：ha='center'
for x,y in enumerate(GDP):
    plt.text(x, y+200, '%s'%y, ha='center')

#选择画纸4
#简单频数直方图
ax4=plt.subplot(224)
data=np.random.randn(1000)
plt.hist(data,bins=20,#指定直方图的条形数位20个
         edgecolor='k',#指定直方图的边界色
         label='直方图')#为直方图呈现标签
# 去除图形顶部边界和右边界的刻度
plt.tick_params(top='off', right='off')
# 显示图例
plt.legend()

plt.show()