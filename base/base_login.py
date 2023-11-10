# encoding = utf-8
import sys, os

sys.path.append(os.getcwd())
from page.login_page import LoginPage
from page.index_page import IndexPage
import time
from base.base_analyze import BaseAnalyze




class BaseLogin:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)
        self.base_analyze = BaseAnalyze()
        self.func_name = "test_login"
        self.file_name = "login_data.yaml"

    def open_feishu(self):
        params = self.base_analyze.analyze_key(self.func_name, self.file_name)
        # print(params)
        url = params["url"]
        # url = "https://web-stg.tapnow.io/zh-HK/"
        # 打开网址
        self.driver.get(url)

    # a = ("https://web-stg.tapnow.io","jamie.tan@presslogic.com","Tjandjamie0")
    # @pytest.mark.parametrize("url, email, password", [a])
    def login(self, url, phone, password):
        # 打开网址
        self.driver.get(url)
        time.sleep(2)
        #关闭提示页面
        self.index_page.find_tip_page_close_button_and_click()
        time.sleep(2)
        # 选择登录按钮
        self.index_page.find_login_button_and_click()
        time.sleep(2)
        # 设置账号登录
        self.index_page.set_login_method_and_click()
        time.sleep(2)
        # 输入手机号码
        self.login_page.find_mobile_input_phone_and_sendkeys(phone)
        time.sleep(2)
        # 定位勾选协议同意
        self.login_page.find_agreement_checkbox_and_check()
        time.sleep(2)
        # 定位下一步按钮
        self.login_page.find_next_button_and_check()
        # # 输入密码
        # self.login_page.find_input_password_label_and_sendkeys(password)
        # # 点击登录
        # self.login_page.find_login_button_and_click()
        time.sleep(10)





