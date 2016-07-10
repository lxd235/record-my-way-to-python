import urllib
from bs4 import BeautifulSoup
import re
loops=0
current_num=' '
url = 'http://www.heibanke.com/lesson/crawler_ex00/'

while True and loops<=100:
        loops=loops+1
        current_url=url+str(current_num[0])
        html = urllib.urlopen(current_url)
        bs_obj = BeautifulSoup(html,'html.parser')

        num_str = bs_obj.h3.get_text()
        p = r'\d+'
        current_num = re.findall(p,num_str)
        if not current_num:
                break

        print current_num
        print bs_obj.text
