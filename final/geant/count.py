routers = set()
f = open('orig_paths.txt', 'r')
for l in f:
    l = l.strip().split(' ')
    for r in l:
        routers.add(r)

print(len(routers))
