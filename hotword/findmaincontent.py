#-*- encoding:utf-8 -*-
from __future__ import print_function

import codecs
import sys

import jieba
import pymysql
from textrank4zh import TextRank4Keyword, TextRank4Sentence

conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="hot", charset="utf8")
cursor = conn.cursor()

if True == all:
    # 找到全部文章的标题和内容
    sql = "select id, word, content from hotword"
else:
    # 找到尚未切词的文章的标题和内容
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
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='all_filters')
    for item in tr4s.get_key_sentences(num=3):
        line =item.sentence
    # 把切词按空格分隔并去特殊字符后重新写到数据库的segment字段里
    sql = "update hotword set maincontent='%s' where id=%d" % (line, row[0])
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        sys.exit(-1)
