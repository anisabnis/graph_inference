import sys
import os

dir= sys.argv[1]
f = open(dir + "/no_edits", "r")
l = int(f.readline().strip())

for i in range(1, l):
    os.system("./gedevo2.sh " + dir + " " + str(i))
