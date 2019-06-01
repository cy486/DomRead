#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/5/5 0005 上午 8:58
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: test4-2.py

#@Software: PyCharm
while True:
    grade=int(input())
    grade_A='E'
    if(grade>=90):
        grade_A='A'
    elif(grade>=80):
        grade_A='B'
    elif(grade>=70):
        grade_A='C'
    elif(grade>=60):
        grade_A='D'
    print(grade_A)