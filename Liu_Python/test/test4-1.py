#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/5/5 0005 上午 8:50
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: test4-1.py

#@Software: PyCharm
money=input()
money_f=money[0]
money_t=money[1:]
if(money_f=='R'):
    money_p=float(money_t)/6
    money_f='$'
else:
    money_p=float(money_t)*6
    money_f = 'R'
print(money_f+"%.2f"%money_p)