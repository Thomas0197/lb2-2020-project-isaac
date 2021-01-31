import numpy as np
from numpy import savetxt
import os
import sys

def Train(WindowSize, input_file, output):
    ws = int(WindowSize)
    HArray=np.zeros((ws,20))
    #Array containing the counts for positions -((ws-1)//2) to +((ws-1)//2) for each residue belonging to H ss.
    EArray=np.zeros((ws,20))
    #Array containing the counts for positions -((ws-1)//2) to +((ws-1)//2) for each residue belonging to E ss.
    CArray=np.zeros((ws,20))
    #Array containing the counts for positions -((ws-1)//2) to +((ws-1)//2) for each residue belonging to C ss.
    RArray=np.zeros((ws,20))
    #Array containing the counts for positions -((ws-1)//2) to +((ws-1)//2) for each residue belonging to any ss.
    numfiles=0

    TP = np.zeros((9,20))
    Rp = np.zeros((3,20))
    lengthSeq=0
    SStotal = 0
    C=0;H=0;E=0;X=0
    
    
    with open(input_file,"r")as ids:
        input_file = ids.readlines()
		
        for file_name in input_file:
            file_name= file_name.rstrip()
                
            numfiles +=1
            pdbID = file_name[:-4]
            m = np.loadtxt("/home/thomas/Documents/Lab2Project/SeqProfile/SeqProfilesTraining/"+ pdbID+ ".txt")
    
            seqprof = open("/home/thomas/Documents/Lab2Project/SeqProfile/SeqProfilesTraining/"+pdbID+".txt", "r")
            proflines=seqprof.readlines()
    
            f = open("/home/thomas/Documents/Lab2Project/SeqProfile/TrainingDssp/"+pdbID+".dssp", "r")
            lines = f.readlines()[1:]
            for line in lines:
                line = line.rstrip()
                SS = line
                #print(SS)
                lengthSeq += len(SS)
    
            for i in SS:
                if i == "-":
                    C += 1
                elif i == "H":
                    H +=1
                elif i == "E":
                    E += 1
                elif i == "X":
                    x +=1
    
    
            f.close()
    
            for linenum in range(0, len(proflines)):
                        Arrayind=-1
                        if SS[linenum]=="-":
                            for i in range(((ws-1)//2),-((ws-1)//2)-1,-1):
                                Arrayind+=1
                                if (linenum-i)>=0 and (linenum-i)<len(proflines):
                                    profline=proflines[linenum-i].rstrip().split()
                                    #print(profline)
                                    #print(Arrayind)
                                    for j in range(0,len(profline)):
                                        CArray[Arrayind,j]+=float(profline[j])/len(proflines)
                                        RArray[Arrayind,j]+=float(profline[j])/len(proflines)
    
                        elif SS[linenum]=="H":
                            for i in range(((ws-1)//2),-((ws-1)//2)-1,-1):
                                Arrayind+=1
                                if (linenum-i)>=0 and (linenum-i)<len(proflines):
                                    profline=proflines[linenum-i].rstrip().split()
                                    #print(profline)
                                    #print(Arrayind)
                                    for j in range(0,len(profline)):
                                        HArray[Arrayind,j]+=float(profline[j])/len(proflines)
                                        RArray[Arrayind,j]+=float(profline[j])/len(proflines)
    
                        else:
                            for i in range(((ws-1)//2),-((ws-1)//2)-1,-1):
                                Arrayind+=1
                                if (linenum-i)>=0 and (linenum-i)<len(proflines):
                                    profline=proflines[linenum-i].rstrip().split()
                                    #print(profline)
                                    #print(Arrayind)
                                    for j in range(0,len(profline)):
                                        EArray[Arrayind,j]+=float(profline[j])/len(proflines)
                                        RArray[Arrayind,j]+=float(profline[j])/len(proflines)
            SStotal += lengthSeq
            H = H/SStotal
            C = C/SStotal
            E = E/SStotal
    #print(CArray/numfiles,HArray/numfiles,EArray/numfiles,RArray/numfiles)
    path = os.getcwd()
    path = path+"/"+output
    try:
    	os.mkdir(path)
    except OSError:
    	print ("Creation of the directory %s failed" % path)
    else:
    	print ("Successfully created the directory %s " % path)

    savetxt(path+"/HArray.csv",HArray,delimiter=",")
    savetxt(path+"/CArray.csv",CArray,delimiter=",")
    savetxt(path+"/EArray.csv",EArray,delimiter=",")
    savetxt(path+"/RArray.csv",RArray,delimiter=",")
    return (CArray/numfiles,HArray/numfiles,EArray/numfiles,RArray/numfiles)
    

if __name__ == "__main__":
    windowsize=sys.argv[1]
    input_file=sys.argv[2]
    output=sys.argv[3]
    Model=Train(windowsize, input_file, output)
    print(Model)

