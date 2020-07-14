#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/7/13 19:10 
# filename: test_pytest.py
# development_tool： PyCharm

import pytest, allure, requests
from Common.read_excel import Do_excel
from Common.operate_logs import Log


class Test_api:
    def setup_class(self):
        print("这是类前置条件")

    def teardown_class(self):
        print("这是类后置条件")

    def setup_method(self):
        print("这是方法前置条件")

    def teardown_method(self):
        print("这是方法后置条件")

    @allure.step("不知道这是什么")
    @allure.description("描述")

    @pytest.mark.parametrize("item", Do_excel().read())
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

        assert res["error_code"] == 0
        return res
if __name__ == '__main__':
    pytest.main()
