import sys
dir = sys.argv[1]

nodes={}


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

f = open(dir + "/o_edges.txt", "r")

## find the number of enclaves
i = 1
for l in f:
    l = l.strip().split(" ")
    if hasNumbers(l[0]) == False and l[0] not in nodes:
        nodes[l[0]] = 'e' + i
        i += 1

f.close()

f = open('orig_path.txt' ,'r')
i = 1

for l in f:
    l = l.strip.split(' ')
    if l[1] not in nodes:
        nodes[

## map the enclaves and egress routers



## map rest of the routers


## Write sorted edges into a set


## Write to file 
