#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 23:13
# @Author  : yuzhenyu
# @File    : operate_file.py


def file():
    with open("lianxi\config\data.txt", "r",encoding="utf-8") as f:
        print(f.read())

file()
