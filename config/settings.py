"""  
全局配置模块，真实配置在.env文件中
"""

# 加入项目根目录，单跑文件测试模块时使用
import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).parent.parent
    )
)





# 加载环境变量
import os

from dotenv import load_dotenv

load_dotenv()

class Setting:
    # 知识库文件的存储路径
    KNOWLEDGE_FILE_PATH = os.getenv("KNOWLEDGE_FILE_PATH")
    # log日志的存储路径
    LOG_FILE_PATH = os.getenv("LOG_FILE_PATH")
    # log等级
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    # 文档切块大小
    CHUNK_SIZE=os.getenv("CHUNK_SIZE")
    # 每块重叠大小
    CHUNK_OVERLAP=os.getenv("CHUNK_OVERLAP")





if __name__ == "__main__":
    setting = Setting()
    print(f"KNOWLEDGE_FILE_PATH:\n{setting.KNOWLEDGE_FILE_PATH}")