#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/5/14 0014 下午 2:51
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: 2-2.py

#@Software: PyCharm


"""重载运算符的方法（实现对应的方法）"""
import math


class Point:

    # 只要实现此方法即可载+法操作(对象加对象)

    a = 1.0
    b = 1.0
    def __add__(self,other):
        if (math.sqrt(other.a*other.a+other.b*other.b)>math.sqrt(self.a*self.a+self.b*self.b)):
            return ">"
        else:
            return  "<"

class PointTest(Point):

    def __init__(self,other):
        other.a=1.1
        other.b=1.1
        print(self+other)
PointTest(Point)
