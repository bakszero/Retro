import nltk
import re
import string

from graph import *

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



stop_words = (set(stopwords.words('english')))
stop_words.add(".")
stop_words.add(",")
stop_words.add("\"")
stop_words.add(";")
stop_words.add("?")

sentence_array = []
preword_array = []

#Read the file
with open('alpha.txt','r') as f:
    for line in f:
        line = line.strip()
        sentence_array.append(line.strip("\n"))
        for word in line.split():
            preword_array.append(word)



#Clean sentence up so that new sentence contains only strings as a list of cleaned-up sentences.
newsentence_array = []
for line in sentence_array:
    if line == '':
        continue
    newsentence_array.append(line)
#punc = string.punctuation

#preword_array = word_tokenize(preword_array)

setword_array = []


for word in preword_array:
    if not word in setword_array:
        setword_array.append(word)


#print(newsentence_array)

filtered_sent=[]
xsent = []
for line in newsentence_array:
    word_tokens =  word_tokenize(line)
    xsent = [w for w in word_tokens if not w in stop_words]
    filtered_sent.append(xsent)

#print (filtered_sent)
#Cool, stop words removed, now onto lemmatization
wordnet_lemmatizer = WordNetLemmatizer()

lemm_sent= []
temp_sent=[]
for line in filtered_sent:
    for word in line:
        temp_sent.append(wordnet_lemmatizer.lemmatize(word))
    lemm_sent.append(tuple(temp_sent))
    temp_sent=[]

#print (lemm_sent)

#Create the sentence graph
sentence_graph = Graph()
#Find the no. of matchings and add to graph as weight

set_sent = set(lemm_sent[0])

x=1
for line1 in lemm_sent:
    for line2 in lemm_sent[x:]:
        weight = 0
        for word in line1:
            if word in line2:
                weight += 1
        sentence_graph.addEdge(line1, line2, weight)
    x=x+1

#print(sentence_graph.getVertices())

for i in sentence_graph.vertList.values():
    for j, val in i.connectedto.items():
        print("{0} --> {1}---->{2}".format(i.getID(), j, val))