# zdppy_requests
python的请求工具库

项目地址：https://github.com/zhangdapeng520/zdppy_requests

## 版本历史
- 版本0.1.0  2022年2月22日 基本增删改查

## 功能清单
- add(self, table: str, data: Dict, status_code: int = 200)：添加数据
- find_by_page(self, table: str, offset: int = 0, size: int = 100, status_code: int = 200)：根据分页查询数据
- find_by_id(self, table: str, id: int = 1, status_code: int = 200)：根据ID查询数据
- delete_by_id(self, table: str, id: int = 1, status_code: int = 200)：根据ID删除数据
- update_by_id(self, table: str, id: int = 1, data: Dict = None, status_code: int = 200)：根据ID更新数据
