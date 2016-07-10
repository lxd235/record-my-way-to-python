#coding:utf-8


import requests

def post_data_django(s, url, data):

        s.get(url)

        params = dict(csrfmiddlewaretoken=s.cookies.get('csrftoken'))
        params.update(data)

        r=s.post(url,data=params)

        return r,s


url='http://www.heibanke.com/lesson/crawler_ex02/'
url_login = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'

s=requests.session()
s.get(url_login)
params=dict(username='test',password='test123',csrfmiddlewaretoken=s.cookies.get('csrftoken'))
s.post(url_login,data=params)
num=0
while num<=30:
        r,s=post_data_django(s, url, {'username':'1','password':str(num)})
        if u'密码错误' in r.text:
                print u'密码错误',num
                num+=1
        else:
                print r.text,num
                break       