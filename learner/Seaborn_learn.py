#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/18 0018 上午 10:27
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: Seaborn_learn.py

#@Software: PyCharm
import matplotlib
import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

def sinplot(flip=1):
    x=np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(x,np.sin(x+i*.5)*(7-i)*flip)

""""
sns五种主题风格
darkgrid
whitegrid
dark
white
ticks
"""
# sinplot()
# sns.set_style("whitegrid")
# sns.despine(offset=10)#离轴线距离
# plt.show()
# sns.palplot(sns.color_palette("hls",100))
"""
palettle是控制颜色额
l是表示亮度
s表示饱和度
"""
# data=np.random.normal(size=(20,8))+np.arange(8)/2
# sns.boxplot(data=data,palette=sns.palplot(sns.color_palette("hls",100)))
# plt.show()
# sns.palplot(sns.color_palette("Paired",8))#颜色对
# sns.palplot(sns.color_palette("BuGn"))#颜色由浅到深
# sns.palplot(sns.color_palette("cubehelix",8))#色调线性变化
"""
画直方图
"""
# x=np.random.normal(size=100)
# sns.distplot(x,kde=False,fit=stats.gamma)
"""散点图"""
# mean,cov=[0,1],[(1,5),(5,1)]
# x,y=np.random.multivariate_normal(mean,cov,1000).T
# with sns.axes_style("darkgrid"):
#     sns.jointplot(x=x,y=y,kind="hex",color="k")
# plt.show()
iris=sns.load_dataset("iris")
sns.pairplot(iris)#统计特征的显示，所有的特征
plt.show()
