#!/bin/bash

dir=$1
for ntrees in {1..100}; do
    python gen_dot2.py results_trees/$dir/output/$ntrees
    fdp results_trees/$dir/output/$ntrees/orig.dot -Tpng -o results_trees/$dir/output/$ntrees/original.png
done