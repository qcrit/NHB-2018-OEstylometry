import sys

def main(dict_file_name, inp_file_name):
	with open(dict_file_name,"r") as input_dict:
		list_of_words=[]
		for line in input_dict:
			list_of_words+=line.strip("\n.").split(" ")
		 #list_of_words=[w.strip("\n")  for w in  input_dict.readlines()]
		 #print (list_of_words)
		 #print len(list_of_words)

	with open(inp_file_name,"r") as input_file:
		 words=[]
		 for line in input_file:
		 	 words+=line.strip("\n.").split(" ")
		 #print (words)

	positions={}
    #ffword="{"
	count=0
	ffword="{"
	for dword in list_of_words:
		positions[count]=[]
		positions[count].append(dword)

		if len(dword)<=3:
			continue
		else:
			for word in words:
				if ffword in word:
					poem=word

				if dword in word:
					positions[count].append(poem)
		count+=1

	with open("comploc.txt","w") as output_file:
		output_file.write("compound,frequency \n ")
		for pos in positions:
			if len(positions[pos])>1:
				output_string=str(positions[pos][0])+" "+str(positions[pos][1:])+"\n"
				output_file.write(output_string)



if __name__=="__main__":

	dict_file_name=sys.argv[1]
	inp_file_name=sys.argv[2]
	main(dict_file_name,inp_file_name)
