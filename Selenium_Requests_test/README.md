# Web自动化与接口自动化测试框架

本项目包含了基于Selenium的Web自动化测试框架和基于Requests+pytest的接口自动化测试框架示例。

## 环境准备

1. 安装依赖项：
```bash
pip install -r requirements.txt
```

2. 安装Allure命令行工具（用于生成报告）：
   - 对于Windows，可以通过Scoop安装：`scoop install allure`
   - 对于macOS，使用Homebrew：`brew install allure`
   - 对于Linux，可以使用包管理器或直接下载二进制文件

## 目录结构

```
Selenium_Requests_test/
├── __init__.py
├── selenium_example.py  # Selenium Web自动化示例
├── requests_pytest_example.py  # Requests接口自动化示例
├── conftest.py  # pytest配置文件
└── requirements.txt  # 项目依赖
```

## 功能特性

### Selenium Web自动化

- 支持多浏览器测试（Chrome、Firefox）
- 使用多种元素定位方法（ID、XPath、CSS选择器等）
- 实现显式和隐式等待策略
- 示例包括：
  - 登录功能测试
  - 表单提交
  - 数据爬取

### Requests + pytest 接口自动化

- 支持各种HTTP请求方法（GET、POST、PUT、DELETE）
- 使用pytest参数化测试
- 集成Allure生成美观的测试报告
- 示例包括：
  - 获取用户信息
  - 创建新资源
  - 更新资源
  - 删除资源
  - 带参数和请求头的请求

## 使用方法

### 运行Selenium测试

```bash
python selenium_example.py
```

### 运行接口自动化测试

```bash
# 运行测试并生成Allure报告数据
pytest requests_pytest_example.py -v --alluredir=./allure-results

# 生成并查看Allure报告
allure serve ./allure-results
```

## 注意事项

1. 确保已安装Chrome或Firefox浏览器
2. webdriver-manager将自动下载和管理浏览器驱动
3. 示例中使用的API是公开的模拟API
