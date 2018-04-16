import os
#a = ["tata", "quest", "sinet", "geant"]
a = ["uninet"]
for di in a:
    #os.system("mkdir ./full_knowledge/" + di)
    os.system("mkdir " + di + "1")
    os.system("cp /media/sf_asabnis/final/edgect/merge/divide_and_conq/final_results/destination_tree/covariance/" + di + "/output.tar.gz "  + di + "1/")
    os.system("cd " + di + "1 ; tar -xvzf output.tar.gz; cd ../")
    os.system("python3 convert.py " + di + "1/" + di + "/output/")
    os.system("./script.sh " + di +"1/" + di + "/")
