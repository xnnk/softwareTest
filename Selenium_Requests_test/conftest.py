import pytest
import allure
import json
import os
from datetime import datetime

@pytest.fixture(scope="session", autouse=True)
def configure_allure(request):
    """配置Allure报告相关信息"""
    # 获取当前测试环境信息
    allure.attach(
        json.dumps({
            "Python版本": os.sys.version,
            "操作系统": os.name,
            "平台": os.sys.platform,
            "测试时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }, indent=4, ensure_ascii=False),
        name="环境信息",
        attachment_type=allure.attachment_type.JSON
    )

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """在测试用例失败时添加截图或日志"""
    outcome = yield
    report = outcome.get_result()
    
    # 测试失败时记录额外信息
    if report.when == "call" and report.failed:
        # 可以在这里添加失败时的截图或额外信息
        allure.attach(
            f"测试失败时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            name="失败信息",
            attachment_type=allure.attachment_type.TEXT
        )
