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

    def output_logs(self, level, message):
        # 输出到控制台
        self.consle = logging.StreamHandler()
        self.consle.setLevel(logging.DEBUG)
        self.consle.setFormatter(self.formatter)
        self.logger.addHandler(self.consle)
        # 写入文本里
        self.file_hander = logging.FileHandler(self.file)
        self.file_hander.setLevel(logging.DEBUG)
        self.file_hander.setFormatter(self.formatter)
        self.logger.addHandler(self.file_hander)

        if level == "debug":
            self.logger.debug(message)
        elif level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        # 防止日志重复输出
        self.logger.removeHandler(self.consle)
        self.logger.removeHandler(self.file_hander)
        self.file_hander.close()

    def debug(self, message):
        self.output_logs("debug", message)

    def info(self, message):
        self.output_logs("info", message)

    def warning(self, message):
        self.output_logs("warning", message)

    def error(self, message):
        self.output_logs("error", message)


if __name__ == '__main__':
    log=Log()
    log.debug("hjkhkj")
    log.info("dsd")
    log.warning("dfd")
    log.error("hjkhjk")