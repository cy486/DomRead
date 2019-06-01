#!/usr/bin/env python
# _*_coding:utf-8 _*_
#@Time    :2019/5/28 0028 下午 4:54
#@Author  :喜欢二福的沧月君（necydcy@gmail.com）
#@FileName: one.py

#@Software:
# qcloudapi-sdk-python SDK工具包
# 安装


# 情感分析API调用
# Python 3.6
from QcloudApi.qcloudapi import QcloudApi

# 设置需要加载的模块
module = 'wenzhi'
# 接口名-情感分析
action = 'TextSentiment'
# 云API的公共参数-参数排序很重要(首字母排序)
config = {
    'method': 'GET',
    'Region': 'ap-guangzhou',
    'secretId': '替换成自己的',
    'secretKey': '替换成自己的',
    'SignatureMethod': 'HmacSHA1'
}
# 请求参数,支持json
# 数组'content':[1,2,3]
params = {'content': '是真的烦人', 'type': 4}

service = QcloudApi(module, config)
# 请求前修改参数(5个参数均可修改)
# service.setRegion('ap-shanghai')

# 生成请求的url,但不发起请求
print(service.generateUrl(action, params))
# 调用接口-发起请求
s = service.call(action, params)
print(s)

# 输出
