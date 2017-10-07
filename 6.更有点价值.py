#!/usr/bin/env python
# encoding: utf-8
import os

"""
@author: wenjiaGuo
@version: ??
@contact: 601152819@qq.com
@software: PyCharm
@file: 6.更有点价值.py
@time: 2017/10/5 20:19
"""

##当然，写程序来找出这个静态的维基百科词条里所有的词条链接很有趣，不过没什么实际
#用处。我们需要让这段程序更像下面的形式。
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime
# 程序首先做的是用系统当前时间生成一个随机数生成器。这样
# 可以保证在每次程序运行的时候，维基百科词条的选择都是一个全新的随机路径。
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,'lxml')
    return bsObj.find('div',{'id':'bodyContent'}).findAll(
        'a',href=re.compile("^(/wiki/)((?!:).)*$")
    )
links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArtitle = links[random.randint(0,len(links)-1)].attrs['href']
    print(newArtitle)

    links = getLinks(newArtitle)

