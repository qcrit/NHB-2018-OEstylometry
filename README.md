## Replication code for Neidorf et al., "Large-scale quantitative profiling of the Old English verse tradition," forthcoming in Nature Human Behaviour

The code requires Python 3.6.0+. It is recommended that you create a virtual environment for this project before installing the required packages and running the code. If you have not done so previously, you will need to install virtualenv (e.g., by running `pip install virtualenv`). To create a virtual environment called 'venv_OE_stylometry', type `virtualenv venv_OE_stylometry`. To activate the virtual environment, type `source venv_OE_stylometry/bin/activate` when in the main directory. 

Before running the replication experiments, install the required Python packages, including scipy, numpy, matplotlib, and nltk. 

## Part 1: Corpus-wide functional ngram profiling (Fig. 1 and Supplemental Fig. S2)

To reproduce the ngram results in Fig. 1 and in Supplemental Fig. S2:

1) cd into the 'ngrams' directory. 
2) Type `python3 main.py` in the terminal. 
3) Running this code will generate a summary file ('results_NG.csv') with the key bigram, trigram and four-gram data, as well as three separate .txt with the full raw data for each ngram analysis. The summary file lists the top-five ngrams for each text in the (nonaggregated) corpus. For each ngram, the file gives the text frequency, corpus frequency, aboslute value of the difference between the text and corpus frequency, the running sum of the frequency differences, and the length of the text. Columns B-AE cover bigrams, columns AG-BJ trigrams, and columns BL-CO four-grams. As such, Fig. 1 is a plot of BI vs. BJ, Supplemental Fig. S2A is a plot of AD vs. AE, and Supplemental Fig. S2B is a plot of CN vs. CO. 

## Part 2: Sense-pause analysis (Fig. 2)

To reproduce the sense-pause results in Fig. 2A:

1) cd into the 'sense_pauses' directory. 
2) Run 'python3 main.py arg1 arg2' in the terminal. 
3) Here 'Arg1' should be the name of the directory that contains the texts to be analyzed, and 'Arg2' should be the name of the output file (e.g., to generate the selected data in Fig. 2A run `python3 main.py selected_texts_Fig2A SPresults`. To generate data for the whole (aggregated) corpus use 'Calgary_corpus' as the input folder - this is the raw data for the 'corpus mean' bar in Fig. 2A. 

## Part 3: Hierarchical agglomerative clustering using high-frequency ngrams (Fig. 4 and Supplemental Fig. S5)

To reproduce the dendrogram in Fig. 4:

1) cd into the 'hierarchical_clustering/trigram_clustering/clustering' subdirectory. 
2) Run `python3 hierarchical_ngram_clustering.py` in the terminal. 

N.B.: 'Results1.xlsx' contains all of the input data required for clustering - 'results' contains the raw ngram counts, 'Sheet1' the length-normalized frequencies, and 'Sheet2' the rescaled data (min -1, max 1). 

To regenerate the raw trigram input data:

1) cd into the 'hierarchical_clustering/trigram_clustering/trigram_calculation' directory. 
2) Type `python3 character_ngrams.py` in the terminal. 
3) This will calculate the frequencies of the 30 most common ngrams in each text in the (modified nonaggregated) corpus and print them to 'results.xlsx'.
4) To prepare the data for clustering, the following preprocessing steps are required. i) Sort the texts by length (i.e., by column AE). ii) Delete everything below row 50 (i.e., retain only the five longest texts). iii) Rescale the frequencies to min -1 and max 1. These three steps will yield the final input data required (i.e., Sheet2 of 'results1.xlsx' in 'hierarchical_clustering/trigram_clustering/clustering'. 

The other analyses (i.e., using functional bigrams and fourgrams, as in Supplemental Fig. S5) can be run in exactly the same way. Just cd into the appropriate directory and run the Python code there. 




