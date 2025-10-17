"""测试数据处理工具"""

import json
import yaml
import csv
from typing import Dict, List, Any


class TestDataHandler:
    """测试数据处理工具类"""
    
    @staticmethod
    def load_json_data(file_path: str) -> Dict[str, Any]:
        """
        加载JSON格式的测试数据
        
        Args:
            file_path: JSON文件路径
            
        Returns:
            dict: 解析后的数据
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    @staticmethod
    def save_json_data(data: Dict[str, Any], file_path: str):
        """
        保存数据为JSON格式
        
        Args:
            data: 要保存的数据
            file_path: 保存的文件路径
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    @staticmethod
    def load_yaml_data(file_path: str) -> Dict[str, Any]:
        """
        加载YAML格式的测试数据
        
        Args:
            file_path: YAML文件路径
            
        Returns:
            dict: 解析后的数据
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    
    @staticmethod
    def load_csv_data(file_path: str) -> List[Dict[str, str]]:
        """
        加载CSV格式的测试数据
        
        Args:
            file_path: CSV文件路径
            
        Returns:
            list: 解析后的数据列表
        """
        data = []
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(dict(row))
        return data
    
    @staticmethod
    def generate_test_cases_from_data(test_data: List[Dict[str, Any]], test_func) -> List:
        """
        根据测试数据生成测试用例
        
        Args:
            test_data: 测试数据列表
            test_func: 测试函数
            
        Returns:
            list: 生成的测试用例列表
        """
        test_cases = []
        for i, data in enumerate(test_data):
            def make_test(data_copy):
                def test_case(self):
                    test_func(self, data_copy)
                return test_case
            test_cases.append(make_test(data))
        return test_cases