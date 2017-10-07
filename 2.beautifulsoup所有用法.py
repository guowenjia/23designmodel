#简单的一个举例
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

# 开始深挖
# BeautifulSoup的 find() 和 findAll()
# findAll(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)

#tag，可以传递一个标签的名称或多个标签的名称组成的python列表做列表参数。
#.findAll({"h1","h2","h3","h4","h5","h6"})

#attributes是属性参数。下面的例子红色和绿色。
#.findAll("span", {"class":{"green", "red"}})
#recursive是一个布尔变量，默认是true。
#text是文本参数，用的是标签的文本内容去匹配。

# nameList = bsObj.findAll(text="the prince")
# print(len(nameList))

#还有一个关键词参数keyword。选择具有指定属性的标签。
allText = bsObj.findAll(id="text")
print(allText[0].get_text())