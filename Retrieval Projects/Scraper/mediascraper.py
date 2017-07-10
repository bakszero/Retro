from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 

link = "http://www.datascienceglossary.org/"

page = urlopen(link)

#Make the soup
soup = BeautifulSoup(page, 'html.parser')

tag_list=[]


big_div = soup.find('div',{"class":'row'})

all_divs = big_div.find_all('div')

for div in all_divs:

        tag = div.find('a')
        tag_list.append(tag.get_text())


for tag in tag_list:
    print (tag)
