from pyexcel_ods import get_data
import json 

data = get_data("CSP-values.ods")
value=json.dumps(data)

param_photo=str.split(value,'Spec50')[0]
## Photo
SN_name=[]
Pdnew=[]
err_Pdnew=[]
OPTd_new=[]
err_OPTd_new=[]	
CDNew=[]
err_CDNew=[]
Mmax=[]
err_Mmax=[]
Mend=[]
err_Mend=[]
Mtail=[]
err_Mtail=[]
s1New=[]
err_s1New=[]
s2New=[]
err_s2New=[]
s3=[]
err_s3=[]
Ni56=[]
err_Ni56=[]
Ni56all=[]
err_Ni56all=[]
n10_20=[]
n10_30=[]
n20_50=[]
M13N2=[]
err_M13N2=[]

for i in range(size(str.split(param_photo,'200'))-1):
	i=i+1

	SN_name.append(str('SN200')+str.split(str.split(str.split(param_photo,'200')[i],',')[0],'"')[0])
	Pdnew.append(float(str.split(str.split(param_photo,'200')[i],',')[1]))
	err_Pdnew.append(float(str.split(str.split(param_photo,'200')[i],',')[2]))
	OPTd_new.append(float(str.split(str.split(param_photo,'200')[i],',')[3]))
	err_OPTd_new.append(float(str.split(str.split(param_photo,'200')[i],',')[4]))	
	CDNew.append(float(str.split(str.split(param_photo,'200')[i],',')[5]))
	err_CDNew.append(float(str.split(str.split(param_photo,'200')[i],',')[6]))
	Mmax.append(float(str.split(str.split(param_photo,'200')[i],',')[7]))
	err_Mmax.append(float(str.split(str.split(param_photo,'200')[i],',')[8]))
	Mend.append(float(str.split(str.split(param_photo,'200')[i],',')[9]))
	err_Mend.append(float(str.split(str.split(param_photo,'200')[i],',')[10]))
	Mtail.append(float(str.split(str.split(param_photo,'200')[i],',')[11]))
	err_Mtail.append(float(str.split(str.split(param_photo,'200')[i],',')[12]))
	s1New.append(float(str.split(str.split(param_photo,'200')[i],',')[13]))
	err_s1New.append(float(str.split(str.split(param_photo,'200')[i],',')[14]))
	s2New.append(float(str.split(str.split(param_photo,'200')[i],',')[15]))
	err_s2New.append(float(str.split(str.split(param_photo,'200')[i],',')[16]))
	s3.append(float(str.split(str.split(param_photo,'200')[i],',')[17]))
	err_s3.append(float(str.split(str.split(param_photo,'200')[i],',')[18]))
	Ni56.append(float(str.split(str.split(param_photo,'200')[i],',')[19]))
	err_Ni56.append(float(str.split(str.split(param_photo,'200')[i],',')[20]))
	Ni56all.append(float(str.split(str.split(param_photo,'200')[i],',')[21]))
	err_Ni56all.append(float(str.split(str.split(param_photo,'200')[i],',')[22]))
	n10_20.append(float(str.split(str.split(param_photo,'200')[i],',')[23]))
	n10_30.append(float(str.split(str.split(param_photo,'200')[i],',')[24]))
	n20_50.append(float(str.split(str.split(param_photo,'200')[i],',')[25]))
	M13N2.append(float(str.split(str.split(param_photo,'200')[i],',')[26]))
	err_M13N2.append(float(str.split(str.split(str.split(param_photo,'200')[i],',')[27],']')[0]))


## Spec
SN_name_spec=[]
HaF=[]
err_HaF=[]
Ham=[]
err_Ham=[]	
Haabs=[]
err_Haabs=[]
Haem=[]
err_Haem=[]
Hb=[]
err_Hb=[]
EWHb=[]
err_EWHb=[]
Fe4=[]
err_Fe4=[]
EWFe4=[]
err_EWFe4=[]
Fe5=[]
err_Fe5=[]
EWFe5=[]
err_EWFe5=[]
Fe6=[]
err_Fe6=[]
EWFe6=[]
err_EWFe6=[]
ScFe=[]
err_ScFe=[]
EWScFe=[]
err_EWScFe=[]
ScM=[]
err_ScM=[]
EWScM=[]
err_EWScM=[]
Na=[]
err_Na=[]
EWNa=[]
err_EWNa=[]
Ba=[]
err_Ba=[]
EWBa=[]
err_EWBa=[]
Sc=[]
err_Sc=[]
EWSc=[]
err_EWSc=[]
VOi=[]
err_VOi=[]
ae=[]
err_ae=[]

param_Spec50=str.split(value,'Spec50')[1]
for i in range(size(str.split(param_photo,'200'))-1):
	i=i+1

	Ham.append(float(str.split(str.split(param_Spec50,'200')[i],',')[3]))
	err_Ham.append(float(str.split(str.split(param_Spec50,'200')[i],',')[4]))	
	Haabs.append(float(str.split(str.split(param_Spec50,'200')[i],',')[5]))
	err_Haabs.append(float(str.split(str.split(param_Spec50,'200')[i],',')[6]))
	Haem.append(float(str.split(str.split(param_Spec50,'200')[i],',')[7]))
	err_Haem.append(float(str.split(str.split(param_Spec50,'200')[i],',')[8]))
	Hb.append(float(str.split(str.split(param_Spec50,'200')[i],',')[9]))
	err_Hb.append(float(str.split(str.split(param_Spec50,'200')[i],',')[10]))
	EWHb.append(float(str.split(str.split(param_Spec50,'200')[i],',')[11]))
	err_EWHb.append(float(str.split(str.split(param_Spec50,'200')[i],',')[12]))
	Fe4.append(float(str.split(str.split(param_Spec50,'200')[i],',')[13]))
	err_Fe4.append(float(str.split(str.split(param_Spec50,'200')[i],',')[14]))
	EWFe4.append(float(str.split(str.split(param_Spec50,'200')[i],',')[15]))
	err_EWFe4.append(float(str.split(str.split(param_Spec50,'200')[i],',')[16]))
	Fe5.append(float(str.split(str.split(param_Spec50,'200')[i],',')[17]))
	err_Fe5.append(float(str.split(str.split(param_Spec50,'200')[i],',')[18]))
	EWFe5.append(float(str.split(str.split(param_Spec50,'200')[i],',')[19]))
	err_EWFe5.append(float(str.split(str.split(param_Spec50,'200')[i],',')[20]))
	Fe6.append(float(str.split(str.split(param_Spec50,'200')[i],',')[21]))
	err_Fe6.append(float(str.split(str.split(param_Spec50,'200')[i],',')[22]))
	EWFe6.append(float(str.split(str.split(param_Spec50,'200')[i],',')[23]))
	err_EWFe6.append(float(str.split(str.split(param_Spec50,'200')[i],',')[24]))
	ScFe.append(float(str.split(str.split(param_Spec50,'200')[i],',')[25]))
	err_ScFe.append(float(str.split(str.split(param_Spec50,'200')[i],',')[26]))
	EWScFe.append(float(str.split(str.split(param_Spec50,'200')[i],',')[27]))
	err_EWScFe.append(float(str.split(str.split(param_Spec50,'200')[i],',')[28]))
	ScM.append(float(str.split(str.split(param_Spec50,'200')[i],',')[29]))
	err_ScM.append(float(str.split(str.split(param_Spec50,'200')[i],',')[30]))
	EWScM.append(float(str.split(str.split(param_Spec50,'200')[i],',')[31]))
	err_EWScM.append(float(str.split(str.split(param_Spec50,'200')[i],',')[32]))
	Na.append(float(str.split(str.split(param_Spec50,'200')[i],',')[33]))
	err_Na.append(float(str.split(str.split(param_Spec50,'200')[i],',')[34]))
	EWNa.append(float(str.split(str.split(param_Spec50,'200')[i],',')[35]))
	err_EWNa.append(float(str.split(str.split(param_Spec50,'200')[i],',')[36]))
	Ba.append(float(str.split(str.split(param_Spec50,'200')[i],',')[37]))
	err_Ba.append(float(str.split(str.split(param_Spec50,'200')[i],',')[38]))
	EWBa.append(float(str.split(str.split(param_Spec50,'200')[i],',')[39]))
	err_EWBa.append(float(str.split(str.split(param_Spec50,'200')[i],',')[40]))
	Sc.append(float(str.split(str.split(param_Spec50,'200')[i],',')[41]))
	err_Sc.append(float(str.split(str.split(param_Spec50,'200')[i],',')[42]))
	EWSc.append(float(str.split(str.split(param_Spec50,'200')[i],',')[43]))
	err_EWSc.append(float(str.split(str.split(param_Spec50,'200')[i],',')[44]))
	VOi.append(float(str.split(str.split(param_Spec50,'200')[i],',')[45]))
	err_VOi.append(float(str.split(str.split(param_Spec50,'200')[i],',')[46]))
	ae.append(float(str.split(str.split(param_Spec50,'200')[i],',')[47]))
	err_ae.append(float(str.split(str.split(str.split(param_Spec50,'200')[i],',')[48],']')[0]))

	SN_name_spec.append(str('SN200')+str.split(str.split(str.split(param_Spec50,'200')[i],',')[0],'"')[0])
	HaF.append(float(str.split(str.split(param_Spec50,'200')[i],',')[1]))
	err_HaF.append(float(str.split(str.split(param_Spec50,'200')[i],',')[2]))

name_params_photo=['Pd','OPTd','Ttrans','Mmax','Mend','Mtail','s1','s2','s3','Ni56']
photo_tot=[Pdnew,OPTd_new,t_trans,Mmax,Mend,Mtail,s1New,s2New,s3,Ni56all]
spec50_tot=[HaF,Haabs,Hb,EWHb,Fe4,EWFe4,Fe5,EWFe5,Fe6,EWFe6,ScFe,EWScFe,ScM,EWScM,Na,EWNa,Ba,EWBa,Sc,EWSc,ae]
err_photo_tot=[err_Pdnew,err_OPTd_new,err_t_trans,err_Mmax,err_Mend,err_Mtail,err_s1New,err_s2New,err_s3,err_Ni56all]

err_spec50_tot=[err_HaF,err_Haabs,err_Hb,err_EWHb,err_Fe4,err_EWFe4,err_Fe5,err_EWFe5,err_Fe6,err_EWFe6,err_ScFe,err_EWScFe,err_ScM,err_EWScM,err_Na,err_EWNa,err_Ba,err_EWBa,err_Sc,err_EWSc,err_ae]
name_params_spec50=['HaF','Haabs','Hb','EWHb','Fe4','EWFe4','Fe5','EWFe5','Fe6','EWFe6','ScFe','EWScFe','ScM','EWScM','Na','EWNa','Ba','EWBa','Sc','EWSc','ae']

