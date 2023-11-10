import sys, os
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class IndexPage(BaseAction):
    #关闭提示页面
    # //div[@data-elem-id='MC2ANWQ36m']
    tip_page_close_button = By.XPATH, ("data-elem-id,MC2ANWQ36m"), "div", 0

    # 登入按钮
    #  //a[contains(text(),'登录')]
    login_button = By.XPATH, ("text(),'登录',2"), "a", 0

    # 设置账号登录按钮
    # //span[@class='universe-icon switch-icon']
    set_login_method_button = By.XPATH,("class,universe-icon switch-icon"), "span", 0


    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 首页选择登入按钮
    def find_tip_page_close_button_and_click(self):
        self.defined_click(self.tip_page_close_button)

    # 首页选择登入按钮
    def find_login_button_and_click(self):
        self.defined_click(self.login_button)

    # 设置登录方式
    def set_login_method_and_click(self):
        self.defined_click(self.set_login_method_button)

