import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os
import csv
import pathlib
#36 Total Samples of Non-Diseased Patients
list_of_nd=['ENCFF166SFX.tsv', 'ENCFF325VHJ.tsv', 'ENCFF707GIJ.tsv', 'ENCFF284VFV.tsv', 'ENCFF586KEK.tsv','ENCFF589PEM.tsv', 'ENCFF742RKK.tsv', 'ENCFF884HHH.tsv', 'ENCFF354MPI.tsv','ENCFF762VOE.tsv', 'ENCFF872OGS.tsv','ENCFF687GJE.tsv','ENCFF574KNI.tsv', 'ENCFF725USM.tsv', 'ENCFF588RXF.tsv', 'ENCFF992KRW.tsv', 'ENCFF594WID.tsv', 'ENCFF345KPY.tsv','ENCFF822OZH.tsv', 'ENCFF468ZUM.tsv', 'ENCFF259IAM.tsv', 'ENCFF108ZQE.tsv', 'ENCFF780QZB.tsv', 'ENCFF361FBY.tsv', 'ENCFF201RLT.tsv', 'ENCFF823FJI.tsv', 'ENCFF042XFA.tsv','ENCFF213NBT.tsv', 'ENCFF094UQH.tsv', 'ENCFF621QOF.tsv', 'ENCFF808SYD.tsv', 'ENCFF905NDM.tsv', 'ENCFF248LJB.tsv', 'ENCFF389KXF.tsv', 'ENCFF693QKW.tsv','ENCFF203FBD.tsv']
list_of_dnorm=['ENCFF479KNI.tsv','ENCFF863VLR.tsv','ENCFF282AKI.tsv','ENCFF016SIN.tsv','ENCFF041HBD.tsv','ENCFF128CDN.tsv','ENCFF190RSI.tsv','ENCFF191XON.tsv','ENCFF204SPU.tsv','ENCFF248BUD.tsv','ENCFF258FWH.tsv','ENCFF269MUV.tsv','ENCFF294WML.tsv','ENCFF324OWT.tsv','ENCFF342TEJ.tsv','ENCFF417ERE.tsv','ENCFF420LNV.tsv','ENCFF509MZI.tsv','ENCFF563JCI.tsv','ENCFF570NEW.tsv','ENCFF614VLQ.tsv','ENCFF658HZK.tsv','ENCFF677FGG.tsv','ENCFF717NTL.tsv','ENCFF738TVC.tsv','ENCFF770BLB.tsv','ENCFF787TLF.tsv','ENCFF845ONN.tsv','ENCFF847QGH.tsv','ENCFF879JZU.tsv','ENCFF899PWS.tsv','ENCFF899VMA.tsv','ENCFF912LYR.tsv','ENCFF952AHW.tsv','ENCFF962YZZ.tsv']
readsdi_tpm = []
readsnd_tpm = []#
readsnd_tpm2 = []
readsmild_tpm = []
readsdnorm_tpm = []
readscogimp_tpm = []

#j=input('Final File Name:')

#For Loop Compiled Data Funcion

#for i in list_of_dnorm:
    #df = np.loadtxt('/Users/andrewyu/Downloads/Diseased Normal/'+i, dtype = str)
    #readsnd_tpm_temp=[]
    #for i in range(len(df[1:,6])):
        #readsnd_tpm_temp.append(float(df[1:,6][i]))
    #readsnd_tpm.append(readsnd_tpm_temp)
#x=zip(*readsnd_tpm)
#file_fin = open(j,'w')
#writer=csv.writer(file_fin,delimiter='\t')
#writer.writerows(x)

for i in range(len(list_of_dnorm)):
    df = pd.read_table('/Users/andrewyu/Downloads/Diseased Normal/ENCFF479KNI.tsv',dtype = str)
    print(df.loc[6876])

# plotting Histogram of Gene Disribution:

# plt.hist(float_lists,log = True, bins=100)
# plt.xlabel('log10+1 FPKM')
# plt.ylabel('Frequency')
# plt.show()

#Plotting The Histogram Using Pandas

#Non-Logorithmic Distribution Histograms
#data = pd.read_table('/Users/andrewyu/Downloads/ENCFF282AKI.tsv')
#floated_data = data['FPKM'].astype(float)
#log_data_dn = np.log10(data['FPKM']+1)
#plt.hist(log_data_dn, log = True, bins = 100)
#plt.show()



#Compiled Data Gene Distribution:

folder_path = '/Users/andrewyu/Downloads/'
file_list = glob.glob(os.path.join(folder_path + "/*.tsv"))
main_dataframe = pd.concat((pd.read_table(f) for f in file_list))

#Number of Files
#file = []
#folder_path = '/Users/andrewyu/Downloads/Control Data'
#for f in glob.glob(folder_path+"/*.tsv"):
    #file.append(f)


#Logorithmic Distribution Histograms
#data = pd.read_table('/Users/andrewyu/Downloads/ENCFF201RLT.tsv')
#floated_data = data['FPKM'].astype(float)
#log10_data = np.log10(data['FPKM']+1)
#plt.hist(log10_data, log = True, bins = 100)
#plt.xlabel('log10 FPKM')
#plt.ylabel('Frequency')
#plt.show()


#df = np.loadtxt('/Users/andrewyu/Downloads/ENCFF863VLR.tsv', dtype = str)
#for i in range(len(df[1:,6])):
    #readsnd_tpm.append(float(df[1:,6][i]))

#total_read = sum(readsnd_tpm)
#float_lists = []
#for i in range(len(readsnd_tpm)):
    #float_lists.append(math.log10(readsnd_tpm[i]+1))

#plotting Histogram of Gene Disribution:

#plt.hist(float_lists,log = True, bins=100)
#plt.xlabel('log10+1 FPKM')
#plt.ylabel('Frequency')
#plt.show()