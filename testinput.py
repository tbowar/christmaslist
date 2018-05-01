

import fileinput, sys

if len(sys.argv) < 1:
	print ("No name file found\n")
	sys.exit()

for line in fileinput.input():
	line = line.strip()
	num = (fileinput.lineno()-1)

givers = [" " for i in range(num)]
norec = [" " for i in range(num)]
rec = [" " for i in range(num)]
print (num, givers[0])

for i in range(num):
	print (i, line)
	print (line.split(','))
	templine = (line.split(','))
	print (templine[0])
	print (templine[1])
	print (templine[2])
	givers[i] = templine[0]
	norec[i] = templine[1]
	rec[i] = templine[2]
	print (givers)
