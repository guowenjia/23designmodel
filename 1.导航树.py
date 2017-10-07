#!/usr/bin/env python
# encoding: utf-8
import os

"""
@author: wenjiaGuo
@version: 3.5.3
@contact: 601152819@qq.com
@software: PyCharm
@file: 1.处理兄弟标签.py
@time: 2017/10/5 13:34
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,'lxml')
for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:#next_siblings就是跳过第一行表格标题。
    print(sibling)