#!/bin/bash

networks=(columbus tata surfnet integra)

for n in ${networks[@]}; do
    for i in {0..5}; do
	./script_random.sh ${n} 3 $i $i
    done
done