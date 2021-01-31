#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 00:50:47 2020

@author: thomas
"""
import requests



def some(filepath):
    
    PdbList = open(filepath , "r")
    for line in PdbList:
        line = line.rstrip()
        LineList = line.split(":")
        pdbID = LineList[0]
        chain = LineList[1]
 
    
        url = 'https://files.rcsb.org/download/'+ pdbID +'.pdb'
        r = requests.get(url, allow_redirects=True)
    
        open(pdbID+'_'+chain+'.Wholepdb', 'wb').write(r.content)
        
        
        
        pdb = open(pdbID+'_'+chain+'.Wholepdb', "r")
        #lines = pdb.readline()
        #linesStrip = lines.rstrip()
        
        
        #pdbID = linesStrip[-4:].lower()
    
        f = open("/home/thomas/Documents/Lab2Project/After Blastp/PdbFiles/"+pdbID + "_" + chain + ".pdb" ,"x")
        for line in pdb:
            line = line.rstrip()
            if "SSBOND" in line:
                f.write(line + "\n")
            if (line.startswith("ATOM") or line.startswith("ANISOU") or line.startswith("HETATM") or line.startswith("TER")) and line[21] == chain:
                f.write(line + "\n")
        f.write("END")
        f.close()
    
            
    
    
some("/home/thomas/Documents/lab2project/testing/WholePdbs/150pdb.txt")