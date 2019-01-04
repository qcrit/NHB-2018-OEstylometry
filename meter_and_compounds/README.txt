The fundamental data resides in the folder ‘Base data’, which contains four files:

A) calgary_proce_x.txt — the Old English verse corpus
B) cynewulf.txt - the titles of Cynewulfian and attributed-Cynewulfian poems under examination
C) unique_compounds.txt — the list of all nominal compounds

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


(PART 1)

- The code ‘compound_freq.py’ can be called in Terminal with the syntax

python compound_freq.py unique_compounds.txt calgary_proce_x.txt

Its output, ‘compfreq.txt’, simply gives the number of instances of a given compound word in the verse corpus. The histogram of this data is plotted in Supplementary Figure 3. For instance, using the following command

sed 's/[^0-9]*//g' compfreq.txt > hist.txt

will remove the actual compounds, and the resulting numerical string (in ‘hist.txt’) can be entered into any program one prefers to draw histograms (eg Matlab)



#

(PART 2)

- The code ‘isolate_compounds.py’ can be run with the following syntax:

python isolate_compounds.py unique_compounds.txt calgary_proce_x.txt

and its output ‘onlycompounds.txt’ simply flags the location of compound words (by line number) in each poem. So now we know where the compounds live. In order to recreate Figure 2c and Supplementary Figure 4, we therefore simply combine INFORMATION 1, which lives in the file ‘compfreq.txt’ created above, with ‘onlycompounds.txt’. 

This combination can be done in many ways. For instance:
I) use the command:     grep '\b1\b' compfreq.txt | awk '{print $1}' > hapax.txt    ,
which creates a file indexing only hapax compounds (which can be checked by running the command again without    | awk '{print $1}'
II) protect the titles of the poems:   awk -F'[{}]' '{print $2}' onlycompounds.txt | grep -v "^[[:space:]]*$" > titles.txt  
III) Combine protected hapax compounds and titles:   cat hapax.txt titles.txt > keep.txt
IV) use the command:    grep -f keep.txt onlycompounds.txt > onlyhap.txt 

The resulting file ('onlyhap.txt') will include the line numbers of hapax compounds in all the poems. Plotting these for any poems of interest generate Figs S4 and 2c. If the reader does not wish to manually copy/write these numbers, the poem of interest can be put in a separate file (say, 'mypoem.txt') and the command 

sed 's/[^0-9]*//g' mypoem.txt > linenums.txt

will leave the bare line numbers. 


####
TL;DR version:
$python isolate_compounds.py unique_compounds.txt calgary_proce_x.txt
$grep '\b1\b' compfreq.txt | awk '{print $1}' > hapax.txt
$awk -F'[{}]' '{print $2}' onlycompounds.txt | grep -v "^[[:space:]]*$" > titles.txt
$cat hapax.txt titles.txt > keep.txt
$grep -f keep.txt onlycompounds.txt > onlyhap.txt

At this juncture, pick poem of choice and separate into a different .txt file, say 'mypoem.txt'

$sed 's/[^0-9]*//g' mypoem.txt > linenums.txt
####



#

(PART 3)

-The code ‘comp_by_poem.py’ can be called in Terminal with the following syntax:

python comp_by_poem.py unique_compounds.txt calgary_proce_x.txt

Its output, ‘comploc.txt’, is the dual to ‘onlycompounds.txt’ from above; instead of having, for each poem, the line number of compound words, it keeps the list of compound words in order but instead indicates which poem they appear in. We can clean up the output with the following regex commands: 

sed 's/[][]//g' comploc.txt | sed 's/[{}]//g' | sed s/"'"/" "/g > comploc_clean.txt

- Next, the code ‘Cynewulf.py’ can be called in Terminal with the syntax

python Cynewulf.py comploc_clean.txt cynewulf.txt

whose output we should also clean up:

sed s/"''"/""/g cynewulfcomps.txt | sed s/"','"/""/g | sed s/","/""/g > cynewulfcomps_clean.txt

These can then be searched for individual pairs with simple regex commands, such as:

grep 'beowulf1' cynewulfcomps_clean.txt | grep 'beowulf2' > SharedBeowulf.txt

which will isolate all compounds shared between the two poems. NOTE that we are counting shared compound words, and not their frequencies; for instance, the rather rare compound "beahhord" (meaning "ring-hoard") occurs only in Beowulf; twice in the first partition, and once in the second. This counts as *one* shared compound between the two partitions, not two.

Adding '-c' after the *second* 'grep' command in the above will give purely the number shared. However, keep in mind that in Figure 3 of the paper the compounds middangeard, heofoncyning, wuldorcyning, and heofonrice (which are very frequently but not always shared between poems, especially known Cynewulfian ones) were not included, so using '-c' without checking for these might give (very) slight discrepancies with the main figure, especially when examining relationships between shorter poems (e.g. Fates, Phoenix). 

The numbers output here, divided by the corresponding number in the prior (see next section, "Matlab code") give the radius of the circle in Figure 3, with the dotted circle indicating a radius of 1, meaning there were just as many shared compounds as predicted by the naive prior. 

###
TL;DR version:
$ python comp_by_poem.py unique_compounds.txt calgary_proce_x.txt
$ sed 's/[][]//g' comploc.txt | sed 's/[{}]//g' | sed s/"'"/" "/g > comploc_clean.txt
$ python Cynewulf.py comploc_clean.txt cynewulf.txt
$ sed s/"''"/""/g cynewulfcomps.txt | sed s/"','"/""/g | sed s/","/""/g > cynewulfcomps_clean.txt

First circle in Figure 3, for instance:

(in MATLAB): $ OECompClustNHB.m
$ grep 'christii' cynewulfcomps_clean.txt | grep -c 'elene'

Divide output of last line (minus 2, since 2 of our excluded compounds appear in this particular example) by first cell in 'Compounds_Plotted.csv' -- this gives the size of the first colored circle relative to the black dotted circle. Repeating for all desired pairs gives relative sizes of colored circles compared to black dotted circle. 
###


Matlab code
——
—————
The folder ‘Matlab code’ contains two files relevant to Figure 3. ‘OEdat_by_comp.mat’ contains a numbered list of all the compound words (not named) and their frequency in the corpus as well as the number of compounds in each poem and their name. The MATLAB script 'OECompClustNHB.m' uses this information to generate two files: 'Compound_Prior.csv', a 243 x 243 upper-triangular file indicating the expected number of shared compound words between pairs of poems in the order given by 'names' in 'OEdat_by_comp.mat' (while there are more than 243 poems in the corpus, many contain 0 compound words and have therefore been excluded); and 'Compound_Plotted.csv', which simply extracts the pairs from 'Compound_Prior.csv' which were plotted in Figure 3, in the order of columns (e.g. the numbers correspond to the expected compounds shared by: Christ-Elene, Christ-Fates, Christ-Juliana, ..., Elene-Fates, Elene-Juliana, ..., Fates-Juliana, ... Juliana-Andreas,... Phoenix-Beowulf, Beowulf-Beowulf. Note that the MATLAB file can take approximately 10-30 minutes to complete. 

The size of the circle in Figure 3 is given by dividing the number of shared compounds actually found in (PART 3) above by the number given in the prior, normalized on the size of the dotted-black-line circle. For instance, the size of the very first circle, comparing Christ II to Elene, is given by the output of the command: 

grep 'christii' cynewulfcomps_clean.txt | grep -c 'elene'

divided by the first cell of 'Compound_Plotted.csv'. The number should be close to 9/9.4 (approximately 1), so the first colored circle in Fig. 3 should be very close to the size of the black dotted circle. 


###

The final file, ‘BeoMeter.mat’, contains the half-lines of incidence of various Sievers metrical types employed in Fig. 2B. These were based on a mapping of a more advanced system of scansion, due to Geoffrey Russom, onto the Sievers system, and were a gift of Dr. Russom. Out of respect for his work and intellectual property we have elected to simply present the Sievers variations. Any questions on scans should be directed to Dr. Russom. 