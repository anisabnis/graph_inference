import sys
import os

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

dir = str(sys.argv[1])
subdir = str(sys.argv[2])

#os.system("mkdir " + str(sys.argv[1]) + "/output/")

# parse out original file
enclaves = set()

f = open(subdir + '/orig_edges.txt', 'r')
for l in f:
   l = l.strip().split(' ')

   if hasNumbers(l[0]) == False:
      enclaves.add(l[0])

   if hasNumbers(l[1]) == False:
      enclaves.add(l[1])
f.close()

new_routers = len(enclaves) * 2
rr = new_routers

add_routers = {}
new_paths = []
map = open(subdir + '/map.txt' , 'w')

enclaves = list(enclaves)
enclaves.sort()

egress_routers = set()
e_map = dict()
f = open(dir + '/orig_path.txt' ,'r')
for l in f:
    l = l.strip().split(' ')
    egress_routers.add(l[1])
    e_map[l[1]] = l[0]

## First assign a alias for each router
## First the enclaves and egress
f = open(subdir + '/orig_edges.txt', 'r')

for l in f:
   l = l.strip().split(' ')
   router_id = 0
   for r in l:
      if hasNumbers(r) == False:
         i = enclaves.index(r)
         if r not in add_routers:
            add_routers[r] = str(i)

      #elif router_id == 1 or router_id == len(l) - 2:
      elif r in egress_routers:
         e_id = e_map[r]
         e_index = enclaves.index(e_id)
         e_index += len(enclaves)

         if r not in add_routers:
            add_routers[r] = str(e_index)
            
            

f.close()

f = open(subdir + '/orig_edges.txt', 'r')

for l in f:
   l = l.strip().split(' ')
   for r in l:
      if r not in add_routers:
         add_routers[r] = str(new_routers)
         new_routers += 1
f.close()

edges = set()
nodes = set()

f = open(subdir + '/orig_edges.txt', 'r')
for l in f:
   l = l.strip().split(' ')
   ne = []
   for r in l:
      ne.append(add_routers[r])
      nodes.add(add_routers[r])
   ne.sort()
   edges.add((ne[0],ne[1]))
map.write(str(add_routers))
map.write("\n")

new_ = open(subdir + '/orig.txt' , 'w')
new_sif = open(subdir + '/orig.sif' , 'w')
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
        
new_ = open(subdir + '/new.txt' , 'w')
new_sif = open(subdir + '/new.sif' , 'w')
new_.write(str(len(nodes)) + " " + str(len(edges)) + "\n")

for e in edges:
    new_.write(str(e[0]) + " " + str(e[1]) + "\n")
    new_sif.write(str(e[0]) + " d " + str(e[1]) + "\n")

#new_.close()
new_sif.close()
new_.close()
