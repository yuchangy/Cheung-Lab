import numpy as np
import matplotlib.pyplot as plt

list_of_nd=['ENCFF166SFX.tsv','ENCFF325VHJ.tsv', 'ENCFF707GIJ.tsv']
list_of_dnorm=['ENCFF479KNI.tsv','ENCFF863VLR.tsv','ENCFF282AKI.tsv']
list_of_cogimp = ['ENCFF624FHC.tsv', 'ENCFF072DPH.tsv', 'ENCFF312WUT.tsv']
list_of_dcogimp = ['ENCFF180CEK.tsv', 'ENCFF469DDY.tsv', 'ENCFF970MGQ.tsv']
list_of_mildcogimp = ['ENCFF539RBY.tsv', 'ENCFF285PGS.tsv', 'ENCFF385ZWK.tsv']
readsdi_tpm = []
readsnd_tpm = []
readsmild_tpm = []
readsdnorm_tpm = []
readscogimp_tpm = []

for i in range(len(list_of_mildcogimp)):
    df = np.loadtxt('/Users/andrewyu/Downloads/'+ list_of_mildcogimp[i],dtype=str)
    APOE_id = 'ENSG00000130203.9'
    #print(df[1:,0])
    for i in range (1, len(df[:,])):
        if APOE_id == df[:,0][i]:
            readsmild_tpm.append(df[:,6][i])
        #elif APOE_id == df[:,0][i]:
            #readsmild_tpm.append(df[:,5][i])

float_readsmild = []
for item in readsmild_tpm:
    float_readsmild.append(float(item))

print(float_readsmild)
#calculating Standard Deviation:

    #mean = sum(float_readsmild)/len(readsmild_tpm)

    #differences = [(x-mean)** 2 for x in float_readsmild]

    #sum_of_differences = sum(differences)

    #standard_deviation = (sum_of_differences/len(readsmild_tpm)-1) ** 0.5

    #print(standard_deviation)

    #Calculating Z-Score:

   # zscores =[(x-mean)/standard_deviation for x in float_readsmild]

   # print(zscores)

    #creating a histogram of the distribution of genes:

    #x = zscores

   # plt.hist(x, bins = 1)

   # plt.show()



