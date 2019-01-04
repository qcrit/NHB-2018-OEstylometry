import sys
import csv

def main(dict_file_name, inp_file_name):
	with open(dict_file_name,"r") as input_dict:
		matto=csv.reader(input_dict,delimiter=" ")
		matth=list(matto)

	with open(inp_file_name,"r") as input_file:
		 words=[]
		 for line in input_file:
		 	 words+=line.strip("\n.").split(" ")

	positions={}
	count=0
	print (words)
	for word in matth:
		positions[count]=[]
		#print (str(word[1:]).strip("[]").strip("''"))

		tracker=0
		for dword in words:
			if dword in word:
				tracker+=1

		if tracker>1:
			print (str(word[1:]).strip("[]").strip("''"))
			positions[count].append(word)
		count+=1

	with open("cynewulfcomps.txt","w") as output_file:
		#output_file.write("compound,frequency \n ")
		for pos in positions:
			if len(positions[pos])>0:
				output_string=str(positions[pos][0])+" "+str(positions[pos][1:]).strip("[]").strip("''")+"\n"
				output_file.write(output_string)



if __name__=="__main__":

	dict_file_name=sys.argv[1]
	inp_file_name=sys.argv[2]
	main(dict_file_name,inp_file_name)
