#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/30 0030 下午 2:43
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: Monte_Carlo.py

#@Software: PyCharm
"""
（五）、蒙特·卡罗法计算圆周率
【题目描述】
蒙特·卡罗方法是一种通过概率来得到问题近似解的方法，在很多领域都有重要的应用，其中就包括圆周率近似值的计问题。假设有一块边长为2的正方形木板，上面画一个单位圆，然后随意往木板上扔飞镖，落点坐标(x,y)必然在木板上（更多的时候是落在单位圆内），如果扔的次数足够多，那么落在单位圆内的次数除以总次数再乘以4，这个数字会无限逼近圆周率的值。这就是蒙特·卡罗发明的用于计算圆周率近似值的方法。编写程序，模拟蒙特·卡罗计算圆周率近似值的方法，输入掷飞镖次数，然后输出圆周率近似值。
"""
import random

num=int(input())
ok=0
for i in range(1,num+1):
    x=random.uniform(-1,1)#到-1到1的随机数
    y=random.uniform(-1,1)
    if(x*x+y*y<=1):
        ok+=1
print(ok/num*4)