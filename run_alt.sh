#!/bin/bash

networks=(6et1 tata sinet columbus geant5 bandcon bics integra rnp sanet dfn surfnet att colt evolink)
#networks=(bics integra rnp sanet dfn surfnet att colt evolink)
int_nodes=(3 3 1 3 4 1 1 3 1 1 1 3 1 1 1)
#int_nodes=(3 1 1 1 3 1 1)
networks=(evolink)
int_nodes=(1)

for i in {0..0}; do
    for n in {0..6}; do
	./script_alt.sh ${networks[$i]} ${int_nodes[$i]} $n;    
    done
done