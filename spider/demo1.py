#coding:utf-8

import urllib
from bs4 import BeautifulSoup
import re

html = urllib.urlopen('http://baike.baidu.com/link?url=QG0uKPAYeinTQwtSvnZLZCEpujzgJ5eFv6YJb6fvDdq9GxULw2TMoeTSUsoSnLSZLiDDTAaFV76EnheEw7LLLK')
bs_obj = BeautifulSoup(html,'html.parser')
# help(bs_obj.findAll)
# findAll(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs) method of bs4.BeautifulSoup instance
#     Extracts a list of Tag objects that match the given
#     criteria.  You can specify the name of the Tag and any
#     attributes you want the Tag to have.
    
#     The value of a key-value pair in the 'attrs' map can be a
#     string, a list of strings, a regular expression object, or a
#     callable that takes a string and returns whether or not the
#     string matches for some custom definition of 'matches'. The
#     same is true of the tag name.
a_list = bs_obj.findAll('a')
for a in a_list:
    if not a.find('img'):
        if a.attrs.get('href'):
            print a.attrs['href']