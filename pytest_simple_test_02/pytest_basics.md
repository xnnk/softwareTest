# Pytest 重要用法

## 1. 安装 Pytest
使用 pip 安装 pytest：
```bash
pip install pytest
```

## 2. 基本测试
创建一个以 `test_` 开头的函数，使用 `assert` 语句进行断言：
```python
# test_sample.py
def test_addition():
    assert 1 + 1 == 2
```
运行测试：
```bash
pytest test_sample.py
```

## 3. 使用 `setup` 和 `teardown`
在测试前后运行初始化和清理代码：
```python
import pytest

@pytest.fixture
def setup_data():
    # 初始化数据
    return {"key": "value"}

def test_example(setup_data):
    assert setup_data["key"] == "value"
```

## 4. 参数化测试
使用 `@pytest.mark.parametrize` 进行参数化测试：
```python
import pytest

@pytest.mark.parametrize("input,expected", [
    (1 + 1, 2),
    (2 * 2, 4),
    (3 - 1, 2)
])
def test_math(input, expected):
    assert input == expected
```

## 5. 跳过测试
使用 `pytest.mark.skip` 跳过某些测试：
```python
import pytest

@pytest.mark.skip(reason="尚未实现")
def test_not_implemented():
    assert False
```

### 动态跳过测试
可以在运行时动态跳过测试，例如根据某些条件：
```python
import pytest
import sys

def test_skip_on_condition():
    if sys.platform == "win32":
        pytest.skip("此测试在 Windows 上被跳过")
    assert True
```

## 6. 捕获异常
使用 `pytest.raises` 验证是否抛出异常：
```python
import pytest

def test_raises_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

## 7. 测试类
将测试组织到类中：
```python
class TestExample:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2
```

## 8. 运行特定测试
运行特定测试文件或测试函数：
```bash
pytest test_sample.py::test_addition
```

## 9. 查看详细输出
使用 `-v` 查看详细的测试输出：
```bash
pytest -v
```

## 10. 生成测试报告
使用 `--html` 生成 HTML 格式的测试报告（需要安装插件 `pytest-html`）：
```bash
pip install pytest-html
pytest --html=report.html
```

## 11. 使用标记
为测试添加自定义标记：
```python
import pytest

@pytest.mark.slow
def test_slow_function():
    import time
    time.sleep(5)
    assert True
```
运行带有特定标记的测试：
```bash
pytest -m slow
```

### 条件标记
可以根据条件动态应用标记：
```python
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 8), reason="需要 Python 3.8 或更高版本")
def test_requires_python_38():
    assert True
```

## 12. 测试覆盖率
结合 `pytest-cov` 插件查看代码覆盖率：
```bash
pip install pytest-cov
pytest --cov=your_module
```

## 13. 调试失败的测试
使用 `--pdb` 在测试失败时进入调试模式：
```bash
pytest --pdb
```

## 14. 重试失败的测试
使用 `pytest-rerunfailures` 插件重试失败的测试：
```bash
pip install pytest-rerunfailures
pytest --reruns 3
```

## 15. 运行目录中的所有测试
运行当前目录及子目录中的所有测试：
```bash
pytest
```

## 16. 测试分组
使用自定义标记对测试进行分组：
```python
import pytest

@pytest.mark.database
def test_database_connection():
    assert True

@pytest.mark.api
def test_api_response():
    assert True
```
运行特定分组的测试：
```bash
pytest -m database
```

## 17. 使用插件扩展
Pytest 提供了丰富的插件支持，例如 `pytest-xdist` 用于并行运行测试：
```bash
pip install pytest-xdist
pytest -n 4  # 使用 4 个 CPU 核心并行运行测试
```

## 18. 自定义命令行参数
可以通过 `pytest_addoption` 添加自定义命令行参数：
```python
# conftest.py
def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="运行环境")

# 测试文件
import pytest

@pytest.fixture
def env(request):
    return request.config.getoption("--env")

def test_environment(env):
    assert env in ["dev", "staging", "prod"]
```
运行测试时传递参数：
```bash
pytest --env=staging
```
`