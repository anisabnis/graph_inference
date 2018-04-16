node_pos = {'a': "40,10!", 'b':"50,20!", 'c':"20,10!", 'd':"20,30!", 'e':"30,50!", 'f':"10,50", 'a1':"40,15!", 'b1':"45,20!", 'c1':"30,15!", 'd1':"25,30!", 'e1':"25,45!", 'f':"15,45!"}
import sys

def gen_dot(paths, dir, type):
    ## Generate a dot file
    nodes = set()
    edges = set()

    for p in paths:
        for i in range(len(p) - 1):
            nodes.add(p[i])
            edges.add((p[i],  p[i+1]))

    f = open(dir + '/topology' + str(type) +'.dot', 'w')
    f.write("digraph  {\n")

    for r in nodes:
        if r in node_pos:
            f.write("\t" + str(r) + " [pos=" + '"' + node_pos[r] + '"' + "];\n")
        else :
            f.write("\t" + str(r) + ";\n")

    for e in edges:
        f.write("\t" + e[0] + " -> " + e[1] + ";\n")

    f.write("\n\t}")


if __name__ == "__main__":
    dir = sys.argv[1]
    
    op = list()
    f = open(dir + "/orig_path.txt", 'r')
    for l in f:
        l = l.strip().split(' ')
        op.append(l)

    gen_dot(op, dir, "orig")


    np = list()
    f = open(dir + "/new_paths.txt", 'r')
    for l in f:
        l = l.strip().split(' ')
        op.append(l)

    gen_dot(op, dir, "inf")
    
    
    
