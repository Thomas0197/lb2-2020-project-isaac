import numpy as np
import math
import sys
            
            

def MCC_matrix(input_file):
    ThreeCM = np.zeros((3,3))
    with open(input_file,"r")as ids:
        input_file = ids.readlines()
        for file_name in input_file:
            file_name= file_name.rstrip()
            dssp_id = file_name[:-4]
            
            with open("/home/thomas/Documents/Lab2Project/SeqProfile/TrainingDssp/"+dssp_id+".dssp","r")as test,open("/home/thomas/Documents/Lab2Project/CV/CV4/predicted/"+file_name ,"r")as predict:

                obv=test.readlines()[1]
                obv=obv.rstrip()
                pred=predict.readlines()[1]
                pred= pred.rstrip()
                
                Dic = {'HH':"00", 'HE':"01", "HC":"02", "EH":"10", "EE":"11", "EC":"12", "CH":"20", "CE":"21", "CC":"22" }
                for i in range(len(pred)):
                    ss = obv[i] + pred[i]
                    if ss in Dic:
                        index = Dic[ss]
                        ThreeCM[int(index[0])][int(index[1])] += 1

    return ThreeCM
        

def Q3(matrix):
    Q3 = (matrix[0,0] + matrix[1,1] + matrix[2,2])/(np.sum(matrix))
    return Q3
    #print("Q3: " + str(Q3))
#Q3(matrix)

def Hmatrix(matrix):
    HCM = np.zeros((2,2))
    HCM[0,0] = matrix[0,0]
    HCM[0,1] = matrix[0,1] + matrix[0,2]
    HCM[1,0] = matrix[1,0] + matrix[2,0]
    HCM[1,1] = matrix[1,1] + matrix[1,2] + matrix[2,1] + matrix[2,2]
    return HCM
    
#Hmatrix(matrix)

def Ematrix(matrix):
    ECM = np.zeros((2,2))
    ECM[0,0] = matrix[1,1]
    ECM[0,1] = matrix[1,0] + matrix[1,2]
    ECM[1,0] = matrix[0,1] + matrix[2,1]
    ECM[1,1] = matrix[0,0] + matrix[0,2] + matrix[2,0] + matrix[2,2]
    return ECM
    
def Cmatrix(matrix):
    CCM = np.zeros((2,2))
    CCM[0,0] = matrix[2,2]
    CCM[0,1] = matrix[2,0] + matrix[2,1]
    CCM[1,0] = matrix[0,2] + matrix[1,2]
    CCM[1,1] = matrix[0,0] + matrix[0,1] + matrix[1,1] + matrix[1,0]

    return CCM
    
def eval(XCM):
    ACC = (XCM[0,0] + XCM[1,1])/(np.sum(XCM))
    SEN = (XCM[0,0])/(XCM[0,0] + XCM[0,1])
    PPV = (XCM[0,0])/(XCM[0,0] + XCM[1,0])
    MCC = (XCM[0,0]*XCM[1,1]-XCM[1,0]*XCM[0,1]) / (math.sqrt((XCM[0,0]+XCM[1,0])*(XCM[0,0] + XCM[0,1])*(XCM[1,1]+XCM[1,0]) * (XCM[1,1] + XCM[0,1])))
    return ACC, SEN, PPV, MCC

if __name__ == "__main__":
    input_file=sys.argv[1]
    matrix = MCC_matrix(input_file)
    
    HCM = Hmatrix(matrix)
    HACC, HSEN, HPPV, HMCC=eval(HCM)
    print("Eval of H: \n" + "ACC: " +str(HACC) + "\n" + "SEN: " + str(HSEN) + "\n" + "PPV: " + str(HPPV) + "\n" + "MCC: " + str(HMCC))

    ECM = Ematrix(matrix)
    EACC, ESEN, EPPV, EMCC= eval(ECM)
    print("Eval of E: \n" + "ACC: " +str(EACC) + "\n" + "SEN: " + str(ESEN) + "\n" + "PPV: " + str(EPPV) + "\n" + "MCC: " + str(EMCC))

    CCM = Cmatrix(matrix)
    CACC, CSEN, CPPV, CMCC= eval(CCM)
    print("Eval of C: \n" + "ACC: " +str(CACC) + "\n" + "SEN: " + str(CSEN) + "\n" + "PPV: " + str(CPPV) + "\n" + "MCC: " + str(CMCC))
    print("\n")
    print("Q3: ", Q3(matrix))
    print("ACC Average: ", ((HACC+EACC+CACC)/3))
    print("MCC Average: ", ((HMCC+EMCC+CMCC)/3))
    print("SEN Average: ", ((HSEN+ESEN+CSEN)/3))
    print("PPV Average: ", ((HPPV+EPPV+CPPV)/3))

