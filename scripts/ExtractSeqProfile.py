#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:15:49 2020

@author: thomas
"""
import os

def Readsome():
    
    for file in os.listdir("/home/thomas/Documents/Lab2Project/SeqProfile/Psi150"):
        with open("/home/thomas/Documents/Lab2Project/SeqProfile/Psi150/"+file,"r") as fl:
            pdbID = file[:-5]
            
            Pssm = open("/home/thomas/Documents/Lab2Project/SeqProfile/SeqProfiles150/"+pdbID +"txt" ,"x")
                      
            lines = fl.readlines()[3:-6]
           
            for line in lines:
                line = line.rstrip()
                LineList = line.split()
                    #print(LineList[20:-2])
                    
                Norm = []
                for i in LineList[22:-2]:
                    u = float(i)/100
                    Norm.append(u)
                for i in Norm:
                    Pssm.write(str(i) + " ")
                Pssm.write("\n")
                    #print(LineList[0:2] + Norm)
                    
            Pssm.close()
Readsome()
