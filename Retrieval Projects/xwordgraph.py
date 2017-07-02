import nltk

import networkx as nx
from graph import *

from operator import itemgetter
from collections import OrderedDict

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

from collections import Counter




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
    xsent = [w.lower() for w in word_tokens if not w in stop_words ]
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

xword_graph = nx.Graph()

#set sliding window size
#sliding_size = 2
#print ((flat_list))
#Iterate and form the word graph, increase weight when more than 1 word encountered
for i in range(0,len(flat_list)-1):
    if flat_list[i] in list(xword_graph.nodes()):
        if flat_list[i+1] in list(xword_graph.neighbors(flat_list[i])):
            #print (word_graph.vertList[flat_list[i]].connectedto)
            xword_graph[flat_list[i]][flat_list[i+1]]['weight'] +=1
        else:
            xword_graph.add_edge(flat_list[i], flat_list[i+1], weight =1)

            
    else:
        xword_graph.add_edge(flat_list[i], flat_list[i+1], weight = 1)


#nx.draw_networkx(xword_graph,node_color='#A0CBE2',edge_color='#BB0000',width=2,edge_cmap=plt.cm.Blues,with_labels=True)
#plt.xlim(-4.0, 4.0)

#plt.show()

for u, v , a in xword_graph.edges(data=True):
    #print( u, v,a )
    pass

#Compute closeness centrality
cc_dict = nx.closeness_centrality(xword_graph, u=None, distance =None, normalized=True)
sorted_cc_dict =  OrderedDict(sorted(cc_dict.items(), key=itemgetter(1), reverse=True))


#for x, y in sorted_cc_dict.items():
  #  print ("{0} : {1}".format(x, y))


#Compute betweenness centrality
bc_dict= nx.betweenness_centrality(xword_graph, k=None, normalized=True, weight=None, endpoints=False, seed=None)
sorted_bc_dict =  OrderedDict(sorted(bc_dict.items(), key=itemgetter(1), reverse=True))

for x, y in sorted_bc_dict.items():
    pass
    #print ("{0} : {1}".format(x, y))


#BIGRAM IN MACHINE LEARNING

BIGRAM = ngrams(flat_list, 2)

for (a, b) in BIGRAM:
    print ("{0}  :   {1}".format(a,b))
#print (Counter(BIGRAM))