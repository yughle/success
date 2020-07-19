#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/7/17 13:51 
# filename: operate_logs.py
# development_tool： PyCharm

import logging
import os
import time


class Log:

    def __init__(self):
        file = os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
        self.filename = os.path.join(file, "logs", "%s.logs" % time.strftime("%Y_%M_%D"))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formater = logging.Formatter(
            "[%(asctime)s] %(name)s][%(filename)s:%(lineno)d] [%(levelname)s][%(message)s")

    def output_consle_log(self):
        """
        把日志输出到控制台
        :return:
        """
        self.consle = logging.StreamHandler()
        self.consle.setLevel(logging.DEBUG)
        self.consle.setFormatter(self.formater)
        self.logger.addHandler(self.consle)

    def output_file_log(self):
        """
        把日志写入logs目录里txt文件里
        :return:
        """
        self.file_log = logging.FileHandler(self.filename)
        self.file_log.setLevel(logging.DEBUG)
        self.file_log.setFormatter(self.formater)
        self.logger.addHandler(self.file_log)

    def judge_log(self, level, msg):
        if level == "debug":
            self.logger.debug(msg)
        elif level == "info":
            self.logger.info(msg)
        elif level == "warning":
            self.logger.warning(msg)
        elif level == "error":
            self.logger.error(msg)
        elif level == "critical":
            self.logger.critical(msg)


class Print_log:

    def debug(self,msg):
        Log().judge_log("debug",msg)

    def info(self,msg):
        Log().judge_log("info", msg)

    def warning(self,msg):
        Log().judge_log("warning", msg)

    def error(self,msg):
        Log().judge_log("error", msg)

    def critical(self,msg):
        Log().judge_log("critical", msg)