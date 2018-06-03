#!/bin/bash

#networks=(6et1 tata sinet columbus bandcon bics rnp sanet dfn surfnet colt evolink)
#intnodes=(3 3 1 2 1 2 1 1 1 3 1 1)

networks=(integra)
intnodes=(3)

for i in {0..0}; do
    ./script_rd.sh ${networks[${i}]} ${intnodes[${i}]};
done