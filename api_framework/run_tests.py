"""运行测试的主文件"""

import unittest
import os
import sys
from datetime import datetime
from config.config import REPORT_DIR, REPORT_NAME


def create_report_dir():
    """创建报告目录"""
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)


def run_all_tests():
    """运行所有测试"""
    # 创建报告目录
    create_report_dir()
    
    # 发现并运行所有测试
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # 运行测试并生成报告
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 生成测试报告
    report_path = os.path.join(REPORT_DIR, f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"测试报告 - {datetime.now()}\n")
        f.write(f"总测试数: {result.testsRun}\n")
        f.write(f"失败数: {len(result.failures)}\n")
        f.write(f"错误数: {len(result.errors)}\n")
        f.write(f"成功率: {((result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100):.2f}%\n\n")
        
        if result.failures:
            f.write("失败的测试:\n")
            for test, traceback in result.failures:
                f.write(f"  {test}: {traceback}\n\n")
        
        if result.errors:
            f.write("错误的测试:\n")
            for test, traceback in result.errors:
                f.write(f"  {test}: {traceback}\n\n")
    
    print(f"\n测试报告已生成: {report_path}")
    return result


def run_specific_test(test_class_name):
    """运行特定的测试类"""
    # 动态导入测试类
    module_name = f"tests.test_example"
    module = __import__(module_name, fromlist=[test_class_name])
    test_class = getattr(module, test_class_name)
    
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(test_class)
    
    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # 运行特定测试
        test_class_name = sys.argv[1]
        print(f"运行测试类: {test_class_name}")
        run_specific_test(test_class_name)
    else:
        # 运行所有测试
        print("开始运行所有测试...")
        run_all_tests()