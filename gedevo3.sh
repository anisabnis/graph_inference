#!/bin/bash

dir=$1
for i in {1..4}; do
    echo $i
    python make_compact2.py $dir/output/O$i/ $dir
    for j in {1..3}; do 
	python graph_params2.py $dir $i $j
	./orca.o node 5 $dir/output/O$i/$j/orig.txt $dir/output/O$i/$j/orig_out.sigs
	./orca.o node 5 $dir/output/O$i/$j/new.txt $dir/output/O$i/$j/new_out.sigs
	python convert.py $dir/output/O$i/$j/ $dir
    done
done


#scp -2 $dir/output/* asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/gedevo/output/
#ssh -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net "cd ~/gedevo; ./gedevo.sh"
#scp -2 asabnis@ct1.h6e-t1a.edgect.isi.deterlab.net:~/gedevo/output/result $dir
