from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 

link = "http://data-informed.com/glossary-of-big-data-terms/"

page = urlopen(link)

#Make the soup
soup = BeautifulSoup(page, 'html.parser')

tag_list=[]


big_div = soup.find('div',{"class":'entry'})

all_p = big_div.find_all('p')
for p in all_p:
    strong_tag = p.find('strong')

    if strong_tag is not None:
        tag_list.append(strong_tag.get_text()) 



for tag in tag_list:
    print (tag)
