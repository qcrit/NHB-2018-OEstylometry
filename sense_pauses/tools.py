import os

# Function for determining relevant punctuation
def punct(mychr):
	"""returns whether mychr is in a punctuation list or not"""
	if mychr == '!' or mychr == ';' or mychr == '?' or mychr == '.' or mychr == ':' or mychr == '(' or mychr == ')':
		return True
	else:
		return False
		
# Function for chunking
def chunk(mystr, samplesize, trashsize):
	"""chunks mystr and returns array answer, samplesize is the size to break chunks into, trashsize is the size below which to discard leftover text"""
	answer = []
	chunkdat = mystr.split(" ")
	
	if len(chunkdat)/samplesize < 1: # sample is only big enough for one chunk
		if not len(chunkdat) < trashsize:
			return [" ".join(chunkdat)]
		else: # last chunk too short
			return []
	
	for i in range(0, len(chunkdat), samplesize): # sample big enough for multiple chunks
		temp = " ".join(chunkdat[i : i + samplesize])
		answer.append(temp)
		
	# check that the last chunk is bigger than trash size
	if len(answer[-1].split(" ")) < trashsize: # last chunk too short
		answer.pop(-1)
	return answer
	
# Function for dataset-to-string
def generateCorpstr(mydata, spaces):
	"""changes mydata datastr to corpus string, spaces- may or may not include"""
	# add mydata to corpstr
	corpstr = ""
	pastchara = ""
	for datapiece in mydata:
		tempstr = ""
		for chara in datapiece[1]:
			if chara not in ["-", ",","\n","\r","\t","#","\ufeff",'"', "'"] and not punct(chara):
				if not (spaces == False and chara == " "):
					if not (chara == " " and pastchara == " "): # avoid double spaces
						tempstr += chara
					pastchara = chara
		corpstr += tempstr

	return corpstr

# Process texts, error on some OE characters
def process_txt(textname, fileRaw, fileNew, append=False):
	"""process a text, e.g. remove numbers, parameters fileRaw, fileNew, and whether to append"""
	# Open original file f1 and empty file f2
	# append= whether should append to fileWrite or rewrite it
	
	#--------------------------------
	f1 = open(fileRaw,'r') # original
	if append == False:
		f2 = open(fileWrite,'w') # clear write file
		f2.write("")
		f2.close()
	f2 = open(fileWrite,'a')
	#--------------------------------
	
	# Variables to be updated as moving through file
	f2.write("{"+textname+"}[custom] ") # {title}[type] tags added at beginning
	pastchara = 'X'

	# Format, write to file and to string
	for line in f1: 
		for chara in line:
			if punctBeowulf(chara):						# separate punctuation from text
				f2.write(" ")
				f2.write(chara) # save results
			elif chara.isdigit():								# remove numbers
				pass			
			elif chara == " " and pastchara == " ":	# not double space
				pass
			elif chara in stripcharacters:
				pass
			elif fLowercase == True and ord(chara) >= 65 and ord(chara) <= 90:
																			# write lowercase letters
																			# to-do, allow old english too
				f2.write(chara.lower())
			else:														# symbols, other letters, etc
				f2.write(chara)
			pastchara = chara
			
	f1.close()
	f2.close()
	print("Text processed.")
	
# Used in next function, string-to-data
def makedata(corpstr):
	"""makes dataset from string"""
	cdata = [["", "", ""]]
	purecorpus = ""
	punctOn = False # used to separate {title}[type] from the data
	title = ""
	type = ""
	partOn = "X" # which aspect am writing to
	
	for letter in corpstr: # go through text's contents
		punctOn = True
		if letter == '{': # is a title!
			partOn = "title"
			cdata.append(["", "", ""]) # create new entry to save to
			title = "" # clear past title/type entry
			type = ""
		elif letter == '}':
			partOn = "W"
		elif letter == '[': # is a type!
			partOn = "type"
		elif letter == ']':
			partOn = "X"
			cdata[-1][0] = title # save title and type
			cdata[-1][1] = type
		else:
			punctOn = False
		if punctOn == False: # i.e. working with text, not {}[]
			if partOn == "title":
				if letter != ":": # messes up file names
					title += letter # write to the title
			elif partOn == "type":
				type += letter # write to the type
			else:
				if letter == "#":
					cdata[-1][2] += "#" # append new line character
				elif letter != "@":
					cdata[-1][2] += letter # write normally to body of text
	cdata.pop(0)
	return cdata

# Create dataset with [title, type, text] for each entity in string of corpus text
def reverse_process_input(txtfile):
	"""makes dataset from string"""
	with open(txtfile,'rb') as v:
		textcontent = v.read().decode('utf-8')
	ddata = makedata(textcontent)

	if not os.path.exists("input files"):
		os.makedirs("input files")
		
	for cdata in ddata:
		myfile = open("input files/"+cdata[0]+".txt",'wb')
		myfile.write(" ".join(cdata[2].split()).encode("utf-8")) # removes double spaces
		myfile.close()
		
# Given array of text files, create single csv using certain rows and columns
# Aimed at ngram files
def combinefile(arr_txts, savename):
	"""for ngrams, aggregate texts in arr_txts into csv file savename"""
	arr_contents = []
	for txt in arr_txts:
		with open(txt, "r") as f:
			arr_contents.append(f.readlines())
	
	with open(savename, "w") as g:
		# Get header and write to savename
		g.write(arr_contents[0][0])
		# For each line of file: write full arr_contents[0], then following without the first columns
		for ind in range(1, len(arr_contents[0])):
			for I,F in enumerate(arr_contents):
				noendline_data = F[ind].splitlines()[0]
				if I != 0:
					noendline_data = noendline_data.split(",")[1:]
					noendline_data = ",".join(noendline_data)
				g.write(noendline_data+",")
			g.write("\n")
	
