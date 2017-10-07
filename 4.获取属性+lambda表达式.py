#!/usr/bin/env python
# encoding: utf-8
import os

"""
@author: wenjiaGuo
@version: ??
@contact: 601152819@qq.com
@software: PyCharm
@file: 4.获取属性+lambda表达式.py
@time: 2017/10/5 19:42
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html,'lxml')
two = bsObj.findAll(lambda bsObj:len(bsObj.attrs)==2)
for i in two:
    print(i)
    print("-----------------------")
