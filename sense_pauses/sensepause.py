import tools as ts
import re

def SP_main(mydata, resultfile):
	# Write headers to file
	myfile = open(resultfile,'w') # column labels on top
	myfile.write("\t SP/Chars \t Intraline/Chars \t Intraline/SP \t Text length \n")

	# sp analysis for each text
	for datapiece in mydata:
		t,a,b,c = SP(datapiece[0], datapiece[1]) # returns title and stats 1, 2, 3
		myfile.write(t+"\t"+str(a)+"\t"+str(b)+"\t"+str(c)+"\t"+str(len(datapiece[1]))+"\n")

	myfile.close()
	print("SP analysis complete")
	
	
def SP(textname, mystr):
	# Sense pause measuring for an OE text
	spausestats = [0, 0, 0] # total sp, total intraline sp, ratio intraline/total sp; will be normalized
	
	lastCharact = "" # the last counted character
	
	if len(mystr) == 0:
		print("warning- "+textname+" has length 0")
		return textname, spausestats[0], spausestats[1], spausestats[2]
	
	# Count sense pauses for total sp
	for charact in re.sub('\ ', '', mystr): # get rid of spaces
		if ts.punct(lastCharact):
			if charact in ["\n", "\r", "#"]:
				spausestats[0] += 1							# endline
			elif not charact == lastCharact: # coincident punctuation
				spausestats[0] += 1						# intraline
				spausestats[1] += 1
				
		lastCharact = charact
			
	# Calculate ratio intraline/total sp
	if spausestats[0] == 0:
		spausestats[2] = 0 # i.e. no pauses. avoid division by 0, mark as 0
	else:
		spausestats[2] = round(spausestats[1]/spausestats[0],5)
		
	# Normalize results by dividing by chars
	#mystr = re.sub('\#|\@', '', mystr) # for stripping unwanted chars
	
	spausestats[0] = round(spausestats[0]/len(mystr),5)
	spausestats[1] = round(spausestats[1]/len(mystr),5)
	
	return textname, spausestats[0], spausestats[1], spausestats[2]
