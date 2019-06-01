#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/5/14 0014 下午 3:52
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: 2-2.py

#@Software: PyCharm
import abc

from math import pi


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def zc(self):
        pass

    @abc.abstractmethod
    def mz(self):
        pass

    @abc.abstractmethod
    def tz(self):
        pass
#点
class Point(Shape):
    """首先定义点类，应包含x，y坐标数据成员，坐标获取及设置方法、显示方法等"""
    x = 1
    y = 1
    def getPoint(self):
        return self.x,self.y
    def setPoint(self,other):
        self.x=other.x
        self.y=other.y
    def printPoint(self):
        print(self.x,self.y)

def Circle(Point):
    bj = 1.0
    def get(self):
        return self.bj
    def set(self,other):
        self.bj = other.bj
    def print(self):
        print(self.bj)
    def mj(self):
        print(int(pi*bj*bj))