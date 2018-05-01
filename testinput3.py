import sys, re

# givers - gift givers
# norec - do not match gift receivers with these (spouses or others
# rec - also do not match with these, last year's receivers
givers = []
norec = []
rec = []

if len(sys.argv) < 2:
    print ("No name file found\n")
    sys.exit()

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    numlines = len(lines)

# Search for names in lines
regex: str = r'(\w+),\s*(\w+),\s*(\w+)\s*'

# Iterate through lines, extract names and assign to lists
for i in range(numlines):
    temp = lines[i]
    match = (re.search(regex, temp))
    givers.append(i)
    givers[i] = match.group(1)
    norec.append(i)
    norec[i] = match.group(2)
    rec.append(i)
    rec[i] = match.group(3)

for i in range(numlines):
    print (givers[i], norec[i], rec[i])

