#!/bin/bash

dir=$1
enc=$2
ntrees=$3
ii=$4

mkdir results_best_only/$dir$ii/

cp results/$dir/graph.txt results_best_only/$dir$ii/
cp results/$dir/distances.txt results_best_only/$dir$ii/
cp results/$dir/orig_path.txt results_best_only/$dir$ii/

python graph-opt.py results_best_only/$dir$ii $enc $ntrees

gams tree.gams

scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
scp -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_best_only/$dir$ii/res$enc.xml

python parsetrees.py results_best_only/$dir$ii $enc
python parse_solution.py results_best_only/$dir$ii 

python gen_dot1.py results_best_only/$dir$ii
fdp results_best_only/$dir$ii/orig.dot -Tpng -o results_best_only/$dir$ii/original.png
fdp results_best_only/$dir$ii/inf.dot -Tpng -o results_best_only/$dir$ii/inferred.png

./gedevo.sh results_best_only/$dir$ii/