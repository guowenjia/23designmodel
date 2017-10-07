#!/usr/bin/env python
# encoding: utf-8
import os

"""
@author: wenjiaGuo
@version: ??
@contact: 601152819@qq.com
@software: PyCharm
@file: 5.数据采集.py
@time: 2017/10/5 19:51
"""
## 对维基百科进行一个数据采集
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html,'lxml')
# print(bsObj)
# for link in bsObj.findAll('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
## 这个时候你发现采集到了你想要的一些词条链接，但是还有一些
##你不需要的词条链接，这个时候需要进行一个过滤。
# 如果你仔细观察那些指向词条页面（不是指向其他内容页面）的链接，
# 会发现它们都有三个共同点：
# • 它们都在 id 是 bodyContent 的 div 标签里
# • URL 链接不包含分号
# • URL 链接都以 /wiki/ 开头
# 我们可以利用这些规则稍微调整一下代码来获取词条链接：
for link in bsObj.find('div',{'id':'bodyContent'}).findAll('a',
                                         href=re.compile('^(/wiki/)((?!:).)*$')):
    if "href" in link.attrs:
        print(link.attrs['href'])