# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  02注册服务.py
@Time    :  2022/7/23 14:35
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
import zdppy_requests

headers = {
    "contentType": "application/json"
}

url = "http://127.0.0.1:8500/v1/agent/service/register"
address = "127.0.0.1"
port = 8500
name = "user-service"
print(f"http://{address}:{port}/health")
rsp = zdppy_requests.put(url, headers=headers, json={
    "Name": name,
    "ID": "user-service-id",
    "Tags": ["mxshop", "bobby", "imooc", "web"],
    "Address": address,
    "Port": port,
    "Check": {
        "GRPC": f"{address}:{port}",
        "GRPCUseTLS": False,
        "Timeout": "5s",
        "Interval": "5s",
        "DeregisterCriticalServiceAfter": "15s"
    }
})
if rsp.status_code == 200:
    print("注册成功")
else:
    print(f"注册失败：{rsp.status_code}")
