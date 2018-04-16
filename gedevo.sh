#!/bin/bash

dir=$1
python graph_params.py $dir
./orca.o node 5 $dir/output/orig.txt $dir/output/orig_out.sigs
./orca.o node 5 $dir/output/new.txt $dir/output/new_out.sigs
python convert.py $dir/output/ $dir
#scp -2 $dir/output/* asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/gedevo/output/
#ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "cd ~/gedevo; ./gedevo.sh"
#scp -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/gedevo/output/result $dir
