#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 13:47
# @Author  : yuzhenyu
# @File    : common_request.py

from common.operate_logs import Print_log
import requests

log = Print_log()


def api_request(method, url, data, headers=None, cookies=None):
    if method == "get":
        try:
            res = requests.get(url, data, headers=headers, cookies=cookies)
            log.info("get请求成功")
            return res
        except Exception as e:
            log.error("get请求失败 %s"%e)

    elif method == "post":
        try:
            res = requests.post(url, data, headers=headers, cookies=cookies)
            log.info("post请求成功")
            return res
        except Exception as e:
            log.error("post请求失败 %s"%e)

