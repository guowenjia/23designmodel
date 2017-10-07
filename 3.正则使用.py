#!/usr/bin/env python
# encoding: utf-8
import os

"""
@author: wenjiaGuo
@version: ??
@contact: 601152819@qq.com
@software: PyCharm
@file: 3.正则使用.py
@time: 2017/10/5 19:34
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,'lxml')
images = bsObj.findAll('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    print(image['src'])

