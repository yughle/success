#!/usr/bin/python3.5.1
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 22:50
# @Author  : yuzhenyu
# @File    : read_excel.py

import openpyxl,os

class Do_excel:
    def __init__(self):
        self.filepath=os.path.dirname(os.path.realpath(__file__))
    def read(self):
        self.file=self.filepath+"\jiekou.xlsx"
        data=openpyxl.load_workbook(self.file)
        sheets=data.get_sheet_names()
        save_sheet=[]
