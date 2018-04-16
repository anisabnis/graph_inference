#!/bin/bash

dir=$1
enc=$2

mkdir results/$dir/

#cp final/$dir/graph.txt results/$dir/
#cp final/$dir/distances.txt results/$dir/
#cp final/$dir/orig_path.txt results/$dir/

python graph-opt.py results/$dir $enc

gams tree.gams

scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
scp -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results/$dir/res$enc.xml

python parsetrees.py results/$dir $enc
python parse_solution.py results/$dir 

python gen_dot1.py results/$dir
fdp results/$dir/orig.dot -Tpng -o results/$dir/original.png
fdp results/$dir/inf.dot -Tpng -o results/$dir/inferred.png

./gedevo.sh results/$dir/