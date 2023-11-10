# encoding = utf-8
import time

from selenium import webdriver

def init_driver():
    options = webdriver.ChromeOptions()
    # 解决浏览器受自动化测试软件控制提示
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 解决浏览器的密码弹窗
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--no-sandbox')
    # 设置在HEADLESS模式下运行
    # options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    # 允许在无GPU的环境下运行，可选
    # options.add_argument('–disable-gpu')
    # 设置默认编码为utf-8
    options.add_argument('lang=zh_CN.UTF-8')
    # 设置浏览器的分辨率大小（建议设置）
    options.add_argument('--window-size=1920x1080')
    driver = webdriver.Chrome(options=options)
    # 清除缓存
    driver.delete_all_cookies()
    # 最大化窗口
    driver.maximize_window()
    return driver

