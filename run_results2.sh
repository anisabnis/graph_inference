#!/bin/bash

n=$1
for i in {1..63}; do
    python calc_metrics.py results_best_cov/${n}${i} f ${i}
done