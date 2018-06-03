#!/bin/bash

networks=(6et1 tata sinet columbus bandcon bics rnp sanet dfn surfnet colt evolink)

for n in ${networks[@]}; do
    echo $n;
    ./script.sh ${n} 3 ;    
done