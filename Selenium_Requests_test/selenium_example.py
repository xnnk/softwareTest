from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
import pandas as pd

class WebAutomationDemo:
    def __init__(self, browser='chrome'):
        """初始化浏览器驱动"""
        if browser.lower() == 'chrome':
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser.lower() == 'firefox':
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError("不支持的浏览器类型，请使用 'chrome' 或 'firefox'")
        
        # 设置隐式等待
        self.driver.implicitly_wait(10)
        # 最大化窗口
        self.driver.maximize_window()
    
    def login_demo(self, url="https://the-internet.herokuapp.com/login"):
        """登录功能示例"""
        try:
            self.driver.get(url)
            
            # 使用不同的定位方法查找元素
            # 1. 使用ID定位
            username = self.driver.find_element(By.ID, "username")
            username.send_keys("tomsmith")
            
            # 2. 使用NAME定位
            password = self.driver.find_element(By.NAME, "password")
            password.send_keys("SuperSecretPassword!")
            
            # 3. 使用CSS选择器定位
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button.radius")
            login_button.click()
            
            # 4. 使用显式等待确认登录成功
            wait = WebDriverWait(self.driver, 10)
            success_message = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "flash.success"))
            )
            
            return "登录成功" in success_message.text
        
        except Exception as e:
            print(f"登录失败，错误信息: {str(e)}")
            return False
    
    def form_submission_demo(self, url="https://the-internet.herokuapp.com/login"):
        """表单提交示例"""
        try:
            self.driver.get(url)
            
            # 使用XPath定位
            username = self.driver.find_element(By.XPATH, "//input[@id='username']")
            password = self.driver.find_element(By.XPATH, "//input[@id='password']")
            
            username.send_keys("tomsmith")
            password.send_keys("SuperSecretPassword!")
            
            # 使用显式等待等待按钮可点击
            wait = WebDriverWait(self.driver, 10)
            login_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )
            login_button.click()
            
            # 验证表单提交结果
            try:
                wait.until(EC.url_contains("/secure"))
                return True
            except TimeoutException:
                return False
                
        except Exception as e:
            print(f"表单提交失败，错误信息: {str(e)}")
            return False
    
    def data_scraping_demo(self, url="https://the-internet.herokuapp.com/tables"):
        """数据爬取示例"""
        try:
            self.driver.get(url)
            
            # 等待表格加载完成
            wait = WebDriverWait(self.driver, 10)
            table = wait.until(
                EC.presence_of_element_located((By.ID, "table1"))
            )
            
            # 获取表头
            headers = []
            for header in table.find_elements(By.TAG_NAME, "th"):
                headers.append(header.text)
            
            # 获取表格数据
            data = []
            for row in table.find_elements(By.TAG_NAME, "tr")[1:]:  # 跳过表头行
                row_data = []
                for cell in row.find_elements(By.TAG_NAME, "td"):
                    row_data.append(cell.text)
                if row_data:
                    data.append(row_data)
            
            # 使用pandas创建DataFrame
            df = pd.DataFrame(data, columns=headers)
            print(df.head())
            
            # 可以保存为CSV文件
            # df.to_csv("scraped_data.csv", index=False)
            
            return df
        
        except Exception as e:
            print(f"数据爬取失败，错误信息: {str(e)}")
            return None
    
    def close(self):
        """关闭浏览器"""
        if self.driver:
            self.driver.quit()

# 使用示例
if __name__ == "__main__":
    # Chrome浏览器测试
    chrome_test = WebAutomationDemo(browser="chrome")
    print("Chrome登录测试结果:", chrome_test.login_demo())
    chrome_test.close()
    
    # Firefox浏览器测试
    try:
        firefox_test = WebAutomationDemo(browser="firefox")
        print("Firefox表单提交测试结果:", firefox_test.form_submission_demo())
        firefox_test.data_scraping_demo()
        firefox_test.close()
    except Exception as e:
        print(f"Firefox测试失败: {e}")
