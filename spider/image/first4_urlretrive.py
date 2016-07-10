import urllib
from bs4 import BeautifulSoup

url = 'http://www.1tu.com/'
html = urllib.urlopen(url)
bs_obj = BeautifulSoup(html,'html.parser')

num=0
for i in bs_obj.findAll('img'):
        num+=1
        print i['src']
        if 'http://' in i['src']:
                urllib.urlretrieve(i['src'],'heibanke_img_'+str(num)+'.'+i['src'][-3:])
        elif '/img/grey.png' in i['src']:
                if 'http://' in i['data-original']:
                        urllib.urlretrieve(i['data-original'],'heibanke_img_'+str(num)+'.'+i['data-original'][-3:])
                else:
                        urllib.urlretrieve(url+i['data-original'],'heibanke_img_'+str(num)+'.'+i['data-original'][-3:])
                                
        else:        
                urllib.urlretrieve(url+i['src'],'heibanke_img_'+str(num)+'.'+i['src'][-3:])        