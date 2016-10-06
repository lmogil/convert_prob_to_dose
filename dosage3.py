#!/ usr/bin/python
from __future__ import division
import re
import sys
import csv   
import os
import numpy as np
        

reader = csv.reader(open('/data/hwheeler1/MesaSHARe/Imputation/Generation_3/AFA imputation v.3.afa.1 (1000G)/MESA_SHARe_imputation_AFA_1kg_11202012/SNP_info/quality_imputed/AFA_chr22_1kg_11202012_quality_imputedSNPs.csv', 'rU'), delimiter=",", quotechar='|')


column1 =[]
column2 =[]
for row in reader:
    column1.append(row[2])
    column2.append(row[7])  
     
col2= map(float, column2[1:])


mydict = dict(zip(column1[1:],col2[1:]))
newdict = dict((k, v) for k, v in mydict.items() if v >= 0.3)

idpos = []

for k, v in newdict.items():
	idpos.append(k)





data1 = open('/data/hwheeler1/MesaSHARe/Imputation/Generation_3/AFA imputation v.3.afa.1 (1000G)/MESA_SHARe_imputation_AFA_1kg_11202012/imputation_data/imp2_AFA_chr22_ref1kg')



from itertools import izip
def by3(iterable):
	a = iter(iterable)
	return izip(a,a,a)
	
	
doselist=[]
for row in data1:
	ndata = row.strip().split()
	if any(i in ndata for i in idpos):
		doselist= ndata[0:5]
		#print doselist1
		chg_data= ndata[:5] +map(float, ndata[5:])
       	for l, j, k in by3(chg_data[5:]):
			if l+j+k >= 0.9 and l+j+k <= 1.1: 
	#keep...
				dose = j+(2*k)
				doselist.append(dose)
				#doselist1.append(dose)
				#print doselist1
	f = open("dose.txt", "a+")
	f.write('\n'+ str(doselist))
	f.close()	
			
				

			