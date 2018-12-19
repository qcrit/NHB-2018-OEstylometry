# main.py
# for running sensepause analysis

import pickle
import os
import sys

import tools as ts
import sensepause as sps

# files will be read from this folder
originaldirectory = sys.argv[1]

# whether to save copy of dataset for access later
pickleOn = False

# for chunking the input files (if needed, set shouldChunk = True)
shouldChunk = False
sChunksize = 500
sTrashsize = 50

# save files
picklefile = "inputfiles.pickle"		# where pickled file of input files will be stored
resultfile_SP = sys.argv[2]        # results for sense pause stored in this .txt file

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

# Do sense pause analysis
sps.SP_main(mydata, resultfile_SP+".txt")
