#!/bin/bash

dir=$1
enc=$2

mkdir results_psm_dist/$dir/
#mkdir results_psm_dist/$dir/$ntrees/

cp results/$dir/graph.txt results_psm_dist/$dir/
cp results/$dir/distances.txt results_psm_dist/$dir/
cp results/$dir/orig_path.txt results_psm_dist/$dir/

python gen_tree.py $dir 0

python graph-opt.py results_psm_dist/$dir/ $enc 6

gams tree.gams

scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
ssh -2 asabnis@ct1.att2.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
ssh -2 asabnis@ct1.att2.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
scp -2 asabnis@ct1.att2.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_psm_dist/$dir/res$enc.xml

python parsetrees.py results_psm_dist/$dir/ $enc
python parse_solution.py results_psm_dist/$dir/ 

python gen_dot1.py results_psm_dist/$dir/
fdp results_psm_dist/$dir/orig.dot -Tpng -o results_psm_dist/$dir/original.png
fdp results_psm_dist/$dir/inf.dot -Tpng -o results_psm_dist/$dir/inferred.png

#./gedevo.sh results_psm_dist/$dir/$ntrees/