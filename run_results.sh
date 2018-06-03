#!/bin/bash

#networks=(6et1 tata sinet columbus bandcon rnp sanet dfn surfnet colt evolink integra)
networks=(6et1 tata sinet columbus bandcon bics rnp sanet colt evolink surfnet dfn)
for n in ${networks[@]}; do
    python calc_metrics.py results_psm_dist/${n} f
done