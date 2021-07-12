#!/usr/bin/python3
import os
import subprocess
import shutil
import fileinput
import re

designs_dict = {}

#get the working directory
working_directory= os.path.normpath(os.getcwd())
print(working_directory)
a_file = open(working_directory+"/designs/designs.txt")

for line in a_file:
    if (line.strip() == ""):
        continue
    else:
        key, value = line.split(',')
        designs_dict[key] = value.strip()
a_file.close()
#make log dir
if not os.path.exists("logs"):
    os.makedirs("logs")
ys_fname="ys_script.ys"

#designs = ["sdc_controller", "ac97_top"]
for design in designs_dict:
    design_top=designs_dict[design]
    design_fname=design

    #copy related yosys file to the design folder
    shutil.copy(working_directory+'/scripts/'+ys_fname,working_directory+'/designs/'+design_top)
    #cd design folder
    os.chdir(working_directory+'/designs/'+design_top)

    #replce design top module and file
    
    fin = open(working_directory+'/scripts/'+ys_fname, "rt")
    data = fin.read()
    data = data.replace('design_top', design_top)
    fin.close()
    fin = open(ys_fname, "wt")
    fin.write(data)
    fin.close()
    fin = open(ys_fname, "rt")
    data = fin.read()
    data = data.replace('design_file.v', design_fname)
    fin.close()
    fin = open(ys_fname, "wt")
    fin.write(data)
    fin.close()
    if(design_top != "ac97_top"):
        fin = open(ys_fname, "rt")
        data = fin.read()
        data = data.replace('-nomem2reg', '')
        fin.close()
        fin = open(ys_fname, "wt")
        fin.write(data)
        fin.close()
    #yosys sim
    yosy_sim_cmd = ('script -c "time yosys "'+ys_fname+' '+working_directory+'/logs/'+design_top+'.log')
    subprocess.call(yosy_sim_cmd,shell=True,executable='/bin/bash')

    # remove yosys script from design folder after execution
    rm_ys = ('rm '+ys_fname)
    subprocess.call(rm_ys,shell=True,executable='/bin/bash')
