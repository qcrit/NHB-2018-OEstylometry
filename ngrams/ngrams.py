import nltk
import tools as ts

def NG_main(mydata, savefile, N, X):	# given array of texts, place to save, type of ngram, number of ngrams per text
															# perform analysis of each text
	myfile = open(savefile,'wb')
	myfile.write("name,ngram,textfreq,corpfreq,diff,diffsum,length, ngram,etc\n".encode('utf-8'))
	
	# useful data
	corpStrSpaces = ts.generateCorpstr(mydata,spaces=True)
	corpStrNoSpaces = ts.generateCorpstr(mydata,spaces=False)
	
	for datapiece in mydata:
		useCorpusNgrams = False; # use X most frequent ngrams corpuswide (true) or textwide (false)
		if useCorpusNgrams:
			ngramDist = NG_dist(corpStrNoSpaces, N)
		else:
			ngramDist = NG_dist(ts.generateCorpstr([datapiece], spaces=False), N)
		
		# get the X most common ngrams
		commongrams = ngramDist.most_common(X)

		writestuff = datapiece[0]+"," # write the name of text

		diffSum = 0
		for fgram in commongrams:
			writestuff += "".join(fgram[0]) + "," # write the ngram being counted
			
			if useCorpusNgrams: # counting text/corpus ngrams in txt string and in corpus
				corpFreq = fgram[1]/len(corpStrSpaces)
				textFreq =  ts.generateCorpstr([datapiece], spaces=False).count(  "".join(fgram[0])  )/len(datapiece[1])
			else:
				textFreq =  fgram[1]/len(datapiece[1])
				corpFreq = corpStrNoSpaces.count(  "".join(fgram[0])  )/len(corpStrSpaces)
				diff = abs(textFreq-corpFreq)
				diffSum += abs(textFreq-corpFreq)
				length = len(datapiece[1])
			 
			writestuff += str(  round(textFreq,8)) + ","
			writestuff += str(  round(corpFreq,8)) + ","
			writestuff += str(  round(diff,8)) + ","
			writestuff += str(	round(diffSum, 8)) + ","
			writestuff += str(  round(length,8)) + ","

		writestuff += '\n'
		myfile.write(writestuff.encode('utf-8'))
	
	myfile.close()
		
	print(str(N)+"gram analysis complete")
		
def NG_dist(corpstr, N): # "dictionary" distribution for corpus ngrams
	tokens = list(corpstr)
	bgs = nltk.ngrams(tokens, N)
	fdist = nltk.FreqDist(bgs)
	return fdist
	
