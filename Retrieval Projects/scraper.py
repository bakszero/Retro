from urllib.request import urlopen
from bs4 import BeautifulSoup

link = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = urlopen(link)


soup = BeautifulSoup(page, "lxml")

#print (soup.prettify())

#All links
'''
all_links = soup.find_all("a")

for link in all_links:
    print (link.get("href"))
    '''

#Find all tables

right_table = soup.find('table', class_='wikitable sortable plainrowheaders')

#print (right_table)

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states = row.findAll("th") #TO STORE 2nd column data

    if len(cells) == 6:
        a.append(cells[0].find(text=True))
        b.append(states[0].find(text=True))

        c.append(cells[1].find(text=True))
        d.append(cells[2].find(text=True))
        e.append(cells[3].find(text=True))
        f.append(cells[4].find(text=True))
        g.append(cells[5].find(text=True))


import pandas as pd 

df  = pd.DataFrame(a, columns=['Number'])
df['State/UT'] =b 
df['Admin_capital']=c 
df['Legislative_capital']=d 
df['Judiciary_capital']=e
df['yeaar_capital']=f 
df['Former_capital']=g

df