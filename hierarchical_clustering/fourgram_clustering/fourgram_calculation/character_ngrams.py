# character_ngrams.py
# functional fourgram frequencies

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

esBigrams = ngrams(text, 4)
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
    c1.append(a[x].count('eall'))
    c2.append(a[x].count('eald'))
    c3.append(a[x].count('scea'))
    c4.append(a[x].count('ende'))
    c5.append(a[x].count('weor'))
    c6.append(a[x].count('onne'))
    c7.append(a[x].count('riht'))
    c8.append(a[x].count('eard'))
    c9.append(a[x].count('ihte'))
    c10.append(a[x].count('ofer'))
    c11.append(a[x].count('eorð'))
    c12.append(a[x].count('hten'))
    c13.append(a[x].count('þonn'))
    c14.append(a[x].count('wear'))
    c15.append(a[x].count('drih'))
    c16.append(a[x].count('alle'))
    c17.append(a[x].count('alde'))
    c18.append(a[x].count('fæst'))
    c19.append(a[x].count('wylc'))
    c20.append(a[x].count('word'))
    c21.append(a[x].count('unde'))
    c22.append(a[x].count('þuh'))
    c23.append(a[x].count('lice'))
    c24.append(a[x].count('gode'))
    c25.append(a[x].count('eond'))
    c26.append(a[x].count('orht'))
    c27.append(a[x].count('olde'))
    c28.append(a[x].count('ning'))
    c29.append(a[x].count('miht'))
    c30.append(a[x].count('ryht'))
    c31.append(len(a[x]) - a[x].count(' '))




results = np.column_stack((c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30, c31))
np.savetxt('results.csv', results, delimiter=',')

