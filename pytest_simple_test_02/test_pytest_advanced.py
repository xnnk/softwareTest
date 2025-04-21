import pytest
import sys

# 1. 测试浮点数比较
def test_float_comparison():
    assert abs(0.1 + 0.2 - 0.3) < 1e-9

# 2. 测试字符串操作
@pytest.mark.parametrize("input,expected", [
    ("hello".upper(), "HELLO"),
    ("WORLD".lower(), "world"),
    ("pytest".capitalize(), "Pytest")
])
def test_string_operations(input, expected):
    assert input == expected

# 3. 测试列表操作
@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3] + [4, 5], [1, 2, 3, 4, 5]),
    ([1] * 3, [1, 1, 1]),
    (list(range(3)), [0, 1, 2])
])
def test_list_operations(input, expected):
    assert input == expected

# 4. 测试字典操作
def test_dict_operations():
    data = {"a": 1, "b": 2}
    data["c"] = 3
    assert data == {"a": 1, "b": 2, "c": 3}

# 5. 测试集合操作
def test_set_operations():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    assert set1 | set2 == {1, 2, 3, 4, 5}
    assert set1 & set2 == {3}

# 6. 测试异常信息
def test_exception_message():
    with pytest.raises(ValueError, match="invalid literal for int"):
        int("abc")

# 7. 测试文件操作
@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello, Pytest!")
    return file

def test_file_read(temp_file):
    assert temp_file.read_text() == "Hello, Pytest!"

# 8. 测试环境变量
@pytest.mark.skipif("MY_ENV_VAR" not in sys.environ, reason="需要设置环境变量 MY_ENV_VAR")
def test_environment_variable():
    assert sys.environ["MY_ENV_VAR"] == "expected_value"

# 9. 测试多线程
import threading

def test_multithreading():
    result = []

    def worker():
        result.append(1)

    threads = [threading.Thread(target=worker) for _ in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert len(result) == 5

# 10. 测试异步代码
import asyncio

@pytest.mark.asyncio
async def test_async_function():
    async def async_add(a, b):
        await asyncio.sleep(0.1)
        return a + b

    result = await async_add(1, 2)
    assert result == 3

# 11. 测试边界值
@pytest.mark.parametrize("input,expected", [
    (0, True),
    (1, True),
    (-1, False),
    (100, True),
    (101, False)
])
def test_boundary_values(input, expected):
    assert (0 <= input <= 100) == expected

# 12. 测试性能（简单计时）
import time

def test_performance():
    start_time = time.time()
    sum(range(1000000))
    end_time = time.time()
    assert end_time - start_time < 1  # 测试是否在 1 秒内完成
