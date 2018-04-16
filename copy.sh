#!/bin/bash

networks=(6et1 tata sinet columbus geant5 bandcon bics integra rnp sanet dfn surfnet colt evolink)
#networks=(att colt evolink)

for n in ${networks[@]}; do
    echo $n;
    cp results_distance/$n/original.png /Users/asabnis/Dropbox/DarpaEdgeCT/Papers/Graph-Inference/figures/${n}_orig.png 
    cp results_distance/$n/inferred.png /Users/asabnis/Dropbox/DarpaEdgeCT/Papers/Graph-Inference/figures/${n}_distance.png 
    cp results_covariance/$n/inferred.png /Users/asabnis/Dropbox/DarpaEdgeCT/Papers/Graph-Inference/figures/${n}_covariance.png 
    cp results_trees/$n/inferred.png /Users/asabnis/Dropbox/DarpaEdgeCT/Papers/Graph-Inference/figures/${n}_tree.png 
done