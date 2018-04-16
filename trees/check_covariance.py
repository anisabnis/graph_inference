import sys
from collections import defaultdict
import os

def prune(src, paths):
    indegree = defaultdict(lambda:defaultdict(lambda:0))
    outdegree = defaultdict(lambda:defaultdict(lambda:0))

    for p in paths:
        for i, r in enumerate(p[1:len(p)-1]):
            indegree[r][p[i]] = indegree[r][p[i]] + 1
            outdegree[r][p[i+2]] = outdegree[r][p[i+2]] + 1

    two_degree_routers = [r for r in indegree if len(indegree[r]) <= 1 and len(outdegree[r]) <= 1]

    new_paths = []
    for p in paths:
        np = [i for i in p if i not in two_degree_routers]
        new_paths.append(np)

    return new_paths

def prune_dict(src, paths):
    new_paths = defaultdict(list)

    indegree = defaultdict(lambda:defaultdict(lambda:0))
    outdegree = defaultdict(lambda:defaultdict(lambda:0))

    for p in paths:
        p = paths[p]
        for i, r in enumerate(p[1:len(p)-1]):
            indegree[r][p[i]] = indegree[r][p[i]] + 1
            outdegree[r][p[i+2]] = outdegree[r][p[i+2]] + 1

    two_degree_routers = [r for r in indegree if len(indegree[r]) <= 1 and len(outdegree[r]) <= 1]

    for p in paths:
        p = paths[p]
        np = [i for i in p if i not in two_degree_routers]
        dst = np[-1]
        new_paths[dst] = np

    return new_paths


def compute_shared_measures(src, paths):
    shared_len = {}
    for i in range(len(paths)):
        p1 = paths[i]
        d1 = p1[-1]

        for j in range(i+1, len(paths)):
            p2 = paths[j]
            d2 = p2[-1]
            l = min(len(p1), len(p2))            
            d = [d1, d2]
            d.sort()
            dist = tuple(d)
            shared_len[dist] = sum([1 if p1[k] == p2[k] else 0 for k in range(l)])

    return shared_len

def calc_relative_sharing(shared_lengths, src):
    shared_path_rules = []

    for p1 in shared_lengths:
        for p2 in shared_lengths:
            if p1 == p2:
                continue

            cv = ''
            index1 = 0
            index2 = 0

            if p1[0] == p2[0]:
                cv = p1[0]
                index1 = 1
                index2 = 1
            elif p1[1] == p2[0]:
                cv = p1[1]
                index1 = 0
                index2 = 1
            elif p1[0] == p2[1]:
                cv = p1[0]
                index1 = 1
                index2 = 0
            elif p1[1] == p2[1]:
                cv = p1[1]
                index1 = 0
                index2 = 0

            if cv == '':
                continue

            ucv1 = p1[index1]
            ucv2 = p2[index2]

            v = [ucv1, cv]
            v.sort()
            s1 = shared_lengths[tuple(v)]

            v = [ucv2, cv]
            v.sort()
            s2 = shared_lengths[tuple(v)]
            
            if s1 > s2:
                shared_path_rules.append([cv, ucv1, ucv2, 1])
            elif s1 == s2:
                shared_path_rules.append([cv, ucv1, ucv2, 0])
            else :
                shared_path_rules.append([cv, ucv1, ucv2, -1])

        return shared_path_rules

def get_path_metrics(file):    
    paths_by_src = defaultdict(list)
    distances = {}
    
    shared_path = defaultdict(lambda : defaultdict(float))
    relative_sharing = {}

    f= open(file, 'r')
    enc = set()

    for l in f:
        l = l.strip().split(' ')
        paths_by_src[l[0]].append(l)
        distances[(l[0], l[-1])] = len(l)
        enc.add(l[0])
    f.close()
    
    for e in enc:
        pruned_paths = prune(e, paths_by_src[e])
        shared_path[e] = compute_shared_measures(e, pruned_paths)
        relative_sharing[e] = calc_relative_sharing(shared_path[e], e)
        
    return relative_sharing

def checkTrees(src_paths, rules):
    count = 0
    for r in rules:
        cv = r[0]
        ucv1 = r[1]
        ucv2 = r[2]
        exp_res = r[3]

        cv_path = src_paths[cv]
        ucv1_path = src_paths[ucv1]
        ucv2_path = src_paths[ucv2]
        
        if len(cv_path) == 0 or len(ucv1_path) == 0 or len(ucv2_path) == 0:
            return True

        l = min(len(cv_path), len(ucv1_path))
        s1 = sum([1 if cv_path[k] == ucv1_path[k] else 0 for k in range(l)])
    
        l = min(len(cv_path), len(ucv2_path))
        s2 = sum([1 if cv_path[k] == ucv2_path[k] else 0 for k in range(l)])

        if s1 > s2:
            ans = 1
        elif s1 == s2:
            ans = 0
        else :
            ans = -1

        if ans != exp_res :
            #print("src_paths ", src_paths)
            print("Rule Violated ", src_paths[cv][0], r)
            count += 1
        
    return count

def verifyTreeConstraints(new_paths, orig_path_metrics):
    paths_by_src = defaultdict(lambda : defaultdict(list))
    enc = set()
    reply = True
    
    for p in new_paths:
        paths_by_src[p[0]][p[-1]] = p
        enc.add(p[0])        

    enc = ['e']
    violations = 0
    for e in enc:
        src_paths = prune_dict(e, paths_by_src[e])
        ans = checkTrees(paths_by_src[e], orig_path_metrics[e])
        violations += ans

    return violations

orig_path_metrics = get_path_metrics('./orig_path.txt')

vio = open('violations1_e.txt' ,'w')

for file_name in os.listdir('./run2'):

    f = open('run2/' + str(file_name) , 'r')
    new_paths = []
    for l in f:
        l = l.strip().split(' ')
        new_paths.append(l)

    f.close()
    print(file_name)

    violations = verifyTreeConstraints(new_paths, orig_path_metrics)
    vio.write(str(file_name) + " " + str(violations) + "\n")

vio.close()



