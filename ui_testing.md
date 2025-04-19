# UI自动化测试指南 (使用 Selenium)

## 1. 安装Selenium

```bash
pip install selenium webdriver-manager
```

## 2. 基本使用

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 自动下载并配置ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 打开网页
driver.get("https://www.baidu.com")

# 查找元素
search_input = driver.find_element(By.ID, "kw")

# 输入文字
search_input.send_keys("Selenium自动化测试")

# 点击提交按钮
search_input.submit()

# 等待加载
time.sleep(2)

# 验证结果
assert "Selenium自动化测试" in driver.title

# 关闭浏览器
driver.quit()
```

## 3. 元素定位方式

```python
# ID定位
element = driver.find_element(By.ID, "kw")

# 类名定位
elements = driver.find_elements(By.CLASS_NAME, "result")

# 标签名定位
links = driver.find_elements(By.TAG_NAME, "a")

# 链接文本定位
help_link = driver.find_element(By.LINK_TEXT, "帮助")

# 部分链接文本
link = driver.find_element(By.PARTIAL_LINK_TEXT, "帮助")

# XPath定位
button = driver.find_element(By.XPATH, "//div[@id='content']/button")

# CSS选择器定位
element = driver.find_element(By.CSS_SELECTOR, "#content button.primary")
```

## 4. 常用交互操作

```python
# 点击
button = driver.find_element(By.ID, "submit")
button.click()

# 输入文本
input_field = driver.find_element(By.NAME, "username")
input_field.clear()  # 清空字段
input_field.send_keys("测试用户")

# 键盘操作
input_field.send_keys(Keys.RETURN)  # 回车键
input_field.send_keys(Keys.CONTROL + 'a')  # Ctrl+A 全选

# 获取元素文本
text = driver.find_element(By.CLASS_NAME, "message").text
print(text)

# 获取属性值
value = driver.find_element(By.ID, "result").get_attribute("data-id")

# 检查元素是否可见
is_visible = driver.find_element(By.ID, "loading").is_displayed()

# 检查元素是否可操作
is_enabled = driver.find_element(By.ID, "submit").is_enabled()

# 检查多选框/单选框是否选中
is_checked = driver.find_element(By.ID, "agree").is_selected()
```

## 5. 等待策略

### 隐式等待

```python
# 设置全局隐式等待（所有元素查找都应用此等待时间）
driver.implicitly_wait(10)  # 等待最多10秒
```

### 显式等待

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 等待特定元素出现，最多等待10秒
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "result"))
)

# 等待元素可点击
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "submit"))
)

# 等待元素可见
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "result"))
)

# 等待元素消失
WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.ID, "loading"))
)
```

## 6. 下拉框操作

```python
from selenium.webdriver.support.ui import Select

# 选择下拉框
select = Select(driver.find_element(By.ID, "province"))

# 按值选择
select.select_by_value("bj")

# 按可见文本选择
select.select_by_visible_text("北京")

# 按索引选择
select.select_by_index(1)

# 获取所有选项
all_options = select.options
for option in all_options:
    print(option.text)
```

## 7. 弹出框处理

```python
# 切换到警告框
alert = driver.switch_to.alert

# 获取文本
alert_text = alert.text

# 接受警告框(点击确定)
alert.accept()

# 取消警告框(点击取消)
alert.dismiss()

# 向提示框输入文本
alert.send_keys("测试文本")
```

## 8. 多窗口/标签页处理

```python
# 获取当前窗口句柄
current_window = driver.current_window_handle

# 获取所有窗口句柄
all_windows = driver.window_handles

# 切换到新窗口
driver.switch_to.window(all_windows[1])

# 切换回主窗口
driver.switch_to.window(all_windows[0])

# 关闭当前窗口
driver.close()

# 切换回剩余窗口
driver.switch_to.window(driver.window_handles[0])
```

## 9. iframe操作

```python
# 通过索引切换到iframe
driver.switch_to.frame(0)

# 通过id或name切换到iframe
driver.switch_to.frame("iframe_id")

# 通过元素切换到iframe
iframe = driver.find_element(By.CSS_SELECTOR, "#content iframe")
driver.switch_to.frame(iframe)

# 切回主文档
driver.switch_to.default_content()

# 切回父级iframe
driver.switch_to.parent_frame()
```

## 10. 与Pytest结合的UI测试框架

```python
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class TestBaiduSearch:
    @pytest.fixture
    def browser(self):
        """每个测试用例启动一个新的浏览器实例"""
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield driver
        # 测试结束后关闭浏览器
        driver.quit()
    
    def test_baidu_search(self, browser):
        """测试百度搜索功能"""
        browser.get("https://www.baidu.com")
        
        # 输入搜索关键词
        search_input = browser.find_element(By.ID, "kw")
        search_input.clear()
        search_input.send_keys("Selenium自动化测试")
        
        # 点击搜索按钮
        browser.find_element(By.ID, "su").click()
        
        # 验证搜索结果页面标题包含关键词
        assert "Selenium自动化测试" in browser.title
        
        # 验证搜索结果数量
        results = browser.find_elements(By.CSS_SELECTOR, ".result.c-container")
        assert len(results) > 0, "搜索结果应该不为空"
```

## 11. 页面对象模式(POM)实现

```python
# 页面基类
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

# 百度首页
class BaiduHomePage(BasePage):
    # 页面元素定位器
    SEARCH_INPUT = (By.ID, "kw")
    SEARCH_BUTTON = (By.ID, "su")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.baidu.com")
    
    def search(self, keyword):
        """执行搜索操作"""
        self.find_element(self.SEARCH_INPUT).clear()
        self.find_element(self.SEARCH_INPUT).send_keys(keyword)
        self.find_element(self.SEARCH_BUTTON).click()
        return BaiduResultPage(self.driver)

# 百度搜索结果页
class BaiduResultPage(BasePage):
    # 页面元素定位器
    RESULTS = (By.CSS_SELECTOR, ".result.c-container")
    
    def get_results_count(self):
        """获取搜索结果数量"""
        return len(self.find_elements(self.RESULTS))

# 测试用例
def test_baidu_search_with_pom(browser):
    """使用页面对象模式的百度搜索测试"""
    home_page = BaiduHomePage(browser)
    result_page = home_page.search("Selenium自动化测试")
    
    # 验证结果
    assert "Selenium自动化测试" in browser.title
    assert result_page.get_results_count() > 0
```
