#!/bin/bash

networks=(6et1 tata sinet columbus geant5 bandcon bics integra rnp sanet dfn surfnet att colt evolink)
#networks=(6et1)
#networks=(tata)
#networks=(geant5)
#networks=(integra rnp sanet dfn surfnet att colt evolink)
#networks=(bandcon)
#networks=(6et1 tata)
#networks=(sanet)

for n in ${networks[@]}; do
    for i in {0..6}; do
	python make_edit.py results_alt_trees/${n}$i 3
	python gen_gedevo_files.py results_alt_trees/${n}$i
	#ls -lrt results_alt_trees/${n}$i/no_edits
    done
done