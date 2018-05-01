givers = ['Joe', 'Sarah', 'John', 'Colleen', 'Andy', 'Emily', \
          'David', 'Rachel', 'Stephanie']
prevyear = [6,4,8,1,2,3,5,0,7] #2015
recnum = [9,9,9,9,9,9,9,9,9]
i = 0
import random
random.seed()
new = False
i = 0
num = 0
loopcount = 0
while i < 9:
    if i == 8: break
    while new == False:
        loopcount = loopcount + 1
        if (loopcount == 50): break
        num = random.randint(0,8)
# make sure we have no duplicates
        if (num in recnum or num == i):
            new = False
# no spouse matches
        elif ((i == 0 and num == 1) or (i == 1 and num == 0)\
              or (i == 2 and num == 3) or (i == 3 and num == 2) \
              or (i == 4 and num == 5) or (i == 5 and num == 4) \
              or (i == 6 and num == 7) or (i == 7 and num == 6)) \
              : new = False
# not the same as last year either
        elif (num == prevyear[i]):
            new = False
        else: new = True
    recnum[i] = num
    new = False
    i = i+1

# Flawed logic: no check to make sure Stephanie (recnum[8]) does not
# get herself or Last year's. See random_names.py for correct logic. 
for j in range(9):
    if j not in recnum:
        recnum[8] = j
# for i in range(9):
#     print (givers[i], "    \t", givers[recnum[i]])
# next

print ()
print ("Giver     \tReceiver     \tLast Year")
print ("-----     \t--------     \t---------")
for i in range(9):
  print (givers[i], "    \t", givers[recnum[i]], "   \t", givers[prevyear[i]])
print ()