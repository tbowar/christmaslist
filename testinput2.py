import sys, re

if len(sys.argv) < 2:
    print ("No name file found\n")
    sys.exit()


with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    numlines = len(lines)

givers = [" " for i in range(numlines)]
norec = [" " for i in range(numlines)]
rec = [" " for i in range(numlines)]
#templine = [" ", " ", " "]
regex = r'\w+\s*,\s*\w+\s*,\s*\w+\s*'

for i in range(numlines):
    temp = lines[i]
    match = (re.search(regex, temp))
#    print (match)
#    templine = (temp.split(','))
#    else:
#        print ("Error in line", i+1)
#    givers[i] = templine[0].strip()
#    norec[i] = templine[1].strip()
#    rec[i] = templine[2].strip()
    
#for i in range(numlines):
#    print (givers[i], norec[i], rec[i])
