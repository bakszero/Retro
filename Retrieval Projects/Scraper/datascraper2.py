from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 

#link = "https://deeplearning4j.org/glossary"

#page = urlopen(link)

#Make the soup
soup = BeautifulSoup(open("./deepgloss.html"))

tag_list=[]


big_article = soup.find('article',{"class":'main-content'})

all_h = big_article.find_all('h3')
for h in all_h:
     tag_list.append(h.get('id'))



for tag in tag_list:
    print (tag)
