import sys, os

import allure
import pytest

sys.path.append(os.getcwd())
from base.base_driver import init_driver
from base.base_login import BaseLogin
from base.base_analyze import BaseAnalyze

@pytest.mark.run(order=4)
@allure.feature("测试用户登录流程")
class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.base_login = BaseLogin(self.driver)
        self.base_analyze = BaseAnalyze()
        self.func_name = "test_login"
        self.file_name = "login_data.yaml"

    def teardown(self):
        self.driver.quit()



    @allure.title("测试用户登录流程")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_phone_login(self):
        # self.base_login.open_feishu()
        params = self.base_analyze.analyze_key(self.func_name, self.file_name)
        # print(params)
        url = params["url"]
        phone = params["tester1_phone"]
        password = params["tester1_password"]
        self.base_login.login(url, phone, password)


