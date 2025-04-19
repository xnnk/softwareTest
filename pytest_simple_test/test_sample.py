import pytest

# 基本测试函数
def test_addition():
    """简单的加法测试"""
    assert 1 + 1 == 2

def test_subtraction():
    """简单的减法测试"""
    assert 5 - 3 == 2
    
# 使用参数化测试
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (10, -2, 8),
    (0, 0, 0)
])
def test_addition_parametrized(a, b, expected):
    """参数化的加法测试"""
    assert a + b == expected

# 使用fixture
@pytest.fixture
def test_data():
    """提供测试数据的fixture"""
    return {
        "user": "testuser",
        "password": "password123",
        "role": "admin"
    }

def test_user_role(test_data):
    """测试用户角色是否正确"""
    assert test_data["role"] == "admin"
    
def test_user_credentials(test_data):
    """测试用户凭据是否正确"""
    assert test_data["user"] == "testuser"
    assert len(test_data["password"]) >= 8
