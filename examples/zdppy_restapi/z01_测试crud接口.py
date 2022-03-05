#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/3/5 23:17
# @Author  : 张大鹏
# @Site    : 
# @File    : z01_测试crud接口.py
# @Software: PyCharm

from zdppy_requests import Requests

r = Requests(host="127.0.0.1", port=8889, root_path="", debug=True)

if __name__ == '__main__':
    # 处理查询
    data = {
        "id": 15,
    }
    r.log.info(r.put("school", data).status_code)
    r.log.info(r.put("school", data).json())
    data = {
        "ids": [15, 16, 17],
    }
    r.log.info(r.put("school", data).status_code)
    r.log.info(r.put("school", data).json())
    data = {
        "page": 1,
        "size": 10,
    }
    r.log.info(r.put("school", data).status_code)
    r.log.info(r.put("school", data).json())
    print("--------------------------------")

    # 处理新增
    data = {
        "columns": ["name"],
        "values": ["北京大学111"]
    }
    r.log.info(r.post("school", data).json())
    data = {
        "columns": ["name"],
        "values": [["北京大学111"], ["北京大学222"], ["北京大学333"]]
    }
    r.log.info(r.post("school", data).json())
    print("--------------------------------")

    # 处理修改
    data = {
        "id": 20,
        "columns": ["name"],
        "values": ["修改北京大学。。。"]
    }
    r.log.info(r.patch("school", data).json())
    r.log.info(r.put("school", data={"id": 20}).json())

    data = {
        "ids": [20, 21, 22],
        "columns": ["name"],
        "values": ["修改北京大学111。。。"]
    }
    r.log.info(r.patch("school", data).json())
    r.log.info(r.put("school", data={"ids": [20, 21, 22]}).json())
    print("--------------------------------")

    # 处理删除
    data = {
        "id": 15
    }
    r.log.info(r.delete("school", data).json())
    data = {
        "ids": [15, 16, 17]
    }
    r.log.info(r.delete("school", data).json())
    print("--------------------------------")
