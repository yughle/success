#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： yuzhenyu
# datetime： 2020/7/2 11:49 
# filename: read_config.py
# development_tool： PyCharm

import configparser,os

def read():
    filename=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file=os.path.join(filename,"Config\config.ini")
    config=configparser.ConfigParser()
    config.read(file,encoding="utf-8")
