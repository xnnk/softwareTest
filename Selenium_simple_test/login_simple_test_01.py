from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    # username_input = browser.find_element(By.CSS_SELECTOR, "#username")
    # password_input = browser.find_element(By.XPATH, "//input[@name='password']")

    username = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='用户名']"))
    )
    password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='password']"))
    )

    # 执行操作
    username.clear()
    username.send_keys("20230001")
    password.clear()
    password.send_keys("SecureP@ssw0rd")

    # 点击前确认按钮可点击
    submit = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='登录']]"))
    )
    submit.click()

    # 验证登录成功
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='web-title']"))
    )
    assert "后台管理系统" in browser.title

# 同样的定位方式测试错误情况...
# def test_failed_login(browser):