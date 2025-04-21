# 2. 基本测试
def test_addition():
    assert 1 + 1 == 2

# 3. 使用 setup 和 teardown
import pytest

@pytest.fixture
def setup_data():
    # 初始化数据
    return {"key": "value"}

def test_example(setup_data):
    assert setup_data["key"] == "value"

# 4. 参数化测试
@pytest.mark.parametrize("input,expected", [
    (1 + 1, 2),
    (2 * 2, 4),
    (3 - 1, 2)
])
def test_math(input, expected):
    assert input == expected

# 5. 跳过测试
@pytest.mark.skip(reason="尚未实现")
def test_not_implemented():
    assert False

# 动态跳过测试
import sys

def test_skip_on_condition():
    if sys.platform == "win32":
        pytest.skip("此测试在 Windows 上被跳过")
    assert True

# 6. 捕获异常
def test_raises_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# 7. 测试类
class TestExample:
    def test_one(self):
        assert 1 == 1

    def test_two(self):
        assert 2 == 2

# 11. 使用标记
@pytest.mark.slow
def test_slow_function():
    import time
    time.sleep(1)  # 模拟耗时操作
    assert True

# 条件标记
@pytest.mark.skipif(sys.version_info < (3, 8), reason="需要 Python 3.8 或更高版本")
def test_requires_python_38():
    assert True

# 16. 测试分组
@pytest.mark.database
def test_database_connection():
    assert True

@pytest.mark.api
def test_api_response():
    assert True

# 18. 自定义命令行参数
@pytest.fixture
def env(request):
    return request.config.getoption("--env")

def test_environment(env):
    assert env in ["dev", "staging", "prod"]
