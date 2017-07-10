from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 

link = "http://bigdata-madesimple.com/big-data-a-to-zz-a-glossary-of-big-data-terminology/"

page = urlopen(link)

#Make the soup
soup = BeautifulSoup(page, 'html.parser')

tag_list=[]


big_div = soup.find('div',{"class":'ptb60'})

all_p = big_div.find_all('p')
for p in all_p:
    strong_tag = p.find('strong')

    if strong_tag is not None:
        tag_list.append(strong_tag.get_text()) 



for tag in tag_list:
    print (tag)
