#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/23 0023 下午 2:12
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: Per_And_Com.py

#@Software: PyCharm
"""
（十三）、牛顿迭代法
【题目描述】
编写程序，使用牛顿迭代法求方程 在x附近的一个实根。

"""
from math import fabs

def solut(a,b,c,d,e):
    x1=e
    # 迭代:
    while True:
        x=x1
        f = ((a * x + b) * x + c) * x + d #原函数1.0 2.0 3.0 4.0 1.0
        f1 = (3 * a * x + 2 * b) * x + c #求导的函数
        x1 = x - f / f1
        if (fabs(x1 - x) <= 0.00000001):
            return x1
num = [float(n) for n in input('').split()]
print(("%0.2f")%(solut(num[0],num[1],num[2],num[3],num[4])))