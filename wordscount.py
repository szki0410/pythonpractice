# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 08:59:42 2019

@author: imawi

textフォルダー内の単語の出現回数を数える
"""
import os
import re

OUTPUT_FILE = 'text/hinan/kekka.txt'
files = os.listdir('text')
pat = r".txt$"

if os.path.isfile(OUTPUT_FILE):
    os.remove(OUTPUT_FILE)

for file in files:
    ext = re.search(pat, file, re.IGNORECASE)
    
    if ext and ext.group() == '.txt':
        
        print(file)
        
        with open('text/' + file) as f:
            #正規表現で何とかする
            text = f.read()
            #text = re.sub(';|:|,|\.|\"|\(|\)|\[|\]|\'|/', '', text)
            
            text = re.sub('[!-/:-@[-`{-~]', '', text)
            '''
            text = text.replace(";", "")
            text = text.replace(":", "")
            text = text.replace(",", "")
            text = text.replace(".", "")
            text = text.replace("\"", "")
            text = text.replace("(", "")
            text = text.replace(")", "")
            text = text.replace("[", "")
            text = text.replace("]", "")
            text = text.replace("\'", "")
            text = text.replace("\'", "")
            text = text.replace("/", "")
            '''
            words = text.split()
                
            counter = {}
                
        for w in words:
            ws = w.lower()
            if ws in counter:
                counter[ws] += 1
            else:
                counter[ws] = 1
        
        """
        print(file + ':') 
        for k, v in counter.items():
            if v >= 1:
                print(k, v)
        print()
        """       
            
        with open(OUTPUT_FILE, 'a') as f:
            f.write(file + ':\n' ) 
            for k, v in sorted(counter.items(), key=lambda x: x[1], reverse=True):
                f.write(k + ' ' + str(v) + '\n')
            f.write('\n')