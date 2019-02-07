# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 06:08:45 2019

@author: imawi
"""

import os
import shutil
import datetime
import re

MY_DIR='photos'
#DEST_DIR='C:/Users/imawi/Desktop'
DEST_DIR=MY_DIR
files = os.listdir('photos')
pat = r"arw$|jpg$"
dcntr = 0
fcntr = 0

for file in files:
    ext = re.search(pat, file, re.IGNORECASE)
    
    if ext:
        fpath = os.path.join(MY_DIR, file)      
        mtime = os.stat(fpath).st_mtime       
        #mtime = os.path.getatime(fpath)
        dt = datetime.datetime.fromtimestamp(mtime)
        dpath = os.path.join(DEST_DIR, ext.group() + dt.strftime('%Y%m%d'))
        
        if os.path.isdir(dpath) == False:
            os.mkdir(dpath)
            dcntr += 1
        
        if os.path.isfile(os.path.join(dpath, file)) == False:
            shutil.copy(fpath, dpath)
            fcntr += 1
            
print('Directory Created: ' + str(dcntr) + ', Files Copied: ' + str(fcntr))