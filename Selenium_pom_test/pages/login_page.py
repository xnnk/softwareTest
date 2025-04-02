from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # 元素定位器（定位策略集中管理）
    USERNAME_INPUT = (By.XPATH, "//input[@placeholder='用户名' and contains(@class,'el-input__inner')]")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.el-input__inner[type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'login-btn')]//span[text()='登录']/..")
    ERROR_MSG = (By.CLASS_NAME, "el-message__content")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def load(self):
        """页面加载"""
        self.driver.get("http://127.0.0.1:5173/#/login")
        return self

    def enter_credentials(self, username, password):
        """组合操作：输入用户名密码"""
        self.input_username(username)
        self.input_password(password)
        return self

    def input_username(self, text):
        """单独用户名输入操作"""
        elem = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        elem.clear()
        elem.send_keys(text)
        return self  # 支持链式调用

    def input_password(self, text):
        """单独密码输入操作"""
        elem = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        elem.clear()
        elem.send_keys(text)
        return self

    def submit(self):
        """提交登录"""
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()
        return self

    def get_error_message(self):
        """获取错误提示"""
        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MSG)
        ).text