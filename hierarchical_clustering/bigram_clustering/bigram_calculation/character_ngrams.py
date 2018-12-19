# character_ngrams.py
# functional bigram frequencies

import nltk, re, string, collections
from nltk.util import ngrams

import csv

import numpy as np
import re

# load file
with open("calgary_proce_alt.txt", "r") as file:
    text = file.read()

# alternate unprocessed copy
text2 = text

# get rid of all the XML markup
text = re.sub('<.*>','',text)


# get rid of punctuation
punctuationNoPeriod = "[" + re.sub("\.","",string.punctuation) + "]"
text = re.sub(punctuationNoPeriod, "", text)

tokenized = text.split('{')
tokenized2 = text.split(' ')

esBigrams = ngrams(text, 2)
# get the frequency of each bigram in our corpus
esBigramFreq = collections.Counter(esBigrams)

# what are the most common ngrams?
#print(esBigramFreq.most_common(1000))

# write initial file
f = open('initial_list.txt', 'w')
for t in esBigramFreq.most_common(1000):
    f.write(' '.join(str(s) for s in t) + '\n')
f.close()

# use grep for additional text processing (to remove ngrams that contain spaces)
# grep -vwE "((' '|' '))" initial_list.txt > final_list.txt

a = text2.split('{')

c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []
c9 = []
c10 = []
c11 = []
c12 = []
c13 = []
c14 = []
c15 = []
c16= []
c17 = []
c18 = []
c19 = []
c20 = []
c21 = []
c22 = []
c23 = []
c24 = []
c25 = []
c26 = []
c27 = []
c28 = []
c29 = []
c30 = []
c31 = []

for x in range(len(a)):
    c1.append(a[x].count('an'))
    c2.append(a[x].count('on'))
    c3.append(a[x].count('ge'))
    c4.append(a[x].count('ea'))
    c5.append(a[x].count('de'))
    c6.append(a[x].count('eo'))
    c7.append(a[x].count('nd'))
    c8.append(a[x].count('ne'))
    c9.append(a[x].count('or'))
    c10.append(a[x].count('re'))
    c11.append(a[x].count('en'))
    c12.append(a[x].count('es'))
    c13.append(a[x].count('um'))
    c14.append(a[x].count('te'))
    c15.append(a[x].count('in'))
    c16.append(a[x].count('er'))
    c17.append(a[x].count('le'))
    c18.append(a[x].count('he'))
    c19.append(a[x].count('st'))
    c20.append(a[x].count('we'))
    c21.append(a[x].count('al'))
    c22.append(a[x].count('ce'))
    c23.append(a[x].count('se'))
    c24.append(a[x].count('hi'))
    c25.append(a[x].count('od'))
    c26.append(a[x].count('ar'))
    c27.append(a[x].count('ra'))
    c28.append(a[x].count('ht'))
    c29.append(a[x].count('ld'))
    c30.append(a[x].count('wi'))
    c31.append(len(a[x]) - a[x].count(' '))



results = np.column_stack((c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30, c31))
np.savetxt('results.csv', results, delimiter=',')

#n = 3
#ngrams = [text[i:i+n] for i in range(len(text)-n+1)]
#print (ngrams)

