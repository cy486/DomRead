#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/30 0030 下午 3:37
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: LRU.py

#@Software: PyCharm
"""
所谓LRU算法，是指在发生缺页并且没有空闲主存块时，把最近最少使用的页面换出主存块，腾出地方来调入新页面。
问题描述：一进程获得n个主存块的使用权，对于给定的进程访问页面次序，问当采用LRU算法时，输出发生的缺页次数。

"""
def LRU(pages, maxNum,n):

    temp = []
    times = 0

    for page in lst:
        num = len(temp)
        if num < n:
            times += 1
            temp.append(page)
        elif num == n:                #要访问的新页面已在主存块中
            if page in temp:          #处理“主存块”，把最新访问的页面交换到列表尾部
                pos = temp.index(page)
                temp = temp[:pos] + temp[pos+1:] + [page]
            else:                     #把最早访问的页面踢掉，调入新页面
                temp.pop(0)
                temp.append(page)
                times += 1

    return times
n=int(input())
lst=tuple(input().split(" "))
print(LRU(lst, 3,n))