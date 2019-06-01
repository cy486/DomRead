#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/5/5 0005 上午 9:20
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: test5-1.py

#@Software: PyCharm
def fibonacci(i):
    if (i==0):
        shu=1
    elif(i==1):
        shu=1
    else:
        shu=fibonacci(i-1)+fibonacci(i-2)
    return shu
def PrintFN(m,n,i):
    print("fib(%d) = %d"%(i,fibonacci(6)))
    sum=0
    j=0
    while(fibonacci(j)<m):
        j+=1
    while(fibonacci(j)<n):
        sum+=1
        j+=1
    print(sum)
m,n,i=input().split()
n=int(n)
m=int(m)
i=int(i)
PrintFN(m,n,i)