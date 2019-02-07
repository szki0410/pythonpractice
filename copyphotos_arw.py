# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 06:08:45 2019

@author: imawi
"""

import os
import shutil
import re

MY_DIR='D:\\'
DEST_DIR='photos'

dcntr = 0
fcntr = 0

files = os.listdir(MY_DIR)
pat = r"arw$"

for root, dirs, files in os.walk(MY_DIR):
    for file in files:
        ext = re.search(pat, file, re.IGNORECASE)
        
        if ext:
            fpath = os.path.join(root, file)
            
            #コピー先のフォルダ名！
            dpath = os.path.join(DEST_DIR, "copied")
            
            if os.path.isdir(dpath) == False:
                os.mkdir(dpath)
                dcntr += 1
            
            if os.path.isfile(os.path.join(dpath, file)) == False:
                print(fpath)
                shutil.copy(fpath, dpath)
                fcntr += 1
            
print('Directory Created: ' + str(dcntr) + ', Files Copied: ' + str(fcntr))