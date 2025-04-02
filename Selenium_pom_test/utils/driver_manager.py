from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    """创建可复用的浏览器实例"""
    options = Options()
    options.add_argument("--headless")  # 无头模式
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver