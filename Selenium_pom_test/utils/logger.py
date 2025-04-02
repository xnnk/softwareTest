import os
import logging
from datetime import datetime


def init_logger():
    # 定义日志目录路径（项目根目录下的 logs 文件夹）
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")  # 根据实际结构调整层级

    # 自动创建目录（如果不存在）
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 日志文件路径
    log_file = os.path.join(log_dir, f"test_{datetime.now().strftime('%Y%m%d_%H%M')}.log")
    file_handler = logging.FileHandler(log_file)  # 使用绝对路径
    file_handler.setFormatter(formatter)

    # 控制台日志
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    print("Current log directory:", os.path.abspath(log_dir))

    return logger
