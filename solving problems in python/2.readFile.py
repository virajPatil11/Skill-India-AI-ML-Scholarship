#opening input file

fin = open("in.txt", "rt")
#output file to write the result to
fout = open("out.txt", "wt")

for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('Today', '01-05-2021').replace('tomorrow','02-05-2021'))
#close input and output files
fin.close()
fout.close()