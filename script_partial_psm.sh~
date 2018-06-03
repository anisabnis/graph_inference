#!/bin/bash

dir=$1
enc=$2
ntrees=$3
ii=$4

mkdir results_partial/$dir$ii/

cp results/$dir/graph.txt results_partial/$dir$ii/
cp results/$dir/distances.txt results_partial/$dir$ii/
cp results/$dir/orig_path.txt results_partial/$dir$ii/

python graph-opt.py results_partial/$dir$ii $enc $ntrees

gams tree.gams

scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
ssh -2 asabnis@ct1.tata.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
ssh -2 asabnis@ct1.tata.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
scp -2 asabnis@ct1.tata.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_partial/$dir$ii/res$enc.xml

python parsetrees.py results_partial/$dir$ii $enc
python parse_solution.py results_partial/$dir$ii 

python gen_dot1.py results_partial/$dir$ii
fdp results_partial/$dir$ii/orig.dot -Tpng -o results_partial/$dir$ii/original.png
fdp results_partial/$dir$ii/inf.dot -Tpng -o results_partial/$dir$ii/inferred.png

#./gedevo.sh results_partial/$dir$ii/