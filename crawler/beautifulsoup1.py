#!/usr/bin/python
#coding:utf-8
# http://python.jobbole.com/81349/

import requests
import urllib2
# import numpy as np
# import pandas as pd
# import json
# import time
from bs4 import BeautifulSoup
# import jieba as jb
# import jieba.analyse
# import sys
# reload(sys)

url = "http://400.haodf.com/index/search?diseasename=&province=&facultyname=&hosfaculty=&hospitalname=&nowpage="
send_headers = {
 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0',
 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
 'Connection':'keep-alive'
}
# for x in range(1,6):
#     pageUrl = url + str(x)
#     print pageUrl + "\n"
html = ''
request = urllib2.Request(url,headers=send_headers)
try:
    response = urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    html = response.read()
    # print html
if html == '':
    exit(886)

soup = BeautifulSoup(html, "html.parser")
# print soup
# print soup.a
# print soup.a.attrs,soup.a.string
# print soup.name
# print soup.head.name
# print soup.head.contents[1]
# print soup.head.children  #是一个 list 生成器对象
spaceHtmlList = soup.find_all('div',attrs={'class':'clearfix showResult-cell bb pb10 mt15'})
for spaceHtml in spaceHtmlList:
    print spaceHtml,"\n"