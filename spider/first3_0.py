#coding:utf-8


import requests

numbers=0
url='http://www.heibanke.com/lesson/crawler_ex02/'
loops=0
while True and loops<=30:
        loops+= 1
        params1 = {'username':'test','password':'test123'}
        params2 = {'username':'1','password':}
        r = requests.get(url)
        current_cookie=r.cookies['csrftoken']
        r2 = requests.get(r.url,data=params,cookies=params)
        if u'密码错误' in r2.text:
                numbers+= 1
        else:
                print r2.text,numbers
                break        
