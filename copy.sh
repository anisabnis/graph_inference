#!/bin/bash

networks=(6et1 tata sinet columbus bandcon bics rnp sanet dfn surfnet colt evolink att integra)

for n in ${networks[@]}; do
    mkdir /Users/asabnis/Dropbox/DarpaEdgeCT/Papers/Graph-Inference/IMC/figures/inferred_networks/${n}
    cp results_distance/${n}/original.png /Users/asabnis/Dropbox/DarpaEdgeCT/Papers/Graph-Inference/IMC/figures/inferred_networks/${n}
    cp results_rd/${n}/inferred.png /Users/asabnis/Dropbox/DarpaEdgeCT/Papers/Graph-Inference/IMC/figures/inferred_networks/${n}/inferred_rd.png
    cp results_psm/${n}/inferred.png /Users/asabnis/Dropbox/DarpaEdgeCT/Papers/Graph-Inference/IMC/figures/inferred_networks/${n}/inferred_psm.png
    cp results_psm_dist/${n}/inferred.png /Users/asabnis/Dropbox/DarpaEdgeCT/Papers/Graph-Inference/IMC/figures/inferred_networks/${n}/inferred_psm_dist.png
    ./script.sh ${n} 3 ;    
done