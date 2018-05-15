import sys
dir = sys.argv[1]
dir1 = sys.argv[2]

enclaves = set()

f = open(dir1 + '/orig_path.txt', 'r')
for l in f:
   l = l.strip().split(' ')
   enclaves.add(l[0])
f.close()

len_enclaves = len(list(enclaves)) * 2

f = open(dir + '/new.sif', 'r')
fi = open(dir + '/new_.sif', 'w')

for l in f:
    l = l.strip().split(' ')
    if int(l[0]) > len_enclaves - 1:
        l[0] = str(int(l[0]) + 10)

    else :
        l[0] = str(int(l[0]) + 1)
        
    if int(l[2]) > len_enclaves - 1:
        l[2] = str(int(l[2]) + 10)
    else :
        l[2] = str(int(l[2]) + 1)

    fi.write(l[0] + " u " + l[2] + "\n")

fi.close()
f.close()


f = open(dir + '/new_out.sigs', 'r')
fi = open(dir + '/new_out_.sigs', 'w')

for l in f:
    l = l.strip().split(' ')
    if int(l[0]) > len_enclaves - 1:
        l[0] = str(int(l[0]) + 10)
    else :
        l[0] = str(int(l[0]) + 1)

    fi.write(" ".join(l))
    fi.write("\n")
    #fi.write(l[0] + " " + l[1] + "\n")

fi.close()
f.close()



f = open(dir + '/orig.sif', 'r')
fi = open(dir + '/orig_.sif', 'w')

for l in f:
    l = l.strip().split(' ')
    l[0] = str(int(l[0]) + 1)
    l[2] = str(int(l[2]) + 1)
    fi.write(l[0] + " u " + l[2] + "\n")
fi.close()
f.close()


f = open(dir + '/orig_out.sigs', 'r')
fi = open(dir + '/orig_out_.sigs', 'w')

for l in f:
    l = l.strip().split(' ')

    l[0] = str(int(l[0]) + 1)

    fi.write(" ".join(l))
    fi.write("\n")
    #fi.write(l[0] + " " + l[1] + "\n")

fi.close()
f.close()

