#!/usr/bin/env python
# encoding: utf-8
import os

"""
@author: wenjiaGuo
@version: ??
@contact: 601152819@qq.com
@software: PyCharm
@file: 8.收集整个网站数据.py
@time: 2017/10/5 20:50
"""

# 如何创建一个爬虫来收集页面标题、正文的第一个段落，
# 以及编辑页面的链接（如果有的话）这些信息。
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
page = set()
def getLinks(pageUrl):
    global page
    html = urlopen('http://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(html,'lxml')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])

    except AttributeError:
        print('缺少一些属性，不过不用担心')
    for link in bsObj.findAll('a',href=re.compile('^(/wiki/)')):
        if 'href'in link.attrs:
            if link.attrs['href'] not in page:
                newPage = link.attrs['href']
                print('---------------\n'+newPage)
                page.add(newPage)
                getLinks(newPage)
getLinks("")
