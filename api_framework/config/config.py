"""配置文件"""

# API基础配置
BASE_URL = "https://httpbin.org"  # 示例API地址，实际项目中请替换为真实的API地址

# 请求配置
REQUEST_TIMEOUT = 30  # 请求超时时间（秒）
MAX_RETRIES = 3       # 最大重试次数

# 报告配置
REPORT_DIR = "../reports"  # 可根据需要修改为绝对路径如 "/workspace/api_framework/reports"
REPORT_NAME = "api_test_report.html"

# 日志配置
LOG_LEVEL = "INFO"
LOG_DIR = "../logs"
LOG_NAME = "api_test.log"