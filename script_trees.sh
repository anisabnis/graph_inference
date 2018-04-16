#!/bin/bash

dir=$1
enc=$2

# mkdir results_trees/$dir/

# cp results/$dir/graph.txt results_trees/$dir/
# cp results/$dir/distances.txt results_trees/$dir/
# cp results/$dir/orig_path.txt results_trees/$dir/

# python graph-opt.py results_trees/$dir $enc

# gams tree.gams

# scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
# ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
# ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
# scp -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_trees/$dir/res$enc.xml

# python parsetrees.py results_trees/$dir $enc
# python parse_solution.py results_trees/$dir 

# python gen_dot1.py results_trees/$dir
# fdp results_trees/$dir/orig.dot -Tpng -o results_trees/$dir/original.png
# fdp results_trees/$dir/inf.dot -Tpng -o results_trees/$dir/inferred.png

./gedevo.sh results_trees/$dir/