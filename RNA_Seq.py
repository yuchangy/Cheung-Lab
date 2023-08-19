import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#list of files
list_of_nd=['ENCFF166SFX.tsv', 'ENCFF325VHJ.tsv', 'ENCFF707GIJ.tsv', 'ENCFF284VFV.tsv', 'ENCFF586KEK.tsv','ENCFF589PEM.tsv', 'ENCFF742RKK.tsv', 'ENCFF884HHH.tsv', 'ENCFF354MPI.tsv','ENCFF762VOE.tsv', 'ENCFF872OGS.tsv','ENCFF687GJE.tsv','ENCFF574KNI.tsv', 'ENCFF725USM.tsv', 'ENCFF588RXF.tsv', 'ENCFF992KRW.tsv', 'ENCFF594WID.tsv', 'ENCFF345KPY.tsv','ENCFF822OZH.tsv', 'ENCFF468ZUM.tsv', 'ENCFF259IAM.tsv', 'ENCFF108ZQE.tsv', 'ENCFF780QZB.tsv', 'ENCFF361FBY.tsv', 'ENCFF201RLT.tsv', 'ENCFF823FJI.tsv', 'ENCFF042XFA.tsv','ENCFF213NBT.tsv', 'ENCFF094UQH.tsv', 'ENCFF621QOF.tsv', 'ENCFF808SYD.tsv', 'ENCFF905NDM.tsv', 'ENCFF248LJB.tsv', 'ENCFF389KXF.tsv', 'ENCFF693QKW.tsv','ENCFF203FBD.tsv']
list_of_dnorm=['ENCFF479KNI.tsv','ENCFF863VLR.tsv','ENCFF282AKI.tsv','ENCFF016SIN.tsv','ENCFF041HBD.tsv','ENCFF128CDN.tsv','ENCFF190RSI.tsv','ENCFF191XON.tsv','ENCFF204SPU.tsv','ENCFF248BUD.tsv','ENCFF258FWH.tsv','ENCFF269MUV.tsv','ENCFF294WML.tsv','ENCFF324OWT.tsv','ENCFF342TEJ.tsv','ENCFF417ERE.tsv','ENCFF420LNV.tsv','ENCFF509MZI.tsv','ENCFF563JCI.tsv','ENCFF570NEW.tsv','ENCFF614VLQ.tsv','ENCFF658HZK.tsv','ENCFF677FGG.tsv','ENCFF717NTL.tsv','ENCFF738TVC.tsv','ENCFF770BLB.tsv','ENCFF787TLF.tsv','ENCFF845ONN.tsv','ENCFF847QGH.tsv','ENCFF879JZU.tsv','ENCFF899PWS.tsv','ENCFF899VMA.tsv','ENCFF912LYR.tsv','ENCFF952AHW.tsv','ENCFF962YZZ.tsv']
list_of_cogimp = ['ENCFF624FHC.tsv', 'ENCFF072DPH.tsv', 'ENCFF312WUT.tsv']
list_of_dcogimp = ['ENCFF180CEK.tsv', 'ENCFF469DDY.tsv', 'ENCFF970MGQ.tsv']
list_of_mildcogimp = ['ENCFF539RBY.tsv', 'ENCFF285PGS.tsv', 'ENCFF385ZWK.tsv']
#lists for all the Calculated Values:
readsnd_fpkm_apoe = []
readsnd_fpkm_beta_actin = []
readsdnorm_fpkm_apoe = []
readsdnorm_fpkm_beta_actin = []
#Floated List of the Results:


#for d patients without cog impaired
for i in range(len(list_of_dnorm)):
    df = np.loadtxt('/Users/andrewyu/Downloads/Diseased Normal/'+ list_of_dnorm[i],dtype=str)
    APOE_id = 'ENSG00000130203.9'
    Beta_actin_id = 'ENSG00000075624'
    print(df[1:,0])
    for i in range (1, len(df[:,])):
        if APOE_id == df[:,0][i]:
            readsdnorm_fpkm_apoe.append(df[:,6][i])
        elif Beta_actin_id == df[:,0][i]:
            readsdnorm_fpkm_beta_actin.append(df[:,6][i])

#for nd patients:
floated_control_list = []

for i in range(len(list_of_nd)):
    df = np.loadtxt('/Users/andrewyu/Downloads/Control Data/'+ list_of_nd[i],dtype=str)
    APOE_id = 'ENSG00000130203.9'
    #print(df[1:,0])
    for i in range (1, len(df[:,])):
        if APOE_id == df[:,0][i]:
            readsnd_fpkm_apoe.append(df[:,6][i])
        elif Beta_actin_id == df[:,0][i]:
            readsnd_fpkm_beta_actin.append(df[:,6][i])

print(readsdnorm_fpkm_beta_actin)
print(readsnd_fpkm_beta_actin)
print(readsnd_fpkm_apoe)
print(readsdnorm_fpkm_apoe)
#box_comparisons = pd.DataFrame('Box 1')

#boxplot_beta_actin = pd.DataFrame(({'Box 1': readsnd_fpkm_beta_actin, 'Box 2': readsdnorm_fpkm_beta_actin} ))
#ax = boxplot_beta_actin[['Box 1', 'Box 2']].plot(kind = 'box', title = 'Beta-Actin FPKM')

#plt.show()
