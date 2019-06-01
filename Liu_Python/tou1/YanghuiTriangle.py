#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/24 0024 下午 9:36
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: YanghuiTriangle.py

#@Software: PyCharm

"""
（九）、杨辉三角形
【题目描述】
输出n（0<n）行杨辉三角形，n由用户输入。

"""
def YangHui (num = 10):
    LL = [[1]]
    for i in range(1,num):
        LL.append([(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
    return LL
a=int(input())
for i in YangHui(a):
    for j in i:
        print("%5d"%j,end="")
    print()