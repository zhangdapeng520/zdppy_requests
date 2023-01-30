# zdppy_requests
基于requests二开的HTTP请求库，无任何第三方依赖，可独立使用，不受开源框架迭代的影响。


# 使用示例
## 安装
```bash
pip install zdppy_requests
```

## 获取网页源码
```python
import zdppy_requests as zr

response = zr.get("https://www.baidu.com/")
print(response.status_code)
print(response.text)

创建Mapping
import zdppy_requests as zr
from zdppy_requests.auth import HTTPBasicAuth

url = "http://localhost:9200"
body = {
  "mappings": {
    "properties": {
      "name": {
        "type": "text"
      },
      "price": {
        "type": "double"
      },
      "author": {
        "type": "text"
      },
      "pub_date": {
        "type": "date"
      }
    }
  }
}
index = "books"
auth = HTTPBasicAuth('elastic','zhangdapeng520')

response = zr.put(f"{url}/{index}", json=body, auth=auth)
print(response.status_code)
print(response.text)
```

## 查询Mapping
```python
import zdppy_requests as zr
from zdppy_requests.auth import HTTPBasicAuth

url = "http://localhost:9200"
index = "books/_mapping?pretty"
auth = HTTPBasicAuth('elastic','zhangdapeng520')
target = f"{url}/{index}"

response = zr.get(target, auth=auth)
print(response.status_code)
print(response.text)
```

## 删除Mapping
```python
import zdppy_requests as zr
from zdppy_requests.auth import HTTPBasicAuth

url = "http://localhost:9200"
index = "books"
auth = HTTPBasicAuth('elastic','zhangdapeng520')
target = f"{url}/{index}"

response = zr.delete(target, auth=auth)
print(response.status_code)
print(response.text)
```

## 根据ID新增数据
```python
import zdppy_requests as zr
from zdppy_requests.auth import HTTPBasicAuth

url = "http://localhost:9200"
index = "books/_doc"
did = "1"
auth = HTTPBasicAuth('elastic','zhangdapeng520')
target = f"{url}/{index}/{did}"
body = {
	"name": "《JavaScript全栈开发实战》",
	"author": "张大鹏",
	"price": 123,
	"pub_date": "2019-12-12"
}

response = zr.put(target, json=body, auth=auth)
print(response.status_code)
print(response.text)
```

## 根据ID查询图书
```python
import zdppy_requests as zr
from zdppy_requests.auth import HTTPBasicAuth

url = "http://localhost:9200"
index = "books/_doc"
did = "1"
auth = HTTPBasicAuth('elastic','zhangdapeng520')
target = f"{url}/{index}/{did}"

response = zr.get(target, auth=auth)
print(response.status_code)
print(response.text)
```

## 根据ID删除图书
```python
import zdppy_requests as zr
from zdppy_requests.auth import HTTPBasicAuth

url = "http://localhost:9200"
index = "books/_doc"
did = "1"
auth = HTTPBasicAuth('elastic','zhangdapeng520')
target = f"{url}/{index}/{did}"

response = zr.delete(target, auth=auth)
print(response.status_code)
print(response.text)
```


