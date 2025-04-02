import pytest
from utils.driver_manager import create_driver
from utils.logger import init_logger

@pytest.fixture(scope="session")
def browser():
    driver = create_driver()
    yield driver
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def logger():
    logger = init_logger()
    logger.info("Logging initialized..")
