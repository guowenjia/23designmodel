#!/usr/bin/env python
# encoding: utf-8
import os
import random
"""
@author: wenjiaGuo
@version: ??
@contact: 601152819@qq.com
@software: PyCharm
@file: 14.数据清洗.py
@time: 2017/10/7 16:06
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
def ngrams(input,n):
    input = input.split(" ")
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output
html = urlopen("http://en.wikipedia.org/wiki/python_(programming_language)")
bsObj = BeautifulSoup(html,"lxml")
content = bsObj.find("div",{"id":"mw-content-text"}).get_text()
print(content)
ngrams = ngrams(content,2)
# print(ngrams)
# print("2-grams count is:"+str(len(ngrams)))
