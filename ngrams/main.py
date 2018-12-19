# main.py
# for running ngram analysis

import pickle
import os
import sys

import tools as ts
import ngrams as ngm

# whether to save copy of dataset for access later
pickleOn = False

# for chunking the input files (if needed set shouldChunk = True)
shouldChunk = False
sChunksize = 500
sTrashsize = 50

# save files
picklefile = "nonaggregated_formatted.pickle"
resultfile_NG = "results_NG"		# results for all ngrams stored in this .csv file with [n]gram measures in .txt files

#----------------------------------------------------------------------------

# Try to load pickle dataset, otherwise create and save and load a dataset from directory
try:
	print("Loading dataset "+picklefile)
	with open(picklefile, 'rb') as handle:
		mydata = pickle.load(handle)
except:
	print("No saved dataset, reading from "+originaldirectory)
	mydata = []
	
	# append contents of files into dataset
	textcontent = ""
	directory = os.fsencode(originaldirectory)
	for file in os.listdir(directory): # go through the given directory
		filename = os.fsdecode(file)
		#print("reading "+filename)
		with open(originaldirectory+"/"+filename,'rb') as v:
			textcontent = v.read().decode('utf-8')
		if shouldChunk == True:
			chunkdata = ts.chunk(textcontent, sChunksize, sTrashsize) # for chunking data
			for ind, chunkd in enumerate(chunkdata):
				mydata.append([filename+str(ind), chunkd])
		else:
			mydata.append([filename, textcontent]) # add string of text into dataset

	# dump for easier access later
	if pickleOn:
		with open(picklefile, 'wb') as handle:
			pickle.dump(mydata, handle, protocol=pickle.HIGHEST_PROTOCOL)

#----------------------------------------------------------------------------

# Do bi/tri/etc ngram analysis for the 5 most common grams
ngm.NG_main(mydata, resultfile_NG+"_n2.txt", 2, 5)
ngm.NG_main(mydata, resultfile_NG+"_n3.txt", 3, 5)
ngm.NG_main(mydata, resultfile_NG+"_n4.txt", 4, 5)

# Aggregate ngram text results into a single csv
ts.combinefile([resultfile_NG+"_n2.txt", resultfile_NG+"_n3.txt", resultfile_NG+"_n4.txt"], resultfile_NG+".csv")
