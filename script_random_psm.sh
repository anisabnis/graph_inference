#!/bin/bash

dir=$1
enc=$2
ntrees=$3

mkdir results_random_err_psm/$dir/
mkdir results_random_err_psm/$dir/$ntrees/

cp results/$dir/graph.txt results_random_err_psm/$dir/$ntrees/
cp results/$dir/distances.txt results_random_err_psm/$dir/$ntrees/
cp results/$dir/orig_path.txt results_random_err_psm/$dir/$ntrees/

python graph-opt.py results_random_err_psm/$dir/$ntrees $enc $ntrees

gams tree.gams

scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
ssh -2 asabnis@ct1.6et1dup.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
ssh -2 asabnis@ct1.6et1dup.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
scp -2 asabnis@ct1.6et1dup.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_random_err_psm/$dir/$ntrees/res$enc.xml

python parsetrees.py results_random_err_psm/$dir/$ntrees $enc
python parse_solution.py results_random_err_psm/$dir/$ntrees 

python gen_dot1.py results_random_err_psm/$dir/$ntrees
fdp results_random_err_psm/$dir/$ntrees/orig.dot -Tpng -o results_random_err_psm/$dir/$ntrees/original.png
fdp results_random_err_psm/$dir/$ntrees/inf.dot -Tpng -o results_random_err_psm/$dir/$ntrees/inferred.png

# #./gedevo.sh results_random_err_psm/$dir/$ntrees/