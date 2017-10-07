# #!/usr/bin/env python
# # encoding: utf-8
# import os
#
# """
# @author: wenjiaGuo
# @version: ??
# @contact: 601152819@qq.com
# @software: PyCharm
# @file: 9.外链跳外链1.py
# @time: 2017/10/6 12:13
# """
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# import datetime
# import random
#
# pages = set()
# random.seed(datetime.datetime.now())
#
# #获取页面内所有内链的列表
# #这里面的bsObj就是页面的对象文件，includeUrl就是包含的文件
# def getInternalLinks(bsObj,includeUrl):
#     internalLinks = []
#     #找出所有以"/"开头的链接
#     for link in bsObj.findAll('a',
#         href = re.compile('^(/|.*'+includeUrl+')')):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in internalLinks:
#                 internalLinks.append(link.attrs['href'])
#     return internalLinks
#
# #获取页面内所有外链的列表
# def getExternalLinks(bsObj,excludeUrl):
#     externalLinks = []
#     #找出所有以"http"或"www"开头且不包含当前URL的链接
#     for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in externalLinks:
#                 externalLinks.append(link.attrs['href'])
#     return externalLinks
#
# #对字符串进行分离。把前面的http去掉
# def splitAddress(address):
#     addressParts = address.replace('http://','').split('/')
#     return addressParts
#
# #比较综合的调用程序
# def getRandomExternalLink(startingPage):
#     html = urlopen(startingPage)
#     bsObj = BeautifulSoup(html,"lxml")
#     externalLinks = getExternalLinks(bsObj,splitAddress(startingPage)[0])
#     if len(externalLinks) == 0:
#         internalLinks = getInternalLinks(startingPage)
#         return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
#     else:
#         return externalLinks[random.randint(0,len(externalLinks)-1)]
# def followExternalOnly(startingSite):
#     externalLink = getRandomExternalLink('http://oreilly.com')
#     print('随机外链是'+externalLink)
#     followExternalOnly(externalLink)
# followExternalOnly('http://oreilly.com')


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())


# Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# Retrieves a list of all external links found on a page
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # Finds all links that start with "http" or "www" that do
    # not contain the current URL
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(bsObj,startingPage)
        return internalLinks[random.randint(0, len(internalLinks) - 1)]
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)

allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html,'lxml')
    internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks :
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取的链接的URL是:"+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)

#getAllExternalLinks('http://oreilly.com")
followExternalOnly("http://oreilly.com")

