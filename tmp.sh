#!/bin/bash

dir=$1
enc=$2
ntrees=$3

#mkdir results/$dir/

#cp final/$dir/graph.txt results/$dir/
#cp final/$dir/distances.txt results/$dir/
#cp final/$dir/orig_path.txt results/$dir/

python graph-opt.py bad-graphs/$dir $enc $ntrees
gams tree.gams

scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
scp -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml bad-graphs/$dir/res$enc.xml

python parsetrees.py bad-graphs/$dir $enc
python parse_solution.py bad-graphs/$dir 

python gen_dot1.py bad-graphs/$dir
fdp bad-graphs/$dir/orig.dot -Tpng -o bad-graphs/$dir/original.png
fdp bad-graphs/$dir/inf.dot -Tpng -o bad-graphs/$dir/inferred.png

./gedevo.sh bad-graphs/$dir/