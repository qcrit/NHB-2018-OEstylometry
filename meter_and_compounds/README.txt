The fundamental data resides in the folder ‘Base data’, which contains four files:

A) calgary_proce_x.txt — the Old English verse corpus
B) cynewulf.txt - the titles of Cynewulfian and attributed-Cynewulfian poems under examination
C) unique_compounds.txt — the list of all nominal compounds
D) unique_compounds_nowhite.txt — the same as above with all whitespace removed. 

Item (C), the list of all nominal compounds, is obtained from the Bosworth-Toller dictionary by manipulating regular expression commands. I demonstrate how this can be done from scratch in the folder ‘Dictionary’, which has its own README file. However, since that process can be a bit tedious, I have included the list of compounds I used in the study as a ‘base’ file as well

From this data, the following information needs to be extracted in order to recreate the figures shown in the paper: 

1) Histogram of compound frequencies (Supplementary Figure 3)
2) Hapax compounds and their poems/lines of occurrence (Figure 2c, Supplementary Figure 4)
3) The number of compounds shared between (pseudo)Cynewulfian poems (Figure 3). 

The associated Python code extracts this information, as described below. To recreate Figure 3 we will also need a Matlab script which draws data from the random prior discussed in the paper. 

Python codes
—————
———————
All Python codes are found in the folder ‘Python code’. However, in order for them to work properly, the codes and the files from ‘Base data’ discussed above must live in the same folder. 

(PART/INFORMATION 1)

- The code ‘compound_freq.py’ can be called in Terminal with the syntax

python compound_freq.py unique_compounds.txt calgary_proce_x.txt

Its output, ‘compfreq.txt’, simply gives the number of instances of a given compound word in the verse corpus. The histogram of this data is plotted in Supplementary Figure 3. For instance, using the following command

sed 's/[^0-9]*//g' compfreq.txt > hist.txt

will remove the actual compounds, and the resulting numerical string (in ‘hist.txt’) can be entered into any program one prefers to draw histograms (eg Matlab)

#

(PART/INFORMATION 2)

- The code ‘isolate_compounds.py’ can be run with the following syntax:

python isolate_compounds.py unique_compounds_nowhite.txt calgary_proce_x.txt

and its output ‘onlycompounds.txt’ simply flags the location of compound words (by line number) in each poem. So now we know where the compounds live. In order to recreate Figure 2c and Supplementary Figure 4, we therefore simply combine INFORMATION 1, which lives in the file ‘compfreq.txt’ created above, with ‘onlycompounds.txt’. 

This combination can be done in many such ways. For instance:
I) use the command grep -E ' 1' compfreq.txt > hapax.txt
II) check this file by eye to make sure only hapax words (i.e. those with frequency 1 and not 10 etc) are included
III) use command+F to remove the 1’s
IV) use the command grep  -f hapax.txt Compounds_master.txt > onlyhap.txt 

The resulting file will include the line numbers of hapax compounds (one may, perhaps, need to put the titles of the poems back in; at any rate Beowulf is the first poem and the only one plotted in the main text) 

#

(PART/INFORMATION 3)

-The code ‘comp_by_poem.py’ can be called in Terminal with the following syntax:

python comp_by_poem.py unique_compounds.txt calgary_proce_x.txt

Its output, ‘comploc.txt’, is the dual to ‘onlycompounds.txt’ from above; instead of having, for each poem, the line number of compound words, it keeps the list of compound words in order but instead indicates which poem they appear in. I made an alternative version ‘comploc_clean.txt’ by opening ‘comploc.txt’ and using Command+F to find and replace the following garbage:

[unknown]
[verse’
the delimiters {,}[,],’ (but not the comma itself!)

- Next, the code ‘Cynewulf.py’ can be called in Terminal with the syntax

python compound_freq.py comploc_clean.txt cynewulf.txt

Its output, ‘cynewulfcomps.txt’, gives the list of compound words shared between (pseudo)Cynewulfian works. This is what will generate, in Figure 3, the number of shared compounds for any two such poems, which we will divide by the naive prior’s prediction of how many those two poems should share in order to get the size of the circle. There is no code written for this; I simply counted by hand. For instance, the first entry (should be)

['þinggemearces', 'andreas', 'elene'] 

for which I would add one stroke under the column Andreas-Elene shared compounds in my notes. Note that if a compound appears multiple times in one of the two compared poems I do not count it more than once; i.e. the third entry (should be)

['wundorcræfte', 'andreas', 'andreas', 'thefatesoftheapostles', 'juliana', 'rid40'] 

for which I add one Andreas-Juliana shared compound and one Andreas-Fates shared compound, not 2. 

Matlab code
——
—————
The folder ‘Matlab code’ contains two files relevant to Figure 3. ‘OEdat_by_comp.mat’ contains a numbered list of all the compound words (not named) and their frequency in the corpus as well as some accessory data. The actual script, ‘OECompClust2.m’, uses this data to create one realization of the naive prior, and has only one output, ‘pair’, which indicates for any two poems how many compounds they had in common in that realization of the prior. The names of the two poems being compared in any cell of ‘pair’ can be found by opening ‘OEdat_by_comp.mat’ and examining the table ‘pairwise’ which gives the names of the two poems corresponding to the number of mutual compounds assigned in ‘pair’. Running ‘OECompClust2.m’ many thousands of times and averaging the results gives the size of the naive prior (dotted circle in Figure 3) for any two poems. 

The final file, ‘BeoMeter.mat’, contains the half-lines of incidence of various Sievers metrical types employed in Fig. 2B. These were based on a mapping of a more advanced system of scansion, due to Geoffrey Russom, onto the Sievers system, and were a gift of Dr. Russom. Out of respect for his work and intellectual property we have elected to simply present the Sievers variations. Any questions on scans should be directed to Dr. Russom. 