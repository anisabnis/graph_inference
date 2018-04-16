import sys, os

#networks=["6et1", "tata", "sinet", "columbus", "geant5", "bandcon", "bics", "integra", "rnp", "sanet", "dfn", "surfnet", "colt", "evolink"]
networks =["sinet"]
for n in networks:
    for i in range(7):
        ## cp command for no_edits
        os.system("cp /media/sf_asabnis/final/edgect/merge/divide_and_conq/tree_formulation/results_alt_distances/" + n + "/" + str(i) + "/no_edits .")
        
        os.system("cp /media/sf_asabnis/final/edgect/merge/divide_and_conq/tree_formulation/results_alt_distances/" + n + "/" + str(i) + "/mapping.txt .")
        
        f=open("no_edits", "r")
        no_edits = int(f.readline().strip())
        ## read no edits file 
        ## cp command for running genresult.sh command: pass as argument network and no edit
        os.system("./genresult.sh " + str(n) + str(i) + " " + str(no_edits))
         
