from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 



link = "http://wiki.fast.ai/index.php/Deep_Learning_Glossary"

page = urlopen(link)

#Make the soup
soup = BeautifulSoup(page, 'html.parser')

tag_list=[]


big_div = soup.find('div',{"id":'mw-content-text'})

all_h = big_div.find_all('h3')
for h in all_h:
    span_tag = h.find('span')

    if span_tag is not None:
        tag_list.append(span_tag.get_text()) 



for tag in tag_list:
    print (tag)

