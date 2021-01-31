import numpy as np
import math
import argparse
import sys
import os

#l1=[]
#Sequ = "VYALG"


#seqprof = open("/home/thomas/Documents/Lab2Project/SeqProfile/SeqProfiles150/6EEL_A.txt", "r")
#proflines=seqprof.readlines()


def Prediction(input_file, outFolder):

    with open(input_file,"r")as ids:
        input_file = ids.readlines()
		
        for file_name in input_file:
            file_name= file_name.rstrip()
            prof_id = file_name[:-4]
            
            HArray = np.genfromtxt('HArray.csv',delimiter=',')
            CArray = np.genfromtxt('CArray.csv',delimiter=',')
            EArray = np.genfromtxt('EArray.csv',delimiter=',')
            RArray = np.genfromtxt('RArray.csv',delimiter=',')
            with open("/home/thomas/Documents/Lab2Project/SeqProfile/SeqProfilesTraining/" + file_name, "r") as file_n:
                proflines=file_n.readlines()
            
                ss = ''
                ws =17
            
                for linenum in range(0, len(proflines)):
                    Arrayind=-1
                    PHelix = 0
                    PCoil = 0
                    PStrand = 0
                    SSprediction=0
                    FreqHelix=0
                    FreqCoil=0
                    FreqStrand=0
                    for i in range(((ws-1)//2),-((ws-1)//2)-1,-1):
                        Arrayind+=1
                        if (linenum-i)>=0 and (linenum-i)<len(proflines):
                            #print(Arrayind)
                            #print(count)
                            profline=proflines[linenum-i].rstrip().split()
                            for j in range(0,len(profline)):
                                FreqHelix += HArray[Arrayind][j]
                                FreqCoil += CArray[Arrayind][j]
                                FreqStrand += EArray[Arrayind][j]
                            for j in range(0,len(profline)):
                                #letter = profline[i]
                                #print(letter)
                                #iNum = dic.get(letter)
                                FreqHelixPosition = HArray[Arrayind][j]#probabilty of helix for that letter in that window
                                FreqCoilPosition = CArray[Arrayind][j]#probabilty of Coil for that letter in that window
                                FreqStrandPosition = EArray[Arrayind][j]#probabilty of Strand for that letter in that window
                                #print(HArray[count][iNum])
                                #print(H)
            
            
            
            
                                FreqLetterPosition = RArray[Arrayind][j]
            
                                #print(FreqLP)
                                PCoil+=float(profline[j])*math.log(FreqCoilPosition/(FreqCoil)*(FreqLetterPosition))
                                #PCoil+=float(profline[iNum])*math.log(FreqLetterPosition/(C)*(FreqCoilPosition))#prediction number for coil
                                PHelix+= float(profline[j])*math.log(FreqHelixPosition/(FreqHelix)*(FreqLetterPosition))
                                #PHelix+= float(profline[iNum])*math.log(FreqLetterPosition/(H)*(FreqHelixPosition))
                                PStrand+=float(profline[j])*math.log(FreqStrandPosition/(FreqStrand)*(FreqLetterPosition))#prediction number for strand
                                #PStrand+=float(profline[iNum])*math.log(FreqLetterPosition/(E)*(FreqStrandPosition))
            
            
                            #print("A")
                            #print(PHelix)
                            #print(PCoil)
                            #print(PStrand)
            
                    SSprediction = max(PCoil, PHelix, PStrand)
                    if SSprediction == 0.0:
                        ss += "C"
                        #l1.append("C")
                        #print(SSprediction)
                    elif SSprediction == PHelix:
                        ss +="H"
                        #l1.append("H")
                        #print(SSprediction)
                    elif SSprediction == PStrand:
                        ss+= "E"
                        #l1.append("E")
                        #print(SSprediction)
                    else:
                        ss+="C"
                        #l1.append("C")
                        #print(SSprediction)
                   
                #print(*l1, sep='')
                print(prof_id)
                print(ss)
                
                with open(outFolder+"/"+prof_id+".txt","w")as outfile:
                    outfile.write(">"+prof_id+":Predicted"+"\n")
                    outfile.write(ss+"\n")


        

if __name__ == "__main__":
    input_file=sys.argv[1]
    outFolder=sys.argv[2]
    
    Prediction(input_file, outFolder) 
  
