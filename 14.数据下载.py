#!/usr/bin/env python
# encoding: utf-8
import os

"""
@author: wenjiaGuo
@version: ??
@contact: 601152819@qq.com
@software: PyCharm
@file: 14.数据下载.py
@time: 2017/10/7 12:17
"""
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
baseUrl = "http://pythonscraping.com"

def getAbsoluteURL(baseUrl,source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://"+source
    else:
        url = baseUrl+"/"+source
    if baseUrl not in url:
        print(baseUrl + url,"不符合要求")
        return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path = absoluteUrl.replace("www.","")
    path = path.replace(baseUrl,"")
    path = downloadDirectory+path
    print(path)
    directory = os.path.dirname(path)

    print(directory)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html,'lxml')
downloadList = bsObj.findAll(src = True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl,download['src'])
    if fileUrl is not None:
        print(fileUrl,"我是fileUrl")
urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))
