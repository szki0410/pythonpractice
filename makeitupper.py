# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 08:59:42 2019

@author: imawi

textフォルダー内にあるtxtファイルの文字を大文字にしたコピーをつくりますよ。
"""
import os
import re

files = os.listdir('text')
pat = r".txt$"

for file in files:
    sentence = ''
    ext = re.search(pat, file, re.IGNORECASE)
    
    if ext.group() == '.txt':

        with open('text/' + file) as f:
            for line in f:
                sentence += line.lower()
                
        print(sentence)
        
        with open('text/up_' + file, 'w') as f:
            f.write(sentence)