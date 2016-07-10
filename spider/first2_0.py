#coding:utf-8
import urllib
from bs4 import BeautifulSoup
import re
psword=0
while True:
        
        url='http://www.heibanke.com/lesson/crawler_ex01/'
        params=urllib.urlencode(dict(username=1,password=psword))
        conn=urllib.urlopen(url,params)
        bs_obj = BeautifulSoup(conn,'html.parser')
        a=bs_obj.h3.text.encode('utf-8')
        p=r'\xe9\x94\x99\xe8\xaf\xaf'
        flag=re.findall(p,a)
        if not flag:
                break
        psword+=1        

print bs_obj.text
print '####################' 
print psword