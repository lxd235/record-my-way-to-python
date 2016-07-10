#coding:utf-8

from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = 'http://www.heibanke.com/accounts/login/?next=/lesson/crawler_ex02/'
driver = webdriver.Firefox()
time.sleep(3)

driver.get(url)
driver.find_element_by_id('id_username').send_keys('test')
driver.find_element_by_id('id_password').send_keys('test123')
driver.find_element_by_id('id_submit').click()

loops=1
num=0
while True and loops<=30:
        loops+=1
        url1='http://www.heibanke.com/lesson/crawler_ex02/'

        driver.get(url1)
        time.sleep(1)
        driver.find_element_by_name('username').send_keys('test')
        driver.find_element_by_name('password').send_keys(num)
        driver.find_element_by_id('id_submit').click()

        html = driver.page_source
        bs_obj = BeautifulSoup(html,'html.parser')
        #文中含有中文一定要在头一行声明编码方式
        if u'密码错误' in bs_obj.text:
                num+=1
                print u'密码错误'
        else:
                print bs_obj.text
                print num
                break
       
time.sleep(5)
driver.close()



