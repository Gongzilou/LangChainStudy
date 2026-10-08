"""  
全局配置模块，真实配置在.env文件中
"""

# 加载环境变量
import os

from dotenv import load_dotenv

load_dotenv()

class Setting:
    # 知识库文件
    KNOWLEDGE_FILE_PATH = os.getenv("KNOWLEDGE_FILE_PATH")