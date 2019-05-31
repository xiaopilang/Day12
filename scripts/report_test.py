import os

import allure
import pytest
class Test_001:

    def test_001(self):
        print("测试用例1")

        with open(os.getcwd()+os.sep+"scripts/4.PNG","rb")as f:
             allure.attach("截图",f.read(),allure.attach_type.PNG)

