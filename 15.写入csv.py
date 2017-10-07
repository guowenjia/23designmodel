#!/usr/bin/env python
# encoding: utf-8
import os

"""
@author: wenjiaGuo
@version: ??
@contact: 601152819@qq.com
@software: PyCharm
@file: 15.写入csv.py
@time: 2017/10/7 15:06
"""
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html,"lxml")
table = bsObj.findAll("table",{"class":"wikitable"})[0]
print(table)
rows = table.findAll('tr')
print("___________________________________________",rows)
csvFile = open("editors.csv",'wt',newline="",encoding="utf-8")
writer = csv.writer(csvFile)
try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvFile.close()

