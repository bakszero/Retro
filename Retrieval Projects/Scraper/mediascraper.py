from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 

link = "http://alumni.media.mit.edu/~tpminka/statlearn/glossary/"

page = urlopen(link)

#Make the soup
soup = BeautifulSoup(page, 'html.parser')

tag_list=[]


frame = soup.find('frame',{"name":'contents'})

print (frame.find_all('html'))

ul_tags = body.find_all('ul')
#print (ul_tags)
for ul_tag in ul_tags:
    print (ul_tag.prettify())
    li_tags = ul_tag.find_all('li')

    for li_tag in li_tags:
        a_tag = li_tag.find('a')

        if a_tag is not None:
            tag_list.append(a_tag.get_text())


print (tag_list)