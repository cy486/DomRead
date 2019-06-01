#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/24 0024 下午 10:06
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: Climbing_ladder.py

#@Software: PyCharm

"""
（八）、爬楼梯
【题目描述】
 假设一段楼梯共n(n>1)个台阶，小朋友一步最多能上3个台阶，那么小朋友上这段楼梯一共有多少种方法。
"""
def climb(num):
    if num==1:
        return 1
    if num==2:
       return 2
    if num==3:
        return 4
    else:
        sum=climb(num-1)+climb(num-2)+climb(num-3)
    return sum
print(climb(int(input())))
