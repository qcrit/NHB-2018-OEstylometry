# character_ngrams.py
# functional trigram frequencies

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

esBigrams = ngrams(text, 3)
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
    c1.append(a[x].count('eor'))
    c2.append(a[x].count('and'))
    c3.append(a[x].count('eal'))
    c4.append(a[x].count('ear'))
    c5.append(a[x].count('ond'))
    c6.append(a[x].count('þæt'))
    c7.append(a[x].count('nde'))
    c8.append(a[x].count('for'))
    c9.append(a[x].count('end'))
    c10.append(a[x].count('nne'))
    c11.append(a[x].count('ges'))
    c12.append(a[x].count('iht'))
    c13.append(a[x].count('hte'))
    c14.append(a[x].count('ode'))
    c15.append(a[x].count('lde'))
    c16.append(a[x].count('ald'))
    c17.append(a[x].count('sce'))
    c18.append(a[x].count('gen'))
    c19.append(a[x].count('him'))
    c20.append(a[x].count('heo'))
    c21.append(a[x].count('ste'))
    c22.append(a[x].count('tan'))
    c23.append(a[x].count('dan'))
    c24.append(a[x].count('cea'))
    c25.append(a[x].count('þon'))
    c26.append(a[x].count('gan'))
    c27.append(a[x].count('swa'))
    c28.append(a[x].count('nge'))
    c29.append(a[x].count('lle'))
    c30.append(a[x].count('god'))
    c31.append(len(a[x]) - a[x].count(' '))

results = np.column_stack((c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30, c31))
np.savetxt('results.csv', results, delimiter=',')




