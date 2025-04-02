import pytest
from pages.login_page import LoginPage


class TestLogin:
    @pytest.mark.parametrize("username,password,expected", [
        ("20230001", "SecureP@ssw0rd", "vue-manage-system后台管理系统"),
        ("wrong_user", "wrong_pass", "vue-manage-system后台管理系统")
    ])
    def test_login_scenarios(self, browser, username, password, expected):
        # 初始化页面对象
        login_page = LoginPage(browser).load()

        # 链式调用操作
        result = login_page.enter_credentials(username, password) \
            .submit() \
            .get_error_message()

        # 断言验证
        if "错误" in expected:
            assert expected in result
        else:
            assert expected in browser.title