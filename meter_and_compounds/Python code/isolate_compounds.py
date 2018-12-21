import sys
import re

def main(dict_file_name, inp_file_name):
	list_of_words=[]
	with open(dict_file_name,"r") as input_dict:
		for line in input_dict:
			data=line.split()
			list_of_words.append(data[0])
			print(list_of_words)

	with open(inp_file_name,"r") as input_file:
		 words=[]
		 for line in input_file:
		 	 words+=line.strip("\n.").split(" ")


	positions={}
	count=0
	ffword="{"
	fgword="}"
	endline="#"
	lineno=1
	for word in words:
		#print(word)
		positions[count]=[]
		positions[count].append(word)
		if endline in word:
			lineno+=1
		if ffword in word or fgword in word:
			positions[count].append(word)
			lineno=1



		if len(word)<=3:
			continue
		else:
			for dword in list_of_words:
				if dword==word:
					positions[count].append(lineno)
		count+=1

	with open("onlycompounds.txt","w") as output_file:
		output_file.write("word,line number \n ")
		for pos in positions:
			if len(positions[pos])>1:
				output_string=str(positions[pos][0])+", "+str(positions[pos][1:])+"\n"
				output_file.write(output_string)

if __name__=="__main__":

	dict_file_name=sys.argv[1]
	inp_file_name=sys.argv[2]
	main(dict_file_name,inp_file_name)
