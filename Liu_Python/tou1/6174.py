#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/30 0030 下午 2:08
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: 6174.py

#@Software: PyCharm
"""
（六）、验证6174猜想
【题目描述】
1955年，卡普耶卡(D.R.Kaprekar)对4位数字进行了研究，发现一个规律：对任意各位数字不相同的4位数，
使用各位数字能组成的最大数减去能组成的最小数，对得到的差重复这个操作，最终会得到6174这个数字，
并且这个操作最多不会超过7次。请编写程序验证这个猜想。
"""
def Min_Number(a):
    a=str(a)
    arr=[]
    for i in range(0,4):
     arr.append(a[i])
    arr.sort()
    return int(''.join(arr))
def Max_Number(a):
    a=str(a)
    arr = []
    for i in range(0, 4):
        arr.append(a[i])
    arr.sort(reverse=True)
    return int(''.join(arr))
a=input()
while (int(a)!=6174):
    a=Max_Number(a)-Min_Number(a)
    print(a,end=" ")
