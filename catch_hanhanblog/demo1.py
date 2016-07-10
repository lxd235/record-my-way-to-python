#-*-coding:utf-8*-*
import urllib
import requests
from bs4 import BeautifulSoup


url='http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'

html=urllib.urlopen(url).read()

bs_obj=BeautifulSoup(html,'html.parser')
print bs_obj
