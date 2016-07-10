#coding:utf-8


import requests

numbers=0
url='http://www.heibanke.com/lesson/crawler_ex01/'
while numbers<=30:

        params={'username':'1','password':str(numbers)}
        r = requests.post(url,data=params)

        if u'密码错误' in r.text:
                numbers+=1
        else:
                print numbers
                print r.text
                break        