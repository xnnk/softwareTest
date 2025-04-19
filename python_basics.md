# Python语法快速入门

## 1. 变量与数据类型

```python
# 变量定义
name = "测试用例1"  # 字符串
age = 25  # 整数
price = 99.9  # 浮点数
is_valid = True  # 布尔值

# 列表
test_cases = ["登录测试", "搜索测试", "支付测试"]
# 字典
test_data = {"user": "admin", "password": "123456"}
```

## 2. 条件语句

```python
# if-elif-else 结构
status_code = 200

if status_code == 200:
    print("请求成功")
elif status_code == 404:
    print("资源未找到")
else:
    print(f"其他错误: {status_code}")
```

## 3. 循环

```python
# for循环
test_cases = ["登录", "搜索", "支付"]
for case in test_cases:
    print(f"执行测试: {case}")

# while循环
attempt = 0
while attempt < 3:
    print(f"尝试第 {attempt+1} 次请求")
    attempt += 1
```

## 4. 函数

```python
# 基本函数定义
def validate_response(status_code, expected_code=200):
    """验证响应状态码"""
    return status_code == expected_code

# 带返回值的函数
def get_test_data(test_name):
    data = {
        "login": {"username": "test", "password": "123456"},
        "search": {"keyword": "自动化测试"}
    }
    return data.get(test_name, {})
```

## 5. 文件操作

### CSV操作

```python
import csv

# 读取CSV
with open('test_data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 写入CSV
test_results = [
    ['测试ID', '测试名称', '结果'],
    ['001', '登录测试', '通过'],
    ['002', '搜索测试', '失败']
]

with open('results.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(test_results)
```

### Excel操作

```python
from openpyxl import Workbook, load_workbook

# 读取Excel
wb = load_workbook('test_data.xlsx')
sheet = wb.active
for row in sheet.iter_rows(values_only=True):
    print(row)

# 写入Excel
wb = Workbook()
sheet = wb.active
sheet.title = "测试结果"
sheet['A1'] = '测试ID'
sheet['B1'] = '测试名称'
sheet['C1'] = '结果'
wb.save('test_results.xlsx')
```

### JSON操作

```python
import json

# 读取JSON
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
    base_url = config['base_url']

# 写入JSON
test_result = {
    "total": 10,
    "passed": 8,
    "failed": 2,
    "details": [
        {"id": "TC001", "status": "pass"},
        {"id": "TC002", "status": "fail"}
    ]
}

with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(test_result, f, ensure_ascii=False, indent=4)
```
