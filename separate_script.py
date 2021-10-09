# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 15:05:09 2021

@author: 16028
"""

import argparse
import random
import string
import os
import sys
import subprocess
from datetime import datetime

base_os = os.getcwd()
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--N', dest='N', required=True,
                        help='Full path to the training file')

    args = parser.parse_args()
    num_dir = int(args.N)
    
    
    ###############################################
    #piping date from command line
    today_date = os.popen('echo %date%').read()
    
    
    base_path = r'C:\Users\16028\Downloads\4302_hw1' 
    dir_list = os.listdir(base_path) 
    for i in range(num_dir):
        
        
        folder_name = 'folder_' + str(i+1)
        # print(folder_name)
        full_path = base_path + '\\' + folder_name
        if not os.path.exists(full_path):
            # print(full_path)
            os.makedirs(full_path)
    
        input_path = full_path + '\\' + 'input\\'
        if not os.path.exists(input_path):
            # print(input_path)
            os.makedirs(input_path)
            
        output_path = full_path + '\\' + 'output\\' 
        if not os.path.exists(output_path):
            # print(output_path)
            os.makedirs(output_path)
            
         
    # Creates a new file
        os.chdir(full_path)
        tmp = os.popen("dir").read()
        os.chdir(base_os)

        with open(full_path + '\\' + 'log.txt', 'w') as fp:
            fp.write(today_date) #print("I have a question.", file=f)
            fp.write("\n")
            fp.write(tmp)
        with open(input_path + '\\' + 'data.txt', 'w') as fp:
            pass
        with open(output_path + '\\' + 'solution.txt', 'w') as fp:
            pass
        # To write data to new file uncomment
        # this fp.write("New file created")

# dbro = os.popen("date").read()   

# Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])
# =============================================================================
# ls = subprocess.Popen(["dir",full_path + '\\' + 'log.txt', ],stdout=subprocess.PIPE)
# lines = [line.rstrip('\n') for line in ls.stdout]
# 
# with open(full_path + '\\' + 'log.txt') as f:
#     print(f.read())
#  =============================================================================
# print(base_path)
# proc = subprocess.Popen(["python", input_path,'dir'], stdout=subprocess.PIPE, shell=True)
# tmp4 = proc.stdout.read()
# lg = subprocess.Popen(r'c:\mytool\tool.exe', cwd=r'd:\test\local')



