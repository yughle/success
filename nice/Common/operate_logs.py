#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/6/30 17:27 
# filename: operate_logs.py
# development_tool： PyCharm
import logging, os, time


class Log:
    def __init__(self):
        """
        设定日志命名，目录，创建容器盛放日志
        """
        self.filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\logs"
        self.file = os.path.join(self.filepath, "%s.logs" % time.strftime("%Y_%m_%d"))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter(
            '%(asctime)s  %(filename)s %(funcName)s %(levelname)s %(message)s')
        # 输出到控制台
        self.consle = logging.StreamHandler()
        self.consle.setFormatter(self.formatter)
        self.logger.addHandler(self.consle)
        # 写入文本里
        self.file_hander = logging.FileHandler(self.file)
        self.file_hander.setFormatter(self.formatter)
        self.logger.addHandler(self.file_hander)

    def get_log(self):
        logging.debug("yuyuyuyu")
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_hander)
        self.file_hander.close()


