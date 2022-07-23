# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  01发送请求.py
@Time    :  2022/7/23 14:17
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
import zdppy_requests

r = zdppy_requests.get('https://www.douban.com/')
print(r.status_code)
print(r.encoding)
print(r.text)
