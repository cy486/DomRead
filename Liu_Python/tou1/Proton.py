#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/23 0023 下午 9:38
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: Proton.py

#@Software: PyCharm
"""
（十二）、正整数的因子展开式
【题目描述】
编写程序，输出一个给定正整数x（x>1）的质因子展开式。

"""
a=int(input())
b=str(a)
num=[]
i=1
while i <= a:
    if a%i == 0:
        a = a/i
        num.append(i)
        i = 1
    i+=1
b+='='+str(num[1])
for j in num[2:]:
    b+="*"+str(j)
print(b)