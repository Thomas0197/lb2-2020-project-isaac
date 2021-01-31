#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:15:49 2020

@author: thomas
"""
import os

#Retrieves secondary structure from DSSP files and also creates new fasta files
def Readsome():
    Dic = { "H": "H", "G": "H", "I": "H", "B": "E", "E": "E", "T": "C", "S": "C", " ": "C"}
    
    for file in os.listdir("/home/thomas/Documents/Lab2Project/BlastpOnCluster/DsspWholePdb"):
        with open("/home/thomas/Documents/Lab2Project/BlastpOnCluster/DsspWholePdb/"+file,"r") as fl:
            
        
            pdbID = file[:-5]
            pdbHead = pdbID[:4]
            chain = pdbID[-1:]
            
            
            dssp = open("/home/thomas/Documents/Lab2Project/BlastpOnCluster/150dssp/"+pdbID +".txt" ,"x")
            fasta = open("/home/thomas/Documents/Lab2Project/BlastpOnCluster/150Fasta/"+pdbID +".fasta" ,"x")
            
            
            dssp.write(">" +pdbHead+":"+chain +"\n")
            fasta.write(">" +pdbHead+":"+chain +"\n")
            lines = fl.readlines()[28:]
            for line in lines:
                line = line.rstrip()
                if line[16] in Dic and line[11] == chain:
                     dssp.write(Dic[line[16]])
                    
                if line[13] == "!" and line[11] == chain:
                     fasta.write("X")
                elif line[13] == "!*" and line[11] == chain:
                    print("\n" + "Something went wrong!")
                elif line[11] == chain:
                    fasta.write(line[13])
            dssp.close()
            fasta.close()
    
Readsome()
