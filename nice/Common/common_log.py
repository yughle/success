#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 21:53
# @Author  : yuzhenyu
# @File    : common_log.py
import logging,os


class Log:
    def __init__(self,filename=None):
        if filename is None:
            filename=os.getcwd()
        self.filename=filename
    def log(self):
        formatter = logging.Formatter(
            '[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]''-[process:%(process)s] - %(message)s')
        self.logger=logging.getLogger()
        self.loger_file=logging.FileHandler("日志文本路径")
        fh = logging.handlers.TimedRotatingFileHandler(self.filename, 'D', 1, 30)
        fh.suffix = "%Y%m%d-%H%M.log"
        fh.setLevel(logging.DEBUG)
        #输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.addHandler(fh)
        self.addHandler(ch)








