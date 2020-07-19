#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 14:02
# @Author  : yuzhenyu
# @File    : testing_unittest.py


from common.read_excel import Excel
from common.operate_logs import Print_log
from common.common_request import api_request
import unittest
import ddt



@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data(*Excel().read())

    def test_1(self,item):
        url,data,sheetname = item["url"], eval(item["data"]), item["sheet_name"]
        caseid,method = item["case_id"], item["method"]
        res=api_request(item["method"], url, data)
        Excel().write_back(
            sheetname,caseid+1,res.status_code, str(res.json())
        )
        self.assertEqual(res.json()["error_code"] , 0)


if __name__ == '__main__':
    unittest.main()
