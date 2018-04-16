#!/bin/bash
dir=$1

./gedevo_unix64 --save $dir/output/result --no-save --groups "$dir"o "$dir"n --sif $dir/output/orig_.sif "$dir"o --sif $dir/output/new_.sif "$dir"n --grsig $dir/output/orig_out_.sigs "$dir"o --grsig $dir/output/new_out_.sigs "$dir"n --pop 200 --maxsame 300 --no-workfiles --undirected
