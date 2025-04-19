# API自动化测试指南 (使用 requests 库)

## 1. 安装requests

```bash
pip install requests
```

## 2. 基本请求操作

```python
import requests

# GET请求
response = requests.get('https://api.example.com/users')
print(response.status_code)  # 状态码
print(response.json())  # 转换为JSON

# POST请求
data = {
    'username': 'test_user',
    'password': '123456'
}
response = requests.post('https://api.example.com/login', json=data)
print(response.text)  # 文本响应

# 请求头设置
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer token123'
}
response = requests.get('https://api.example.com/profile', headers=headers)
```

## 3. 基于requests的API测试框架

```python
import requests
import pytest

class TestUserApi:
    base_url = "https://api.example.com"
    
    @pytest.fixture
    def auth_token(self):
        """获取认证token"""
        response = requests.post(
            f"{self.base_url}/login",
            json={"username": "test", "password": "password"}
        )
        assert response.status_code == 200
        return response.json()["token"]
    
    def test_get_user_profile(self, auth_token):
        """测试获取用户信息"""
        headers = {"Authorization": f"Bearer {auth_token}"}
        response = requests.get(f"{self.base_url}/profile", headers=headers)
        
        # 验证状态码
        assert response.status_code == 200
        
        # 验证响应内容
        user_data = response.json()
        assert "id" in user_data
        assert "username" in user_data
        assert user_data["username"] == "test"
```

## 4. 高级技巧

### 异常处理

```python
def safe_request(url, method='GET', **kwargs):
    """处理请求异常的包装函数"""
    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()  # 抛出4XX/5XX状态码的异常
        return response
    except requests.exceptions.HTTPError as e:
        print(f"HTTP错误: {e}")
    except requests.exceptions.ConnectionError:
        print(f"连接错误，无法连接到 {url}")
    except requests.exceptions.Timeout:
        print("请求超时")
    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")
    return None
```

### 会话管理

```python
# 使用会话保持Cookie和连接
session = requests.Session()

# 登录
session.post(
    'https://api.example.com/login',
    json={'username': 'test', 'password': '123456'}
)

# 后续请求自动使用同一个会话(保持登录状态)
profile = session.get('https://api.example.com/profile')
orders = session.get('https://api.example.com/orders')
```

### 请求超时设置

```python
# 设置连接超时和读取超时(秒)
response = requests.get('https://api.example.com', timeout=(3, 10))
```

### 上传文件

```python
files = {'file': open('test_report.pdf', 'rb')}
response = requests.post('https://api.example.com/upload', files=files)
```

## 5. 与pytest结合的接口测试示例

```python
import pytest
import requests

class TestOrderApi:
    @pytest.fixture
    def api_client(self):
        class ApiClient:
            def __init__(self):
                self.base_url = "https://api.example.com"
                self.session = requests.Session()
                self._login()
            
            def _login(self):
                response = self.session.post(
                    f"{self.base_url}/login",
                    json={"username": "test", "password": "123456"}
                )
                assert response.status_code == 200
            
            def create_order(self, product_id, quantity):
                return self.session.post(
                    f"{self.base_url}/orders",
                    json={"product_id": product_id, "quantity": quantity}
                )
            
            def get_order(self, order_id):
                return self.session.get(f"{self.base_url}/orders/{order_id}")
                
        return ApiClient()
    
    def test_create_order(self, api_client):
        # 创建订单
        response = api_client.create_order("product123", 2)
        assert response.status_code == 201
        
        # 验证响应数据
        data = response.json()
        assert "order_id" in data
        assert data["status"] == "created"
        
        # 获取并验证订单
        order_id = data["order_id"]
        order_response = api_client.get_order(order_id)
        assert order_response.status_code == 200
        order_data = order_response.json()
        assert order_data["product_id"] == "product123"
        assert order_data["quantity"] == 2
```
