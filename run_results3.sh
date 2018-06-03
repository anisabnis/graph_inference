#!/bin/bash

n=$1
for i in {1..5}; do
    python calc_metrics.py results_random_err2/${n}/${i} t ${i}
done