#!/bin/bash

dir=$1
subdir=$2

python graph_params_exp2.py $dir $dir/$subdir
./orca.o node 5 $dir/$subdir/orig.txt $dir/$subdir/orig_out.sigs
./orca.o node 5 $dir/$subdir/new.txt $dir/$subdir/new_out.sigs
python convert.py $dir/$subdir/ $dir

