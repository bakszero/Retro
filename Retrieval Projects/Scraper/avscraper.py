from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd 

link = "https://www.analyticsvidhya.com/glossary-of-common-statistics-and-machine-learning-terms/"

page = urlopen(link)

#Make the soup
soup = BeautifulSoup(page, 'html.parser')

for link in soup.find_all('a'):
    pass
    #print (link.get('href'))

#print (soup.get_text())

all_tables = soup.find_all('table')
#print (all_tables[1].prettify())
#list for gloss
gloss = []


for right_table in all_tables:
    #print (right_table.name)
    #print (body.get_text())
    for rows in right_table.find_all('tr')[1:]:
        for data in rows.find_all('td')[0:1]:
            #print (data)
            if len(data) >=1:
                final = data.find('strong')
                #print(final)
                if final is not None:
                    gloss.append (final.find(text=True))
                    
                    


for item in gloss:
    print (item)
print (len(gloss))