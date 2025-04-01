from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_successful_login(browser):
    # 打开登录页面
    browser.get("http://127.0.0.1:5173/#/login")

    # 使用CSS选择器定位元素
    username_input = browser.find_element(By.CSS_SELECTOR, "#username")
    password_input = browser.find_element(By.XPATH, "//input[@name='password']")
    submit_button = browser.find_element(By.CLASS_NAME, "login-btn")

    # 执行操作
    username_input.clear()
    username_input.send_keys("20230001")
    password_input.send_keys("SecureP@ssw0rd")
    submit_button.click()

    # 验证登录成功
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "welcome-header"))
    )
    assert "Dashboard" in browser.title

# 同样的定位方式测试错误情况...
# def test_failed_login(browser):