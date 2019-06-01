#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/4/17 0017 下午 1:15
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: cut.py

#@Software: PyCharm
# -*- coding: cp936 -*-
import os
import time


def mkSubFile(lines, head, srcName, sub):
    [des_filename, extname] = os.path.splitext(srcName)
    filename = des_filename + '_' + str(sub) + extname
    print('make file: %s' % filename)
    fout = open(filename, 'w')
    try:
        fout.writelines([head])
        fout.writelines(lines)
        return sub + 1
    finally:
        fout.close()


def splitByLineCount(filename, count):
    fin = open(filename, 'r')
    try:
        head = fin.readline()
        buf = []
        sub = 1
        for line in fin:
            buf.append(line)
            if len(buf) == count:
                sub = mkSubFile(buf, head, filename, sub)
                buf = []
        if len(buf) != 0:
            sub = mkSubFile(buf, head, filename, sub)
    finally:
        fin.close()


if __name__ == '__main__':
    begin = time.time()
    splitByLineCount('E:/Preliminary-finals.csv', 10000)
    end = time.time()
    print('time is %d seconds ' % (end - begin))
