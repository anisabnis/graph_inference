import sys
import itertools

def findsubsets(S,m):
    return set(itertools.combinations(S, m))

f = open("subset.txt", "w")
en = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(1,7):
    sub = findsubsets(en, i)
    for s in sub:
        st = ":".join([str(x) for x in s])
        f.write(st + "\n")

f.close()
        
