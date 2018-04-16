import sys
import os

dir = str(sys.argv[1])
#os.system("mkdir " + str(sys.argv[1]) + "/output/")
# parse out original file
enclaves = set()
subdir="output"

f = open(dir + '/' + subdir + '/orig_path.txt', 'r')
for l in f:
   l = l.strip().split(' ')
   enclaves.add(l[0])

new_routers = len(enclaves) * 2
rr = new_routers

add_routers = {}
new_paths = []
map = open(dir + '/' + subdir + '/map.txt' , 'w')

enclaves = list(enclaves)
enclaves.sort()
print(enclaves)

## First assign a alias for each router
## First the enclaves and egress
f = open(dir + '/' + subdir + '/orig_path.txt', 'r')

for l in f:
   l = l.strip().split(' ')
   s = l[0]
   d = l[-1]
   router_id = 0
   for r in l:
      if r == s or r == d:
         i = enclaves.index(r)
         if r not in add_routers:
            add_routers[r] = str(i)

      elif router_id == 1 or router_id == len(l) - 2:
         if router_id == 1:
            e_id = s
         else :
            e_id = d
         e_index = enclaves.index(e_id)
         e_index += len(enclaves)
         if r not in add_routers:
            add_routers[r] = str(e_index)

      router_id += 1

f.close()

f = open(dir + '/' + subdir + '/orig_path.txt', 'r')

for l in f:
   l = l.strip().split(' ')
   for r in l:
      if r not in add_routers:
         add_routers[r] = str(new_routers)
         new_routers += 1
f.close()

f = open(dir + '/' + subdir + '/orig_path.txt', 'r')
for l in f:
   l = l.strip().split(' ')
   np = []
   for r in l:
      np.append(add_routers[r])

   new_paths.append(np)

map.write(str(add_routers))
map.write("\n")

edges = set()
nodes = set()

for l in new_paths:
    for i in range(len(l) - 1):
        edge = [l[i], l[i+1]]
        edge.sort()
        edge = (edge[0], edge[1])
        edges.add(edge)
        nodes.add(l[i])

new_ = open(dir + '/output/orig.txt' , 'w')
new_sif = open(dir + '/output/orig.sif' , 'w')
new_.write(str(len(nodes)) + " " + str(len(edges)) + "\n")

for e in edges:
    new_.write(str(e[0]) + " " + str(e[1]) + "\n")
    new_sif.write(str(e[0]) + " d " + str(e[1]) + "\n")

#new_.close()
new_sif.close()
new_.close()

## do the same for new file


################################################################


f = open(dir + '/new_paths.txt', 'r')
new_routers = rr
add_routers = {}
new_paths = []


for l in f:
   l = l.strip().split(' ')
   s = l[0]
   d = l[-1]
   router_id = 0
   for r in l:
      if r == s or r == d:
         i = enclaves.index(r)
         if r not in add_routers:
            add_routers[r] = str(i)

      elif router_id == 1 or router_id == len(l) - 1:

         if router_id == 1:
            e_id = s
         else :
            e_id = d
         e_index = enclaves.index(e_id)
         e_index += len(enclaves)

         if r not in add_routers:
            add_routers[r] = str(e_index)
            
      router_id += 1

f.close()

f = open(dir + '/new_paths.txt', 'r')
for l in f:
   l = l.strip().split(' ')
   for i in range(2, len(l) - 2):
      r = l[i]
      if r not in add_routers:
         add_routers[r] = str(new_routers)
         new_routers += 1
f.close()

f = open(dir + '/new_paths.txt', 'r')
for l in f:
   l = l.strip().split(' ')
   np = []
   for r in l:
      np.append(add_routers[r])
   new_paths.append(np)

print(add_routers)
print(len(add_routers))

map.write(str(add_routers))
map.write("\n")

edges = set()
nodes = set()

for l in new_paths:
   for i in range(len(l) - 1):
      edge = [l[i], l[i+1]]
      edge.sort()
      edge = (edge[0], edge[1])
      edges.add(edge)
      nodes.add(l[i])
        
new_ = open(dir + '/output/new.txt' , 'w')
new_sif = open(dir + '/output/new.sif' , 'w')
new_.write(str(len(nodes)) + " " + str(len(edges)) + "\n")

for e in edges:
    new_.write(str(e[0]) + " " + str(e[1]) + "\n")
    new_sif.write(str(e[0]) + " d " + str(e[1]) + "\n")

#new_.close()
new_sif.close()
new_.close()
