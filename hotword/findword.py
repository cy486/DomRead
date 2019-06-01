#-*- encoding:utf-8 -*-
from __future__ import print_function

import sys

import pymysql
from textrank4zh import TextRank4Keyword, TextRank4Sentence

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="hot", charset="utf8")
cursor = conn.cursor()


sql = "select id, word, content from hotword"
cursor.execute(sql)


for row in cursor.fetchall():

    print("key %s" % row[1])
    # 对标题和内容切词
    tr4w = TextRank4Keyword()
    text=row[1] + ' ' + row[2]
    tr4w.analyze(text=text, lower=True, window=2)
    seg_list = row[1] + ' ' + row[2]
    line = ""
    for item in tr4w.get_keywords(20, word_min_len=1):
        line = line + " " + item.word
    line = line.replace('\'', ' ')

    sql = "update hotword set keyword='%s' where id=%d" % (line, row[0])
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        sys.exit(-1)
# 关闭数据库连接
conn.close()