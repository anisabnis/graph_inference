#!/bin/bash

start=1
filelines=`cat subset.txt`
networks=(att dfn)
intnodes=(3 1)

for i in {0..1}; do
    for line in $filelines; do
	./script_partial_psm.sh ${networks[${i}]} 3 $line $start 
	start=$(($start + 1))
    done
done
