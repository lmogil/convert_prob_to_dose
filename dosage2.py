#!/ usr/bin/python
from __future__ import division
import re
import sys
import csv   
import os
        
#read in csv file with rsid, postion, and info score...
reader = csv.reader(open('/data/hwheeler1/MesaSHARe/Imputation/Generation_3/AFA imputation v.3.afa.1 (1000G)/MESA_SHARe_imputation_AFA_1kg_11202012/SNP_info/quality_imputed/AFA_chr22_1kg_11202012_quality_imputedSNPs.csv', 'rU'), delimiter=",", quotechar='|')

#make lists
column1 =[]
column2 =[]

#pull desired rows (position, info score)
for row in reader:
    column1.append(row[2])
    column2.append(row[7])  

#make info score float     
col2= map(float, column2[1:])

#make dictionary and then filter...if info is greater than 0.3 keep it and store the position
mydict = dict(zip(column1[1:],col2[1:]))
newdict = dict((k, v) for k, v in mydict.items() if v >= 0.3)

idpos = []
#store position of info scores that pass filter
for k, v in newdict.items():
	idpos.append(k)


#import chr impute2 file with probabilities 
data1 = open('/data/hwheeler1/MesaSHARe/Imputation/Generation_3/AFA imputation v.3.afa.1 (1000G)/MESA_SHARe_imputation_AFA_1kg_11202012/imputation_data/imp2_AFA_chr22_ref1kg')



from itertools import izip
def by3(iterable):
	a = iter(iterable)
	return izip(a,a,a)
	
	

doselist1=[]
for row in data1:
	ndata = row.strip().split() 
	#if the position matches the postion stored from above...
	if any(i in ndata for i in idpos):
		#add rsid, position, a1,a2 to list 
		doselist1.append("\n" + str(ndata[1]))
		doselist1.append(ndata[2:5])
		#make decimals float for processing	
		chg_data= ndata[:5] +map(float, ndata[5:])
		#starting at position 6, if adding 3 numbers together meets statement
       	for l, j, k in by3(chg_data[5:]):
			if l+j+k >= 0.9 and l+j+k <= 1.1: 
	#keep...calculate the dose
				dose = j+(2*k)
				doselist1.append(dose)
				#convert to string add to file
				ds = str(doselist1).strip()
				f = open("/data/lmogil/dose_chr22.txt", "w")
				f.write(ds)
f.close()
		
			