import pytest
import allure

class TestStep:
    @allure.step(title="我是测试第一步")
    def test_001(self):
        allure.attach("我是第一步标题", "对第一步的具体描述")
        print("测试用例1")
        assert True
    @allure.step(title="我是测试第二步")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test_002(self):
        allure.attach("用户名:","张三")
        allure.attach("密码:","123456")
        print("测试用例2")
        assert True

    @allure.step(title="我是测试第三步")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_003(self):
        allure.attach("我是标题", "对步骤三的描述")
        print("测试用例3")
        assert False

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="我是测试第四步")
    def test_004(self):
        allure.attach("我是步骤4的标题", "对步骤4 的具体描述")
        print("测试用例4")
        assert True

    @allure.step(title="我是测试第五步")
    def test_005(self):
        allure.attach("我是第五步标题","对第五步具体描述")
        print("测试用例5")
        assert True