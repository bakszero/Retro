import nltk
import re
import string

from graph import *

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



stop_words = (set(stopwords.words('english')))

#Union operation on sets
stop_words = stop_words | {",",".",";","(",")","'","?"}

#print (stop_words)


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
    xsent = [w for w in word_tokens if not w in stop_words ]
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

flat_list = [item for sublist in lemm_sent for item in sublist]
#print (flat_list)
#Create the sentence graph
word_graph = Graph()
#Find the no. of matchings and add to graph as weight

#set sliding window size
#sliding_size = 2
print ((flat_list))
#Iterate and form the word graph, increase weight when more than 1 word encountered
for i in range(0,len(flat_list)-1):
    if flat_list[i] in word_graph.vertList:
        if flat_list[i+1] in word_graph.vertList[flat_list[i]].connectedto.keys():
            #print (word_graph.vertList[flat_list[i]].connectedto)
            word_graph.vertList[flat_list[i]].connectedto[flat_list[i+1]]+=1
        else:
            word_graph.addEdge(flat_list[i], flat_list[i+1], 1)

            
    else:
        word_graph.addEdge(flat_list[i], flat_list[i+1], 1)


#print (word_graph.vertList['stupid'].connectedto)
#print (word_graph.vertList)
for i in word_graph.vertList.values():
    for j, val in i.connectedto.items():
        print ("{0} --> {1} --> {2}".format(i.getID(), j, val))


