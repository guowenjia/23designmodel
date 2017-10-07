#!/usr/bin/env python
# encoding: utf-8
import os
##递归1000次可能就停止了。前面的递归程序可能因此而崩溃。
"""
@author: wenjiaGuo
@version: ??
@contact: 601152819@qq.com
@software: PyCharm
@file: 7.去重.py
@time: 2017/10/5 20:38
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
pages = set()
def getlinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(html,'lxml')
    for link in bsObj.findAll('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getlinks(newPage)
getlinks("")