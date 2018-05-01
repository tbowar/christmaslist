#!/usr/bin/python
#
# Random Names takes the children and their spouses names,
# and randomly matches them with each other for a "secret Santa".
# Putting the order of the previous year's matches into the prevyear
# array assures that no one will get the same person 2 years in a row.
#
# 0 - Joe
# 1 - Sarah
# 2 - John
# 3 - Colleen
# 4 - Andy
# 5 - Emily
# 6 - David
# 7 - Rachel
# 8 - Stephanie
#
givers = ['Joe', 'Sarah', 'John', 'Colleen', 'Andy', 'Emily', \
          'David', 'Rachel', 'Stephanie']
#prevyear = [6,4,8,1,2,3,5,0,7] #2015
prevyear = [7,5,6,0,1,8,3,2,4] #2016



import random
restart = True
restart_count = 0
while restart:
  restart = False
  random.seed()
  new = False
  recnum = [9,9,9,9,9,9,9,9,9]
  i = 0
  num = 0
  loopcount = 0
  while i < 9:
    if i == 8: break
    while not new:
      loopcount = loopcount + 1
      if (loopcount == 100): break
      num = random.randint(0,8)
# make sure we have no duplicates
#      print restart_count, loopcount, givers[i], givers[num]
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
    i += 1

  j = 0
  for j in range(9):
    if (j not in recnum):
      recnum[8] = j
      break
  if (j != 8 or j != prevyear[8]):
    restart = True
#    print restart_count, loopcount, givers[8], givers[j]
    restart_count += 1
#    print "RESTART\n"
    if restart_count > 200: break

print
print ("Restart count = ", restart_count)
print ("Giver     \tReceiver     \tLast Year")
print ("-----     \t--------     \t---------")
for i in range(9):
  print (givers[i], "     \t", givers[recnum[i]], "    \t", givers[prevyear[i]])
print