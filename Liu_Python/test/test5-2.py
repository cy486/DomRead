#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/5/5 0005 上午 9:13
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: test5-2.py

#@Software: PyCharm
import math


def primeSum(x,y):
    print(x)
    print(y)
    MAX_INT=y
    MIN_INT=x
    marks_bool = [True] * (MAX_INT + 1)
    for i in range(2,int(math.sqrt(MAX_INT)) + 1):
        j = i
        k = j
        while j * k <= MAX_INT:
            marks_bool[j * k] = False
            k += 1
    sum=0
    for i in range(2,MAX_INT + 1):
        if marks_bool[i] is True:
            if(i>=MIN_INT):
                sum+=i
    return sum
x,y =map(int, input().split())
print(primeSum(x,y))