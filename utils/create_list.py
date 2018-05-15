import random
from utils import database

def new_list(name_file, newfile):
    with open(name_file, 'r') as file:
        namelist = [line.strip().split(',') for line in file.readlines()]

    listlen = len(namelist)
    restart = True
    restart_count = 0

    while restart:
        reclist = []
        restart = False
        random.seed()
        new = False
        i = 0
        num = 0
        loopcount = 0
        print()
        i = 0
        for i in range(listlen):
            while not new:
                loopcount += 1
                if (loopcount == 100):
                    restart = True
                    restart_count += 1
                    break
                num = random.randint(0, listlen-1)
                # make sure we have no duplicates
                #      print restart_count, loopcount, givers[i], givers[num]
                if (num >= listlen or num == i):
                    new = False
                # no spouse matches
                elif ((namelist[num][0] == namelist[i][1]) or (namelist[num][0] == namelist[i][2]) or (namelist[num][0] in reclist)):
                    new = False
                else:
                    new = True
                    reclist.append(namelist[num][0])
                    database.add(newfile, namelist[i][0], namelist[i][1], reclist[i])
            new = False
            if restart_count > 200:
                print()
                break
