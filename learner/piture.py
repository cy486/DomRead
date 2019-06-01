#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/4/17 0017 下午 5:55
# @Author  :喜欢二福的沧月君（necydcy@gmail.com）
# @FileName: piture.py

# @Software: PyCharm

import pandas as pd
import matplotlib.pyplot as plt
from numpy.ma import arange
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
# unrate=pd.read_csv("unrate.csv")
# unrate['DATE']=pd.to_datetime(unrate["DATE"])
# print(unrate.head(3))

# first_twelve=unrate[0:12]

"""
一个折线图折线图
plt.plot(first_twelve['DATE'],first_twelve['VALUE'])
plt.xticks(rotation=45)
plt.xlabel('Month')
plt.ylabel('Unemploymnet Rate')
plt.title('Monthly Unemployment Trends,1948')
plt.show()

fig=plt.figure()
ax1=fig.add_subplot(4,3,1)
ax2=fig.add_subplot(4,3,2)
ax3=fig.add_subplot(4,3,6)

unrate['MONTH']=unrate['DATE'].dt.month
fig=plt.figure(figsize=(6,3))
plt.plot(unrate[0:12]['MONTH'],unrate[0:12]['VALUE'],c='red')
plt.plot(unrate[12:24]['MONTH'],unrate[12:24]['VALUE'],c='blue')
plt.legend(loc='best')

"""
"""
柱状图
"""
reviews = pd.read_csv("fandango_scores.csv")
cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]
# print(norm_reviews)
"""
bar_heights = norm_reviews.ix[0, cols].values
bar_positions = arange(5) + 0.75
tick_positions=range(1,6)
fig,ax=plt.subplots()
ax.barh(bar_positions,bar_heights,0.3)
ax.set_yticks(tick_positions)
ax.set_yticklabels(cols)
ax.set_ylabel('Rating Source')
ax.set_xlabel('Average Rating')
ax.set_title('Average User Rating For Avengers:Age of Ultron (2015)')

"""
fig,ax=plt.subplots()
ax.scatter(norm_reviews['Fandango_Ratingvalue'],norm_reviews['RT_user_norm'])
plt.show()