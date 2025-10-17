"""HTTP客户端封装"""

import requests
import json
from typing import Optional, Dict, Any
from config.config import REQUEST_TIMEOUT, MAX_RETRIES


class HttpClient:
    """HTTP客户端类，封装常用的HTTP请求方法"""
    
    def __init__(self, base_url: str = None):
        """
        初始化HTTP客户端
        
        Args:
            base_url: API基础URL
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = REQUEST_TIMEOUT
        self.max_retries = MAX_RETRIES
        
        # 设置通用请求头
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'API-Automation-Framework/1.0'
        })
    
    def _make_request(self, method: str, url: str, **kwargs) -> requests.Response:
        """
        发送HTTP请求的通用方法
        
        Args:
            method: HTTP方法 (GET, POST, PUT, DELETE等)
            url: 请求URL
            **kwargs: 其他请求参数
            
        Returns:
            requests.Response: 响应对象
        """
        # 如果提供了base_url，则拼接完整URL
        if self.base_url and not url.startswith(('http://', 'https://')):
            full_url = f"{self.base_url.rstrip('/')}/{url.lstrip('/')}"
        else:
            full_url = url
        
        # 设置默认超时时间
        if 'timeout' not in kwargs:
            kwargs['timeout'] = self.timeout
            
        # 执行请求
        for attempt in range(self.max_retries + 1):
            try:
                response = self.session.request(method, full_url, **kwargs)
                return response
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries:
                    raise e
                print(f"请求失败，正在重试 ({attempt + 1}/{self.max_retries}): {e}")
    
    def get(self, url: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        """
        GET请求
        
        Args:
            url: 请求URL
            params: URL参数
            **kwargs: 其他参数
            
        Returns:
            requests.Response: 响应对象
        """
        return self._make_request('GET', url, params=params, **kwargs)
    
    def post(self, url: str, data: Optional[Dict] = None, json_data: Optional[Dict] = None, **kwargs) -> requests.Response:
        """
        POST请求
        
        Args:
            url: 请求URL
            data: 表单数据
            json_data: JSON数据
            **kwargs: 其他参数
            
        Returns:
            requests.Response: 响应对象
        """
        if json_data:
            kwargs['json'] = json_data
        elif data:
            kwargs['data'] = data
        return self._make_request('POST', url, **kwargs)
    
    def put(self, url: str, data: Optional[Dict] = None, json_data: Optional[Dict] = None, **kwargs) -> requests.Response:
        """
        PUT请求
        
        Args:
            url: 请求URL
            data: 表单数据
            json_data: JSON数据
            **kwargs: 其他参数
            
        Returns:
            requests.Response: 响应对象
        """
        if json_data:
            kwargs['json'] = json_data
        elif data:
            kwargs['data'] = data
        return self._make_request('PUT', url, **kwargs)
    
    def delete(self, url: str, **kwargs) -> requests.Response:
        """
        DELETE请求
        
        Args:
            url: 请求URL
            **kwargs: 其他参数
            
        Returns:
            requests.Response: 响应对象
        """
        return self._make_request('DELETE', url, **kwargs)
    
    def patch(self, url: str, data: Optional[Dict] = None, json_data: Optional[Dict] = None, **kwargs) -> requests.Response:
        """
        PATCH请求
        
        Args:
            url: 请求URL
            data: 表单数据
            json_data: JSON数据
            **kwargs: 其他参数
            
        Returns:
            requests.Response: 响应对象
        """
        if json_data:
            kwargs['json'] = json_data
        elif data:
            kwargs['data'] = data
        return self._make_request('PATCH', url, **kwargs)


# 全局HTTP客户端实例
http_client = HttpClient()