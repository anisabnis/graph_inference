#!/bin/bash

networks=(bics rnp sanet dfn surfnet evolink att)

for i in {0..6}; do
    ./script_psm.sh ${networks[${i}]} 1;
done