#!/bin/bash

dir=$1
enc=$2

mkdir results_deter/$dir/
#mkdir results_deter/$dir/$ntrees/

cp results_distance/$dir/graph.txt results_deter/$dir/
cp results_distance/$dir/distances.txt results_deter/$dir/
cp results_distance/$dir/orig_path.txt results_deter/$dir/

#python gen_tree.py $dir 0

python graph-opt.py results_deter/$dir/ $enc 6

gams tree.gams

scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
ssh -2 asabnis@ct1.att2.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
ssh -2 asabnis@ct1.att2.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
scp -2 asabnis@ct1.att2.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_deter/$dir/res$enc.xml

python parsetrees.py results_deter/$dir/ $enc
python parse_solution.py results_deter/$dir/ 

python gen_dot1.py results_deter/$dir/
fdp results_deter/$dir/orig.dot -Tpng -o results_deter/$dir/original.png
fdp results_deter/$dir/inf.dot -Tpng -o results_deter/$dir/inferred.png

#./gedevo.sh results_deter/$dir/$ntrees/