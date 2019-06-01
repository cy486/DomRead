#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/17 0017 下午 12:57
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: __init__.py.py

#@Software: PyCharm


import pandas

train_info= pandas.read_csv("E:/train_set_1.csv")
# print(type(train_info))
# print(train_info.dtypes)
# print(help(pandas.read_csv))
# print(train_info.head(3))
# print(train_info.tail(4))
# print(train_info.columns)
# print(train_info.shape)
# print(train_info.loc[0])
# print(train_info.loc[3:6])
# print(train_info["id"])
train_info.sort_values("class",inplace=True,ascending=False)
print(train_info["class"])