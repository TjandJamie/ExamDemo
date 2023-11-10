# encoding = utf-8
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import time

class BaseAction:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)


    # 自定义查找某一个元素
    def defined_find_element(self, loc, t=5, poll=1):
        try:
            loc_by, loc_value, loc_tag, loc_end = loc
            if loc_by == By.XPATH:
                loc_value = self.make_xpath_with_feature(loc_value, loc_tag, loc_end)
            return WebDriverWait(self.driver, t, poll).until(lambda x: x.find_element(loc_by, loc_value))
        except Exception as e:
            print(e)
            # return e
            return False

    # 对查找元素给的关键字进行进一步处理
    def make_xpath_with_feature(self, feature, tag, end):
        xpath_start = ""
        xpath_end = ""
        xpath = ""
        if tag == "" or tag == 0:
            xpath_start = "//*["
        elif tag != "":
            xpath_start = "//%s[" % tag
        if end == "" or end == 0:
            xpath_end = "]"
        elif end != "":
            xpath_end = "]" + "%s" % end
        if isinstance(feature, str):
            xpath = self.make_xpath_with_unit_feature(feature)
        else:
            for i in feature:
                xpath = xpath + self.make_xpath_with_unit_feature(i)
        xpath = xpath.rstrip("and")
        xpath = xpath_start + xpath + xpath_end
        # print(xpath)
        return xpath
    # 对查找元素给的关键字进行进一步处理
    def make_xpath_with_unit_feature(self, unit_feature):
        xpath = ""
        args = unit_feature.split(",")
        if len(args) == 2:
            xpath = xpath + "@" + args[0] + "='" + args[1] + "'and"
        elif len(args) == 3:
            if args[2] == "0":
                xpath = xpath + "@" + args[0] + "='" + args[1] + "'and"
            elif args[2] == "1":
                xpath = xpath + "contains(@" + args[0] + ",'" + args[1] + "')and"
            elif args[2] == "2":
                xpath = xpath + "contains(" + args[0] + "," + args[1] + ")and"
        return xpath

    # 自定义查找某一类元素集
    def defined_find_elements(self, loc, t=5, poll=1):
        try:
            loc_by, loc_value, loc_tag, loc_end = loc
            if loc_by == By.XPATH:
                loc_value = self.make_xpath_with_feature(loc_value, loc_tag, loc_end)
            return WebDriverWait(self.driver, t, poll).until(lambda x: x.find_elements(loc_by, loc_value))
        except Exception as e:
            print(e)
            return False

    # 判断查找元素是否存在
    def defined_element_is_exist_or_not(self, loc, t=5, poll=1):
        result = self.defined_find_element(loc, t, poll)
        if result is False:
            # print("页面中不存在此元素")
            return False
        else:
            # print("页面中存在此元素")
            return True

    # 判断查找某类元素是否存在
    def defined_elements_is_exist_or_not(self, loc, t=5, poll=1):
        result = self.defined_find_elements(loc, t, poll)
        if result is False:
            # print("页面中不存在此元素")
            return False
        else:
            # print("页面中存在此元素")
            return True

    # 查找元素并点击
    def defined_click(self, loc, t=5, poll=1):
        try:
            self.defined_find_element(loc, t, poll).click()
        except Exception as e:
            raise e


    # 查找元素并双击,后输入关键字
    def defined_double_click(self, loc, t=5, poll=1):
        try:
            element = self.defined_find_element(loc, t, poll)
            ActionChains(self.driver).double_click(element).send_keys(Keys.BACKSPACE).perform()
        except Exception as e:
            raise e

    # 多次点击某一个元素
    def defined_cycle_click_method(self, loc, r, t=5, poll=1):
        element = self.defined_find_element(loc, t, poll)
        for i in range(r):
            element.click()
            time.sleep(1)

    # 查找元素并输入关键字
    def defined_sendkeys(self, loc, content, t=5, poll=1):
        try:
            self.defined_find_element(loc, t, poll).send_keys(content)
        except Exception as e:
            raise e

    # 查找元素，输入关键字并点击ENTER
    def defined_sendkeys_and_enter(self, loc, content, t=5, poll=1):
        try:
            element = self.defined_find_element(loc, t, poll)
            ActionChains(self.driver).click(element).send_keys(content).send_keys(Keys.ENTER).perform()
        except Exception as e:
            raise e

    # 定位页面的iframe页面
    def defined_swich_to_frame(self, loc, t=5, poll=1):
        try:
            self.driver.switch_to.frame(self.defined_find_element(loc, t, poll))
        except Exception as e:
            raise e

    # 从iframe页面重新聚焦到当前页面
    def defined_frame_swich_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    # 滑动滚动条
    def defined_slide_scroll_bar_method(self, t, p):
        '''
        使用JS来操作浏览器页面
        '''
        for i in range(t):
            js = 'document.documentElement.scrollTop=%d' % (i * p)
            self.driver.execute_script(js)
            time.sleep(1)

    # 滑动滚动条
    def defined_slide_scroll_bar_method_two(self, start, t, p):
        '''
        使用JS来操作浏览器页面
        '''
        for i in range(start, start+t):
            js = 'document.documentElement.scrollTop=%d' % (i * p)
            self.driver.execute_script(js)
            time.sleep(1)


    # 设置元素的属性值
    def defined_add_attribute(self, elementobj, attributeName, value):
        '''
        封装向页面标签添加新属性的方法
        调用JS给页面标签添加新属性，arguments[0]~arguments[2]分别
        会用后面的element，attributeName和value参数进行替换
        添加新属性的JS代码语法为：element.attributeName=value
        比如input.name='test'
        '''
        self.driver.execute_script("arguments[0].%s=arguments[1]" % attributeName, elementobj, value)

    def defined_set_attribute(self, elementobj, attributeName, value):
        '''
        封装设置页面对象的属性值的方法
        调用JS代码修改页面元素的属性值，arguments[0]~arguments[1]分别
        会用后面的element，attributeName和value参数进行替换
        '''
        self.driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementobj, attributeName, value)

    def defined_get_attribute(self, elementobj, attributeName):
        # 封装获取页面对象的属性值方法
        return elementobj.get_attribute(attributeName)


    def defined_remove_attribute(self, elementobj, attributeName):
        '''
        封装删除页面属性的方法
        调用JS代码删除页面元素的指定的属性，arguments[0]~arguments[1]分别
        会用后面的element，attributeName参数进行替换
        '''
        self.driver.execute_script("arguments[0].removeAttribute(arguments[1])", elementobj, attributeName)

    # 定义清空输入框内容方法
    def defined_clear_input_box(self, loc):
        js = 'document.querySelector(%s).value="";' % loc
        print(js)
        self.driver.execute_script(js)

    # 清除Textarea标签的内容并输入新的内容
    def defined_clear_textarea_contant(self, element, content):
        try:
            # windows 系统，则使用Control+a，mac则使用Command+a
            ActionChains(self.driver).click(element).key_down(Keys.COMMAND).key_down("a").key_down(Keys.DELETE).perform()
            element.send_keys(content)
        except Exception as e:
            raise e




