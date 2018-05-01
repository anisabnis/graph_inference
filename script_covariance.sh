#!/bin/bash

dir=$1
enc=$2

#mkdir results_covariance/$dir/


# cp results/$dir/graph.txt results_covariance/$dir/
# cp results/$dir/distances.txt results_covariance/$dir/
# cp results/$dir/orig_path.txt results_covariance/$dir/

python graph-opt.py results_covariance/$dir $enc 6
# cp tree.gams results_covariance/$dir/

# gams tree.gams

# scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
# ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
# ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
# scp -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_covariance/$dir/res$enc.xml

# python parsetrees.py results_covariance/$dir $enc
# python parse_solution.py results_covariance/$dir 

# python gen_dot1.py results_covariance/$dir
# fdp results_covariance/$dir/orig.dot -Tpng -o results_covariance/$dir/original.png
# fdp results_covariance/$dir/inf.dot -Tpng -o results_covariance/$dir/inferred.png

# ./gedevo.sh results_covariance/$dir/