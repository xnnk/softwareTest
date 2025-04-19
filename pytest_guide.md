# Pytest 测试框架入门指南

## 基础用法

### 1. 安装pytest

```bash
pip install pytest pytest-html pytest-xdist
```

### 2. 测试函数示例

```python
# test_sample.py
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 2 == 3
```

### 3. 运行测试

```bash
# 运行当前目录下所有测试
pytest

# 运行特定测试文件
pytest test_sample.py

# 生成HTML报告
pytest --html=report.html

# 并行运行测试
pytest -xvs -n 4
```

## unittest 基础

```python
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        # 每个测试用例执行前的准备工作
        self.test_str = "Hello World"
    
    def test_upper(self):
        self.assertEqual(self.test_str.upper(), "HELLO WORLD")
    
    def test_split(self):
        self.assertEqual(self.test_str.split(), ["Hello", "World"])
    
    def tearDown(self):
        # 每个测试用例执行后的清理工作
        pass

if __name__ == '__main__':
    unittest.main()
```

## Pytest 高级特性

### 1. Fixtures - 依赖管理

```python
import pytest

@pytest.fixture
def browser():
    """提供一个浏览器实例"""
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    # 测试完成后关闭浏览器
    driver.quit()

def test_baidu_search(browser):
    """使用browser fixture进行测试"""
    browser.get("https://www.baidu.com")
    search_input = browser.find_element_by_id("kw")
    search_input.send_keys("Pytest")
    search_input.submit()
    assert "Pytest" in browser.title
```

### 2. 参数化测试

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 54)
])
def test_calculations(input, expected):
    # 将输入字符串作为Python表达式执行
    assert eval(input) == expected
```

### 3. 跳过测试和预期失败

```python
import pytest
import sys

@pytest.mark.skip(reason="功能尚未实现")
def test_unfinished_feature():
    pass

@pytest.mark.skipif(sys.version_info < (3, 8), reason="需要Python 3.8以上版本")
def test_new_feature():
    pass

@pytest.mark.xfail(reason="已知问题，等待修复")
def test_known_issue():
    assert False
```

### 4. 使用pytest-html生成报告

```bash
pytest --html=report.html --self-contained-html
```

### 5. 自定义Fixtures作用域

```python
import pytest

@pytest.fixture(scope="session")
def database_connection():
    """整个测试会话期间使用同一个数据库连接"""
    # 创建连接
    db = connect_to_database()
    yield db
    # 关闭连接
    db.close()

@pytest.fixture(scope="function")
def clean_database(database_connection):
    """每个测试函数前重置数据库状态"""
    database_connection.reset()
    return database_connection
```

### 6. 使用conftest.py共享fixtures

在测试目录中创建conftest.py文件，可以在多个测试模块中共享fixture:

```python
# conftest.py
import pytest

@pytest.fixture(scope="session")
def api_client():
    from api_client import ApiClient
    client = ApiClient(base_url="https://api.example.com")
    client.login("test_user", "password")
    yield client
    client.logout()
```
