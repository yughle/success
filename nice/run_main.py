#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/6/29 19:23 
# filename: run_main.py
# development_tool： PyCharm

import HTMLtestrunner_cn,unittest,os

file=os.path.dirname(os.path.abspath(__file__))
suite=unittest.defaultTestLoader.discover(file+"\Case",pattern="test*.py")

if __name__ == '__main__':
    fp_file=os.path.join(file,"report\接口测试.html")
    fp=open(fp_file,"wb")
    runner=HTMLtestrunner_cn.HTMLTestRunner(stream=fp,title="接口测试",description="接口测试内容")
    runner.run(suite)
