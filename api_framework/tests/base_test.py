"""测试用例基类"""

import unittest
import json
from common.http_client import http_client
from utils.assertion import Assertion
from config.config import BASE_URL


class BaseTestCase(unittest.TestCase):
    """测试用例基类，提供通用的测试方法和属性"""
    
    def setUp(self):
        """测试用例初始化方法"""
        self.client = http_client
        if BASE_URL:
            self.client.base_url = BASE_URL
        self.assertion = Assertion()
        
    def tearDown(self):
        """测试用例清理方法"""
        pass
    
    def send_request(self, method: str, url: str, **kwargs):
        """
        发送HTTP请求的便捷方法
        
        Args:
            method: HTTP方法
            url: 请求URL
            **kwargs: 其他参数
            
        Returns:
            requests.Response: 响应对象
        """
        method = method.upper()
        if method == 'GET':
            return self.client.get(url, **kwargs)
        elif method == 'POST':
            return self.client.post(url, **kwargs)
        elif method == 'PUT':
            return self.client.put(url, **kwargs)
        elif method == 'DELETE':
            return self.client.delete(url, **kwargs)
        elif method == 'PATCH':
            return self.client.patch(url, **kwargs)
        else:
            raise ValueError(f"不支持的HTTP方法: {method}")
    
    def load_test_data(self, file_path: str):
        """
        加载测试数据
        
        Args:
            file_path: 测试数据文件路径
            
        Returns:
            dict: 测试数据
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)