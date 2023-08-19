import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats as st
from bioinfokit.analys import get_data
import statistics
import math
#file=np.genfromtxt('test.dat')
#filedf = pd.read_table('Diseased.dat')
#log_file = np.log10(filedf+1)
#boxplot = plt.boxplot(log_file)
#plt.xlabel('Samples')
#plt.ylabel('log10 FPKM')
#plt.show()

df_control = pd.read_table('non_diseased.dat')
df_diseased = pd.read_table('Diseased.dat')


#APOE_row_diseased = df_diseased.iloc[6876]
#APOE_row_control = df_control.iloc[6876]
#data_APOE = pd.DataFrame({"Patients": APOE_row_diseased, "Control": APOE_row_control})
#data_APOE_df = data_APOE.melt(var_name = 'Samples', value_name = 'FPKM')
#sns.boxplot(x = 'Samples', y = 'FPKM', data = data_APOE_df)
#sns.stripplot(x = 'Samples', y = 'FPKM', data = data_APOE_df, color = 'black')
#plt.show()

#Beta_actin_row = df_diseased.iloc[1969]
#Beta_actin_row_diseased = df_diseased.iloc[1964]
#Beta_actin_row_control = df_control.iloc[1964]
#data_Beta_actin = pd.DataFrame({"Patients": Beta_actin_row_diseased, "Control": Beta_actin_row_control})
#data_df = data_Beta_actin.melt(var_name = 'Samples', value_name = 'FPKM')
#sns.boxplot(x = 'Samples', y = 'FPKM',data = data_df)
#sns.stripplot( x = "Samples", y = 'FPKM', data = data_df, color = 'black')
#plt.show()

#plotting a normal graph with
APOE_row_control = df_control.iloc[6876]
n = len(APOE_row_control)
mean = sum(APOE_row_control) / n
deviation = [(x - mean)**2 for x in APOE_row_control]

variance = sum(deviation)/n
print(variance)

APOE_row_diseased = df_diseased.iloc[6876]
n2 = len(APOE_row_diseased)
mean2 = sum(APOE_row_diseased)/ n
deviation2 = [(x-mean)**2 for x in APOE_row_diseased]
variance = sum(deviation)/n
print(variance)

#t-test for the APOE between the two groups:

#APOE_row_control = df_control.iloc[6876]
#APOE_row_diseased = df_diseased.iloc[6876]
#ttest = (st.ttest_ind(APOE_row_control,APOE_row_diseased,equal_var = True))
#print(ttest)

