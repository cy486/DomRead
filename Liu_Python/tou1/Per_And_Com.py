#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/23 0023 下午 2:12
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: Per_And_Com.py
#@Software: PyCharm
import itertools
"""
（四）、排列组合序列
【题目描述】
用户输入整数n（1<=n<=26）和整数m（m<=n），然后输入n个不同的字母，请编写程序输出在这n个字母中选择m个字母的所有排列序列和组合序列。
"""
e=input()
num=int(input())
arr = input().split(" ")
print(arr)
a = list(itertools.combinations(arr,num))
b = list(itertools.permutations(arr,num))
print("Permutation:" )
for i in b:
  for j in i:
      print(j,end=" ")
  print()
print("Combination:" )
for i in a:
  for j in i:
      print(j,end=" ")
  print()


