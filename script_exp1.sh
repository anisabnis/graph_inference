#!/bin/bash

dir=$1
enc=$2

# mkdir results_distance/$dir/
# #mkdir results_distance/$dir/$ntrees/

# cp results_psm/$dir/graph.txt results_distance/$dir/
# cp results_psm/$dir/distances.txt results_distance/$dir/
# cp results_psm/$dir/orig_path.txt results_distance/$dir/

# #python gen_tree.py $dir 0

# python graph-opt.py results_distance/$dir/ $enc 6

# gams tree.gams

# scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
# ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
# ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
# scp -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_distance/$dir/res$enc.xml

# python3.6 parsetrees.py results_distance/$dir/ $enc
# python3.6 parse_solution.py results_distance/$dir/ 

python3.6 gen_dot1.py results_distance/$dir/
fdp results_distance/$dir/orig.dot -Tpng -o results_distance/$dir/original.png
fdp results_distance/$dir/inf.dot -Tpng -o results_distance/$dir/inferred.png

#./gedevo.sh results_distance/$dir/$ntrees/
