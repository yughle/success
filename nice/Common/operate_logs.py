#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/6/30 17:27 
# filename: operate_logs.py
# development_tool： PyCharm
import logging,os,time

class Log:
    def __init__(self):
        """
        设定日志命名，目录，创建容器盛放日志
        """
        self.filepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+"\logs"
        self.file=os.path.join(self.filepath,"%s.logs"%time.strftime("%Y_%m_%d"))
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')





