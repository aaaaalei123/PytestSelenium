#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from config.conf import LOCATE_MODE
from tools.times import sleep
from tools.logger import log
from PIL import Image, ImageEnhance
import re
import pytesseract
import time



"""
selenium基类
本文件存放了selenium基类的封装方法
"""

class WebPage(object):
    """selenium基类"""

    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
        self.timeout = 20
        self.wait = WebDriverWait(self.driver, self.timeout)

    def get_url(self,url):
        """打开网址并验证"""
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(60)
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            log.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    @staticmethod
    def element_locator(func, locator):
        """元素定位器"""
        name, value = locator
        return func(LOCATE_MODE[name], value)

    def find_element(self, locator):
        """寻找单个元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_element_located(args)), locator)

    def find_elements(self, locator):
        """查找多个相同的元素"""
        return WebPage.element_locator(lambda *args: self.wait.until(
            EC.presence_of_all_elements_located(args)), locator)

    def elements_num(self, locator):
        """获取相同元素的个数"""
        number = len(self.find_elements(locator))
        log.info("相同元素：{}".format((locator, number)))
        return number

    def input_text(self, locator, txt):
        """输入(输入前先清空)"""
        sleep(0.5)
        ele = self.find_element(locator)
        ele.clear()
        ele.send_keys(txt)
        log.info("输入文本：{}".format(txt))

    def is_click(self, locator):
        """点击"""
        self.find_element(locator).click()
        sleep()
        log.info("点击元素：{}".format(locator))

    def element_text(self, locator):
        """获取当前的text"""
        _text = self.find_element(locator).text
        log.info("获取文本：{}".format(_text))
        return _text

    @property
    def get_source(self):
        """获取页面源代码"""
        return self.driver.page_source

    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    # def codeIdentify(self):
    #     # 截图保存到本地
    #     screenImg = "D:/imagesDemo/screenImg.png"
    #     # 浏览器截屏
    #     self.driver.get_screenshot_as_file(screenImg)
    #     # 定位验证码位置,大小
    #     location = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div[3]/img').location
    #     size = self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div[3]/img').size
    #     left = location['x']
    #     top = location['y']
    #     right = location['x'] + size['width']
    #     bottom = location['y'] + size['height']
    #     # 从文件读取截图，截取验证码位置再次保存
    #     img = Image.open(screenImg).crop((left, top, right, bottom))
    #     # 图片处理
    #     img = img.convert('RGBA')  # 转换模式：L | RGB
    #     img = img.convert('L')  # 转换模式：L | RGB
    #     img = ImageEnhance.Contrast(img)  # 增强对比度
    #     img = img.enhance(2.0)  # 增加饱和度
    #     img.save(screenImg)
    #     # 再次读取识别验证码
    #     img = Image.open(screenImg)
    #     code = pytesseract.image_to_string(img)
    #     # 打印识别的验证码
    #     print(code.strip())
    #     # 识别验证码去特殊符号-加工-正则表达式
    #     b = ''
    #     for i in code.strip():
    #         pattern = re.compile(r'[a-zA-Z0-9]')
    #         m = pattern.search(i)
    #         if m != None:
    #             b += i
    #         # 输出去特殊符号以后的验证码
    #         print(b)
    #         return b

if __name__ == "__main__":
    pass