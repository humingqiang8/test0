"""示例测试用例"""

from base_test import BaseTestCase


class TestExampleAPI(BaseTestCase):
    """示例API测试用例"""
    
    def test_get_request(self):
        """测试GET请求"""
        # 发送GET请求
        response = self.send_request('GET', '/get', params={'key1': 'value1', 'key2': 'value2'})
        
        # 断言状态码
        self.assertion.assert_status_code(response, 200)
        
        # 断言响应时间
        self.assertion.assert_response_time(response, 5.0)  # 响应时间不超过5秒
        
        # 断言响应中包含特定键
        self.assertion.assert_json_key(response, 'args')
        
        # 检查响应中的具体值
        json_data = response.json()
        # httpbin.org返回的参数格式为字符串而非数组，根据实际响应调整验证逻辑
        args = json_data.get('args', {})
        self.assertIn('key1', args)
        self.assertIn('key2', args)
        # 验证参数值（httpbin.org会将参数作为字符串或字符串列表返回）
        key1_value = args['key1']
        key2_value = args['key2']
        # 如果是列表形式，则取第一个元素；如果是字符串，则直接比较
        if isinstance(key1_value, list):
            self.assertEqual(key1_value[0], 'value1')
        else:
            self.assertEqual(key1_value, 'value1')
        if isinstance(key2_value, list):
            self.assertEqual(key2_value[0], 'value2')
        else:
            self.assertEqual(key2_value, 'value2')
    
    def test_post_request(self):
        """测试POST请求"""
        # 准备POST数据
        post_data = {
            'name': 'test',
            'value': '123'
        }
        
        # 发送POST请求
        response = self.send_request('POST', '/post', json_data=post_data)
        
        # 断言状态码
        self.assertion.assert_status_code(response, 200)
        
        # 断言响应时间
        self.assertion.assert_response_time(response, 5.0)
        
        # 验证POST数据是否正确发送
        json_data = response.json()
        self.assertEqual(json_data['json']['name'], 'test')
        self.assertEqual(json_data['json']['value'], '123')
    
    def test_status_code_200(self):
        """测试状态码为200的API"""
        response = self.send_request('GET', '/status/200')
        
        # 断言状态码
        self.assertion.assert_status_code(response, 200)
        
        # 断言响应头
        self.assertion.assert_header(response, 'Content-Type')
    
    def test_headers(self):
        """测试响应头信息"""
        response = self.send_request('GET', '/headers')
        
        # 断言状态码
        self.assertion.assert_status_code(response, 200)
        
        # 断言响应中包含headers键
        self.assertion.assert_json_key(response, 'headers')
        
        # 断言特定响应头
        self.assertion.assert_header(response, 'Content-Type', 'application/json')


if __name__ == '__main__':
    unittest.main()