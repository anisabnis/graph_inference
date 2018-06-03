#!/bin/bash

dir=$1
enc=$2

mkdir results_rd/$dir/
#mkdir results_rd/$dir/$ntrees/

cp results/$dir/graph.txt results_rd/$dir/
cp results/$dir/distances.txt results_rd/$dir/
cp results/$dir/orig_path.txt results_rd/$dir/

#python gen_tree.py $dir 0

python graph-opt.py results_rd/$dir/ $enc 6

gams tree.gams

scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
ssh -2 asabnis@ct1.6et1dup.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
ssh -2 asabnis@ct1.6et1dup.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
scp -2 asabnis@ct1.6et1dup.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_rd/$dir/res$enc.xml

python parsetrees.py results_rd/$dir/ $enc
python parse_solution.py results_rd/$dir/ 

python gen_dot1.py results_rd/$dir/
fdp results_rd/$dir/orig.dot -Tpng -o results_rd/$dir/original.png
fdp results_rd/$dir/inf.dot -Tpng -o results_rd/$dir/inferred.png

#./gedevo.sh results_rd/$dir/$ntrees/