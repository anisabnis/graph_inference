#!/bin/bash

networks=(columbus tata surfnet integra)

for n in ${networks[@]}; do
    for i in {1..2}; do
	./script_random.sh ${n} 3 $i
    done
done