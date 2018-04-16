import sys

def edit_distance(s1, s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

    return tbl[i,j]

dir = sys.argv[1]

o_path = dict()
f = open(dir + '/orig_path.txt', 'r')
for l in f:
    l = l.strip().split(' ')
    s = l[0]
    d = l[1]
    o_path[((s,d))]
f.close()

f = open(dir + '/new_paths.txt' , 'r')
n_path = dict()
for l in f:
    l = l.strip().split(' ')
    s = l[0]
    d = l[1]
    n_path[((s,d))]
f.close()


#print(edit_distance("Helloworld", "HalloWorld"))
