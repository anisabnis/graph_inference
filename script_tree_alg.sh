#!/bin/bash

dir=$1
enc=$2
ii=$3

python graph-opt.py results_deter/$dir $enc a:b $ii

gams tree.gams

scp -2 tree.mps asabnis@users.deterlab.net:/users/asabnis/cplex/bin/x86-64_linux/
ssh -2 asabnis@traf11.tata2.edgect.isi.deterlab.net "rm ~/cplex/bin/x86-64_linux/solution.xml"
ssh -2 asabnis@traf11.tata2.edgect.isi.deterlab.net "cd ~/cplex/bin/x86-64_linux/; ./cplex -f ./command.txt; cd ../../..;" 
scp -2 asabnis@traf11.tata2.edgect.isi.deterlab.net:~/cplex/bin/x86-64_linux/solution.xml results_deter/$dir/$ii/res$enc.xml

python parsetrees1.py results_deter/$dir/$ii $enc $ii
python parse_solution.py results_deter/$dir/$ii 

python gen_dot1.py results_deter/$dir/$ii
fdp results_deter/$dir/$ii/orig.dot -Tpng -o results_deter/$dir/$ii/original.png
fdp results_deter/$dir/$ii/inf.dot -Tpng -o results_deter/$dir/$ii/inferred.png

./gedevo.sh results_deter/$dir/$ii/