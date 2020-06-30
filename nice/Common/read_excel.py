#!/usr/bin/python3.5.1
# -*- coding= utf-8 -*-
# @Time    : 2020/6/29 22:50
# @Author  : yuzhenyu
# @File    : read_excel.py

import openpyxl, os


class Do_excel:
    def __init__(self):
        self.filepath = os.path.dirname(os.path.realpath(__file__))
        self.file = os.path.join(self.filepath, 'jiekou.xlsx')
        self.data = openpyxl.load_workbook(self.file)
        self.sheet = self.data.get_sheet_names()

    def read(self):
        save_list = []
        for i in range(2, self.sheet.max_row + 1):
            save_dict = {}
            save_dict["case_id"] = self.sheet.cell(i, 1).value
            save_dict["url"] = self.sheet.cell(i, 2).value
            save_dict["method"] = self.sheet.cell(i, 3).value
            save_dict["params"] = self.sheet.cell(i, 4).value
            save_dict["title"] = self.sheet.cell(i, 5).value
            save_list.append(save_dict)
        return save_list

    def write_back(self, case_id, value, result):
        self.sheet.cell(case_id, 6).value = value
        self.sheet.cell(case_id, 7).value = result
        self.data.save(self.file)
