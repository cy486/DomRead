#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/17 0017 下午 5:11
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: train.py

#@Software: PyCharm
import numpy as np
import pandas as pd

titanic_survival= pd.read_csv("titanic_train.csv")
#print(titanic_survival.head)

""" 
age中有缺失值
求平均值

age=titanic_survival["Age"]
#print(age.loc[0:10])
age_is_null=pd.isnull(age)
#print(age_is_null)
age_null_true=age[age_is_null]
# print(age_null_true)
age_null_count=len(age_null_true)
# print(age_null_count)
good_ages=titanic_survival["Age"][age_is_null == False]
# print(good_ages)
correct_mean_age=sum(good_ages)/len(good_ages)
# print(correct_mean_age)
"""
"""
求每个船舱的平均存活人数

passenger_survival =titanic_survival.pivot_table(index="Pclass",values="Survived",aggfunc=np.mean)#默认是求均值
# print(passenger_survival)
port_stats =titanic_survival.pivot_table(index="Embarked",values=["Fare","Survived"],aggfunc=np.sum)
# print(port_stats)
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["Age","Sex"])
print(new_titanic_survival)
"""
"""

"""
