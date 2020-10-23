#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
from tools.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage


class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_url(self, drivers):
        """打开网址"""
        search = SearchPage(drivers)
        search.get_url(ini.url)

    def test_login(self,drivers):
        """登录"""
        search = SearchPage(drivers)

        search.input_search("admin")
        search.input_pass("admin")





        search.input_code("123")
        result = re.search(r'项目管理',search.get_source)
        log.info(result)
        assert  result





if __name__ == '__main__':
    pytest.main(['test_search.py'])