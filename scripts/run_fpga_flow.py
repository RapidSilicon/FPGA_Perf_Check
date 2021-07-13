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

#designs = ["sdc_controller", "ac97_top"]
for design in designs_dict:
    design_top=designs_dict[design]
    design_fname=design
       
    #yosys sim
    yosys_sim_cmd = ('yosys -p "plugin -i ql-qlf; synth_quicklogic -blif './designs'/'+design_top+'/'+design_top+'.blif -family qlf_k4n8 -top '+design_top+'" ./designs/'+design_top+'/'+design_fname+' -l ./logs/'+design_top+'.log')
    subprocess.call(yosys_sim_cmd,shell=True,executable='/bin/bash')


