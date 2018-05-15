import sys
import os

networks = ["6et1", "tata", "sinet", "columbus", "geant5", "bandcon", "bics", "integra", "rnp", "sanet", "dfn", "surfnet", "att", "colt", "evolink"]
#networks = ["tata"]
enclaves = [6,6,6,6,5,5,6,5,5,5,6,5,6,6,6]
all_enclaves = ['a', 'b', 'c', 'd', 'e', 'f'] 


for i in range(len(networks)):
    
    ## Copy input files
    os.system("./prepare_dir.sh " + networks[i])
    
    ## generate correlations
    os.system("python gen_tree.py " + networks[i])
    
    ## Run the optimization to get results
    for j in range(enclaves[i]):
        os.system("mkdir results_tree_algorithm/" + networks[i] + "/" + str(all_enclaves[j]) + "/")
        os.system("cp results_distance/" + networks[i] + "/graph.txt results_tree_algorithm/" + networks[i] + "/" + str(all_enclaves[j]) + "/")
        #os.system("cp results_distance/" + networks[i] + "/orig_path.txt results_tree_algorithm/" + networks[i] + "/" + str(all_enclaves[j]) + "/")
        #os.system("cp results_deter/" + networks[i] + "/results.txt results_deter/" + networks[i] + "/" + str(all_enclaves[j]) + "/correlations.txt")
        os.system("./script_tree_alg.sh " + networks[i] + " " + str(3) + " " + str(all_enclaves[j]))


    