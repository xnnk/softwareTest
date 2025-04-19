import requests
import pytest
import json
import allure
import os

class TestAPI:
    """接口自动化测试示例"""
    
    # 测试数据，实际项目中可从配置文件读取
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    @allure.feature("GET请求测试")
    @allure.story("获取单个用户")
    @pytest.mark.parametrize("user_id,expected_status", [(1, 200), (999, 404)])
    def test_get_user(self, user_id, expected_status):
        """测试GET请求获取用户信息"""
        with allure.step(f"发送GET请求获取用户ID: {user_id}"):
            response = requests.get(f"{self.BASE_URL}/users/{user_id}")
        
        with allure.step("验证响应状态码"):
            assert response.status_code == expected_status
            
        if expected_status == 200:
            with allure.step("验证响应JSON数据"):
                user_data = response.json()
                assert "id" in user_data
                assert user_data["id"] == user_id
                assert "name" in user_data
                assert "email" in user_data
                
                # 添加响应数据到报告中
                allure.attach(
                    json.dumps(user_data, indent=4), 
                    name="用户数据",
                    attachment_type=allure.attachment_type.JSON
                )
    
    @allure.feature("POST请求测试")
    @allure.story("创建新资源")
    def test_create_post(self):
        """测试POST请求创建帖子"""
        new_post = {
            "title": "测试帖子标题",
            "body": "测试帖子内容",
            "userId": 1
        }
        
        with allure.step("发送POST请求创建帖子"):
            response = requests.post(f"{self.BASE_URL}/posts", json=new_post)
            
        with allure.step("验证响应状态码"):
            assert response.status_code == 201
            
        with allure.step("验证响应数据"):
            post_data = response.json()
            assert "id" in post_data  # 验证返回的数据包含ID字段
            assert post_data["title"] == new_post["title"]
            assert post_data["body"] == new_post["body"]
            
            allure.attach(
                json.dumps(post_data, indent=4),
                name="创建的帖子",
                attachment_type=allure.attachment_type.JSON
            )
    
    @allure.feature("PUT请求测试")
    @allure.story("更新资源")
    def test_update_post(self):
        """测试PUT请求更新帖子"""
        post_id = 1
        updated_data = {
            "title": "更新后的标题",
            "body": "更新后的内容",
            "userId": 1
        }
        
        with allure.step(f"发送PUT请求更新帖子ID: {post_id}"):
            response = requests.put(f"{self.BASE_URL}/posts/{post_id}", json=updated_data)
            
        with allure.step("验证响应状态码"):
            assert response.status_code == 200
            
        with allure.step("验证响应数据"):
            resp_data = response.json()
            assert resp_data["title"] == updated_data["title"]
            assert resp_data["body"] == updated_data["body"]
    
    @allure.feature("DELETE请求测试")
    @allure.story("删除资源")
    def test_delete_post(self):
        """测试DELETE请求删除帖子"""
        post_id = 1
        
        with allure.step(f"发送DELETE请求删除帖子ID: {post_id}"):
            response = requests.delete(f"{self.BASE_URL}/posts/{post_id}")
            
        with allure.step("验证响应状态码"):
            assert response.status_code == 200
            
        with allure.step("验证资源已被删除"):
            # 尝试再次获取该资源，应该返回404
            verify_response = requests.get(f"{self.BASE_URL}/posts/{post_id}")
            # 注意：jsonplaceholder API是模拟API，实际上它不会真正删除资源
            # 如果是真实API，应该断言verify_response.status_code == 404
            assert verify_response.status_code == 200  # jsonplaceholder特殊情况
            
    @allure.feature("复杂请求测试")
    @allure.story("查询参数和请求头测试")
    def test_request_with_params_and_headers(self):
        """测试带查询参数和自定义请求头的请求"""
        # 查询参数
        params = {
            "userId": 1,
            "_limit": 3
        }
        
        # 自定义请求头
        headers = {
            "Content-Type": "application/json",
            "X-Custom-Header": "test-value"
        }
        
        with allure.step("发送带参数和自定义头的GET请求"):
            response = requests.get(
                f"{self.BASE_URL}/posts", 
                params=params,
                headers=headers
            )
            
        with allure.step("验证响应状态码"):
            assert response.status_code == 200
            
        with allure.step("验证响应数据"):
            posts = response.json()
            assert isinstance(posts, list)
            assert len(posts) <= 3  # 验证_limit参数生效
            
            # 验证所有返回的帖子都属于userId=1
            for post in posts:
                assert post["userId"] == 1
                
            allure.attach(
                json.dumps(posts, indent=4),
                name="查询结果",
                attachment_type=allure.attachment_type.JSON
            )

# 运行pytest的命令
# pytest -v requests_pytest_example.py --alluredir=./allure-results
# allure serve ./allure-results
