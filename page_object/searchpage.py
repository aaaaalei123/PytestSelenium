#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""页面对象"""
from page.webpage import WebPage, sleep
from common.readelement import Element

search = Element('search')

class SearchPage(WebPage):
    """搜索类"""

    def input_search(self, content):
        """输入账号"""
        self.input_text(search['账号'], txt=content)
        sleep(2)

    def input_pass(self, content):
        """输入密码"""
        self.input_text(search['密码'], txt=content)
        sleep(2)

    def input_code(self, content):
        """输入验证码"""
        self.input_text(search['验证码'], txt=content)
        sleep(2)

    # @property
    # def imagine(self):
    #     """搜索联想"""
    #     return [x.text for x in self.find_elements(search['候选'])]

    def click_search(self):
        """点击登录"""
        self.is_click(search['登录按钮'])

