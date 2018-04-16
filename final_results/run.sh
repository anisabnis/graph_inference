#!/bin/bash

networks=(6et1 tata sinet columbus geant5 bandcon bics integra rnp sanet dfn surfnet att colt evolink)
#networks=(att colt evolink)

for n in ${networks[@]}; do
    mkdir covariance/${n}/
    cp ../results_covariance/${n}/original.png covariance/${n}/
    cp ../results_covariance/${n}/inferred.png covariance/${n}/
done