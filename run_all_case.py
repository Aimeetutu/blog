import unittest
import os
from HTMLTestRunner_cn import HTMLTestRunner

#用例路径
case_path = os.path.join(os.getcwd(),"case")

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test_*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    with open(r'E:\Bolg\report\BolgReport.html','wb+') as f:
        runner = HTMLTestRunner(stream=f,
                                    title='登录博客园的测试报告',
                                    description='以下是测试用例执行结果',
                                    verbosity=2,
                                    retry=1,
                                   save_last_try = True
                                    )
        #调用add_case函数返回值
        runner.run(all_case())