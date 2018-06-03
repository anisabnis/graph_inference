#!/bin/bash

start=1
filelines=`cat subset.txt`

networks=(tata columbus)

for n in ${networks[@]}; do
    for line in $filelines; do
	./script_best.sh $n 3 $line $start 
	start=$(($start + 1))
    done
done
