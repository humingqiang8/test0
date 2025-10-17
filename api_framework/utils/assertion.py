"""断言工具类"""


class Assertion:
    """断言工具类，提供各种断言方法"""
    
    @staticmethod
    def assert_status_code(response, expected_code: int):
        """
        断言响应状态码
        
        Args:
            response: 响应对象
            expected_code: 期望的状态码
        """
        actual_code = response.status_code
        assert actual_code == expected_code, f"状态码断言失败: 期望 {expected_code}, 实际 {actual_code}"
        print(f"✓ 状态码断言成功: {actual_code}")
    
    @staticmethod
    def assert_response_time(response, max_time: float):
        """
        断言响应时间
        
        Args:
            response: 响应对象
            max_time: 最大响应时间（秒）
        """
        response_time = response.elapsed.total_seconds()
        assert response_time <= max_time, f"响应时间断言失败: 期望 ≤{max_time}s, 实际 {response_time}s"
        print(f"✓ 响应时间断言成功: {response_time}s")
    
    @staticmethod
    def assert_json_key(response, key: str):
        """
        断言响应JSON中包含指定键
        
        Args:
            response: 响应对象
            key: 要检查的键
        """
        try:
            json_data = response.json()
            assert key in json_data, f"JSON键断言失败: 响应中不包含键 '{key}'"
            print(f"✓ JSON键断言成功: 包含键 '{key}'")
        except ValueError:
            raise AssertionError("响应不是有效的JSON格式")
    
    @staticmethod
    def assert_json_value(response, key: str, expected_value):
        """
        断言响应JSON中指定键的值
        
        Args:
            response: 响应对象
            key: 要检查的键
            expected_value: 期望的值
        """
        try:
            json_data = response.json()
            actual_value = json_data.get(key)
            assert actual_value == expected_value, f"JSON值断言失败: 键 '{key}', 期望 {expected_value}, 实际 {actual_value}"
            print(f"✓ JSON值断言成功: 键 '{key}', 值为 {actual_value}")
        except ValueError:
            raise AssertionError("响应不是有效的JSON格式")
    
    @staticmethod
    def assert_text_in_response(response, text: str):
        """
        断言响应文本中包含指定内容
        
        Args:
            response: 响应对象
            text: 要检查的文本
        """
        content = response.text
        assert text in content, f"文本包含断言失败: 响应中不包含 '{text}'"
        print(f"✓ 文本包含断言成功: 包含 '{text}'")
    
    @staticmethod
    def assert_header(response, header_name: str, expected_value: str = None):
        """
        断言响应头信息
        
        Args:
            response: 响应对象
            header_name: 响应头名称
            expected_value: 期望的响应头值（可选）
        """
        headers = dict(response.headers)
        assert header_name in headers, f"响应头断言失败: 不包含头 '{header_name}'"
        
        if expected_value is not None:
            actual_value = headers[header_name]
            assert actual_value == expected_value, f"响应头值断言失败: 头 '{header_name}', 期望 {expected_value}, 实际 {actual_value}"
            print(f"✓ 响应头断言成功: '{header_name}' = '{actual_value}'")
        else:
            print(f"✓ 响应头断言成功: 包含头 '{header_name}'")