import sys, os
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 手机号码输入框
    # //input[@class='mobile-input-phone']
    mobile_input_phone =  By.XPATH,("class,mobile-input-phone"), "input", 0
    # 勾选协议同意
    # //span[@class='ud__checkbox']
    agreement_checkbox = By.XPATH, ("class,ud__checkbox"), "span", 0
    # 下一步按钮
    # //div[@class='step-box__body']//button
    next_button = By.XPATH, ("class,step-box__body"), "button", 0

    # 密码输入框
    password_label = By.CSS_SELECTOR, "form > label:nth-child(2)", 0, 0
    # 登录按钮
    login_button = By.CSS_SELECTOR, "form > div", 0, 0
    # 注册跳转按钮
    sign_up_button = By.XPATH, ("text(),'未有帳號？立即註冊！',2"), 0, 0


    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 定位用户电话输入框并输入电话
    def find_mobile_input_phone_and_sendkeys(self, phone):
        self.defined_sendkeys(self.mobile_input_phone, phone)

    # 定位勾选协议同意
    def find_agreement_checkbox_and_check(self):
        self.defined_click(self.agreement_checkbox)

    # 定位下一步按钮
    def find_next_button_and_check(self):
        self.defined_click(self.next_button)


    # 定位用户密码输入框并输入密码
    def find_input_password_label_and_sendkeys(self, password):
        self.defined_sendkeys(self.password_label, password)

    # 定位登录按钮并点击
    def find_login_button_and_click(self):
        self.defined_click(self.login_button)

    # 定位注册跳转按钮并点击
    def find_sign_up_button_and_click(self):
        self.defined_click(self.sign_up_button)

