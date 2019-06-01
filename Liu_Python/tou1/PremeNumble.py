#!/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time    :2019/4/23 0023 下午 10:03
# @Author  :喜欢二福的沧月君（necydcy@gmail.com）
# @FileName: PremeNumble.py

# @Software: PyCharm
import numpy
"""
（十）、筛法求素数
【题目描述】
用户输入整数n和m（1<n<m<1000），应用筛法求[n,m]范围内的所有素数。
"""
import math
num = [int(n) for n in input('').split()]
MAX_INT=num[1]
MIN_INT=num[0]
marks_bool = [True] * (MAX_INT + 1)
for i in range(2,int(math.sqrt(MAX_INT)) + 1):
    j = i
    k = j
    while j * k <= MAX_INT:
        marks_bool[j * k] = False
        k += 1
sum_int = 0
l=[]
for i in range(2,MAX_INT + 1):
    if marks_bool[i] is True:
        if(i>=MIN_INT):
            l.append(i)
print(numpy.array(l).reshape(-1,5))

