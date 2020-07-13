#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/7/3 9:41 
# filename: hatest_unittest_1.py
# development_tool： PyCharm

import unittest, ddt, requests
from Common.read_excel import Do_excel
from Common.operate_logs import Log

@ddt.ddt
class Api_test(unittest.TestCase):
    """
    单元测试
    """
    @classmethod
    def setUp(self):
        pass

    @classmethod
    def tearDown(self):
        pass

    @ddt.data(*Do_excel().read())

    def test_1(self, item):
        url, data = item["url"], eval(item["data"])
        try:
            if item["method"] == "get":
                res = requests.get(url, data).json()
                Log().info("请求成功")

            elif item["method"] == "post":
                res = requests.post(url, data).json()
                Log().info("请求成功")

        except Exception as e:
            Log().error("请求失败,错误:%s" % e)
            raise e

        try:
            Do_excel().write_back(item["case_id"], res["error_code"], str(res))
            Log().info("写入成功")
        except Exception as e:
            Log().info("写入失败,原因{0}".format(e))
            raise e

        self.assertEqual(res["error_code"], 0)
        return res

