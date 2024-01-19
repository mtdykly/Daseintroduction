import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import seaborn as sns
plt.style.use('ggplot')
import matplotlib
import numpy as np
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False


plt.figure(figsize=(10,10))

GDP = [36102,38700,14083,25002]
city = ['北京市', '上海市', '天津市', '重庆市']
dict={'GDP':GDP,'city':city}
df=pd.DataFrame(dict)
df.to_csv('gdp.csv')

inf=pd.read_csv('gdp.csv')
inf[:2]

#创建画纸1
#折线图
ax1=plt.subplot(221)
print(inf.to_string())
sns.lineplot(x="city",y="GDP",data=inf,markers="o")

#选择画纸2
#散点图
ax2=plt.subplot(222)
sns.scatterplot(x="city",y="GDP",data=inf)

#选择画纸3
#简单垂直条形图
ax3=plt.subplot(223)
sns.barplot(x="city",y="GDP",data=inf)

#选择画纸4
#简单频数直方图
data=np.random.randn(1000)
sns.displot(data=data,bins=50)
plt.grid(linestyle='-')
sns.despine(ax=None, top=True, right=True, left=True,bottom=True)

plt.show()
