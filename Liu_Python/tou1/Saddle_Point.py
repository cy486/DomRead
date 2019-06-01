#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/23 0023 下午 3:29
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: Saddle_Point.py

#@Software: PyCharm11 3 5 6 9 12 4 7 8 10 10 5 6 9 11 8 6 4 7 8 15 10 11 20 25
"""
（十一）、查找鞍点
【题目描述】
对于给定5X5的整数矩阵，设计算法查找出所有的鞍点的信息（包括鞍点的值和行、列坐标，坐标从1开始）。
提示：鞍点的特点：列上最小，行上最大。

"""
import numpy as np
num = [int(n) for n in input('').split()]
num = np.array(num,dtype=int)
num = num.reshape(5,5)
for i in range(0,5):
  for j in range(0,5):
     if (num[i][j] == min(num[:,j]) & num[i][j] == max(num[i,:])):
        print("[%s,%s,%s]"%(i+1,j+1,num[i][j]))





