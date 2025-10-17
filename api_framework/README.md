# API自动化测试框架

## 框架概述

这是一个基于Python的API自动化测试框架，提供了HTTP请求封装、断言工具、测试用例管理等功能，方便进行接口自动化测试。

## 目录结构

```
api_framework/
├── common/                 # 通用组件
│   └── http_client.py      # HTTP客户端封装
├── config/                 # 配置文件
│   └── config.py           # 配置参数
├── tests/                  # 测试用例
│   ├── base_test.py        # 测试用例基类
│   └── test_example.py     # 示例测试用例
├── utils/                  # 工具类
│   ├── assertion.py        # 断言工具
│   └── test_data_handler.py # 测试数据处理工具
├── reports/                # 测试报告（自动生成）
├── run_tests.py            # 运行测试的主文件
├── requirements.txt        # 项目依赖
└── README.md               # 说明文档
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置说明

在 `config/config.py` 中可以配置：

- `BASE_URL`: API基础URL
- `REQUEST_TIMEOUT`: 请求超时时间
- `MAX_RETRIES`: 最大重试次数
- `REPORT_DIR`: 报告保存目录

## 使用示例

### 1. 编写测试用例

继承 `BaseTestCase` 类编写测试用例：

```python
from tests.base_test import BaseTestCase

class TestMyAPI(BaseTestCase):
    
    def test_get_user_info(self):
        # 发送GET请求
        response = self.send_request('GET', '/users/1')
        
        # 断言状态码
        self.assertion.assert_status_code(response, 200)
        
        # 断言响应时间
        self.assertion.assert_response_time(response, 5.0)
        
        # 断言响应JSON中包含特定键
        self.assertion.assert_json_key(response, 'name')
        
        # 断言JSON值
        self.assertion.assert_json_value(response, 'name', 'John Doe')
```

### 2. 运行测试

运行所有测试：

```bash
python run_tests.py
```

运行特定测试类：

```bash
python run_tests.py TestExampleAPI
```

## 框架特性

1. **HTTP客户端封装**: 提供GET、POST、PUT、DELETE等常用HTTP方法
2. **断言工具**: 提供状态码、响应时间、JSON键值等多种断言方法
3. **重试机制**: 请求失败时自动重试
4. **测试报告**: 自动生成测试报告
5. **灵活配置**: 支持各种配置参数

## 扩展功能

- 支持JSON、YAML、CSV格式的测试数据
- 可自定义请求头、认证等信息
- 支持参数化测试
- 集成日志记录功能