# Python自动化测试学习指南

这个仓库提供了Python自动化测试的快速学习资料，从Python基础到高级测试框架的使用。

## 目录

1. [Python语法基础](python_basics.md)
   - 变量、条件语句、循环、函数
   - 文件操作（CSV、Excel、JSON）

2. [Pytest测试框架](pytest_guide.md)
   - unittest基础
   - pytest使用指南
   - 高级特性（fixtures、参数化测试）
   - 生成测试报告

3. [API接口测试 (requests)](api_testing.md)
   - 基本请求操作
   - 会话与认证
   - 断言与验证
   - 请求异常处理

4. [UI自动化测试 (Selenium)](ui_testing.md)
   - 浏览器控制
   - 元素定位与操作
   - 等待策略
   - 页面对象模式

## 安装必要的包

```bash
pip install pytest pytest-html pytest-xdist requests selenium webdriver-manager openpyxl
```

## 学习路线建议

1. 先掌握Python基础语法，确保理解变量、条件、循环和函数概念
2. 学习pytest测试框架基础，编写简单测试用例
3. 学习requests库，进行API测试
4. 学习Selenium，进行UI自动化测试
5. 将以上技术结合，构建完整的自动化测试框架

## 推荐工具

- **PyCharm**: 强大的Python IDE，适合编写和调试代码
- **Jupyter Notebook**: 交互式学习环境，适合快速练习和实验
- **Postman**: API测试辅助工具，帮助理解API请求

## 实践项目建议

1. **API测试项目**: 选择开放API（如天气API）编写完整的测试套件
2. **Web UI测试**: 为电商网站编写登录、搜索、下单等功能的自动化测试
3. **测试框架搭建**: 结合Jenkins等CI工具，实现自动化测试流水线

## 注意事项

- 始终遵循测试的基本原则：独立、可重复、自我验证
- 编写测试时考虑边界情况和异常场景
- 定期重构测试代码，保持测试的可维护性
