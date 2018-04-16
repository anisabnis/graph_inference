f = open('new_paths.txt', 'r')
nodes = set()
for l in f:
    l = l.strip().split(' ')
    for i in l:
        nodes.add(i)

print(len(nodes))
