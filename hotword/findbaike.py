#-*- encoding:utf-8 -*-
from __future__ import print_function

import requests

from bs4 import BeautifulSoup

import sys

import pymysql
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="hot", charset="utf8")
cursor = conn.cursor()

 # 找到全部文章的标题和内容
sql = "select id, word from hotword"
cursor.execute(sql)

for row in cursor.fetchall():

    url = "https://baike.baidu.com/item/" + row[1]
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.content, 'html.parser')
    summary_node = soup.find('div', attrs={"class": "lemma-summary", "label-module": "lemmaSummary"})
    try:
      a = summary_node.get_text()
    except AttributeError:
       a="无此词条"
    # 把切词按空格分隔并去特殊字符后重新写到数据库的segment字段里
    sql = "update hotword set baike='%s' where id=%d" % (a, row[0])
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
        sys.exit(-1)
