#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 15:00
# @Author  : yuzhenyu
# @File    : openate_config.py

import configparser
import os


def read_config():
    file=os.path.dirname(
        os.path.dirname(
        os.path.abspath(__file__)
    )
    )
    file_name=os.path.join(file,"config\\request_api.ini")
    con=configparser.ConfigParser()
    con.read(file_name,encoding="utf-8")
    sections=con.sections()


