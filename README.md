## Replication code for Chaudhuri et al., "Large-scale quantitative profiling of the Old English verse tradition," forthcoming in Nature Human Behaviour

The code requires Python 3.6.0+. It is recommended that you create a virtual environment for this project before installing the required packages and running this code. If you have not done so previously, you will need to install virtualenv (e.g., by running `pip install virtualenv`). To create a virtual environment called 'venv_OE_stylometry', type `virtualenv venv_OE_stylometry`. To activate the virtual environment, type `source venv_OE_stylometry/bin/activate` when in the main directory. 

Before running the replication experiments, install the required Python packages. (N.B. I'll make a full list when all of the code is added to the repo - for now just install whatever you're prompted to.)

## Part 1: Corpus-wide functional ngram profiling (Fig. 1 and Supplemental Fig. S2)

To reproduce the ngram results in Fig. 1:

1) cd into the 'ngrams' directory. 
2) Type `python3 main.py` in the terminal. 
3) Running this code will generate three texts files listing the five most common functional bigrams, trigrams, or fourgrams in each text in the (nonaggregated) corpus, along with their frequencies and differences from the corpus mean. It will also produce a summary .csv file with key data. Fig. 1 is a plot of the sum of the trigram differences (i.e., the sum of columns Z, AD, AH, AL, and AP in 'results_NG.csv') against length (given in 'lengths.csv') for each text. 

## Part 2: Sense-pause analysis (Fig. 2)

To reproduce the sense-pause results in Fig. 2A:

1) cd into the 'sense_pauses' directory. 
2) Run 'python3 main.py arg1 arg2' in the terminal. 
3) 'Arg1' should be the name of the directory that contains the texts to be analyzed and 'Arg2' should be the name of the output file.
E.g., to generate the selected data in Fig. 2A run `python3 main.py selected_texts_Fig2A SPresults`. To generate data for the whole (aggregated) corpus use 'Calgary_corpus' as the input folder

## Part 3: Hierarchical agglomerative clustering using high-frequency ngrams (Fig. 4 and Supplemental Fig. S5)

To reproduce the dendrogram in Fig. 4:

1) cd into the 'hierarchical_clustering/trigram_clustering/clustering' directory. 
2) Run `python3 hierarchical_ngram_clustering.py` in the terminal. 

To generate the raw trigram input data (not required for running 'hierarchical_ngram_clustering.py' because the input data is already provided):

1) cd into the 'hierarchical_clustering/trigram_clustering/trigram_calculation' directory. 
2) Type `python3 character_ngrams.py` in the terminal. 
3) This will calculate the frequencies of the 30 most common ngrams in each text in the (modified nonaggregated) corpus and print them to 'results.xlsx'.
4) To prepare the data for clustering, the following preprocessing steps are required. i) Sort the texts by length (i.e., by column AE). ii) Delete everything below row 50 (i.e., retain only the five longest texts). iii) Rescale the frequencies to min -1 and max 1. These three steps will yield the final input data required (i.e., Sheet2 of 'results1.xlsx' in 'hierarchical_clustering/trigram_clustering/clustering'. 

The other analyses (i.e., using functional bigrams and fourgrams, as in Supplemental Fig. S5) can be run in exactly the same way. Just cd into the appropriate directory and run the Python code there. 




