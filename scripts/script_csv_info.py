#!/usr/bin/python3
import re
import csv
import sys
import pandas as pd
import os 

working_directory= os.path.normpath(os.getcwd())

if not os.path.exists("Reports"):
    os.makedirs("Reports")

def read_log_file (path_of_log_files):
    match_list=["lut       ","  dff       ","_DFF_N_    ","_DFF_P_    ","=== ","real	"]
    desin_name=list()
    desin_name.append('None')
    lut_list =list()
    lut_list.append(0)
    dff_list=list()
    dff_list.append(0)
    dff_n_list=list()
    dff_n_list.append(0)
    dff_p_list=list()
    dff_p_list.append(0)
    run_time=list()
    run_time.append(0)
    with open(path_of_log_files, "r") as file:
        line_data=file.readlines()
        for line in line_data:
            for required in match_list:
                if re.search(required,line):
                    splited_line=line.split()
                    if required==match_list[0]:
                        lut_list.append(splited_line[1])
                    elif required==match_list[1]:
                        dff_list.append(splited_line[1])
                    elif required==match_list[2]:
                        dff_n_list.append(splited_line[1])
                    elif required==match_list[3]:
                        dff_p_list.append(splited_line[1])
                    elif required==match_list[4]:
                        desin_name.append(splited_line[1])
                    elif required==match_list[5]:
                        run_time.append(splited_line[1])
    with open(working_directory+"/Reports/designs_info.csv", "a+") as csvfile:
         writer = csv.writer(csvfile) 
         writer.writerow([desin_name[len(desin_name)-1], dff_list[len(dff_list)-1], lut_list[len(lut_list)-1], dff_n_list[len(dff_n_list)-1], dff_p_list[len(dff_p_list)-1], run_time[len(run_time)-1]] )
         desin_name*=0
         dff_list*=0
         lut_list*=0
         dff_n_list*=0
         dff_p_list*=0 
         run_time*=0

with open(working_directory+"/logs/designs_info.csv", "w") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(['Design','DFF','LUT','DFF_N','DFF_P','Tool Runtime'])
print ("-------------------------------------------\n")
print ("--- CSV Report Generated Successfully!  ---\n")
print ("---      Reports/designs_info.csv       ---\n")
print ("-------------------------------------------\n")

for file in os.listdir(working_directory+"/logs"):
    # Check whether file is in log format or not
    if file.endswith(".log"):
        path_of_log_files =file
        read_log_file(working_directory+"/logs/"+path_of_log_files)
