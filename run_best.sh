#!/bin/bash

start=53
filelines=`cat subset.txt`

for line in $filelines; do
    ./script_best.sh columbus 3 $line $start 
    start=$(($start + 1))
done
