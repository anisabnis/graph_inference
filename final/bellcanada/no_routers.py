f = open('orig_path.txt', 'r')
a = set()
for l in f:
    l = l.strip().split()
    for s in l:
        a.add(s)

print(a)