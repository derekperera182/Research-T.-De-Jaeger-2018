#############################################################################################################
#
#
#                                        CSP !!!!!!!!!!!!!!!
#
#
#############################################################################################################


## DATA CSP ###########
data_csp=np.loadtxt('Data_all_SNe_CSP.dat',usecols=[1,2,3,4,5,6,7,8,9,10,11]).transpose()
A_V_csp=data_csp[0]
redshift_csp=data_csp[1]*1.0/c_light
err_redshift_csp=data_csp[2]*1.0/c_light
JD_explosion_csp=data_csp[3]
err_JD_explosion_csp=data_csp[4]
z_CMB_csp=data_csp[9]*1.0/c_light
err_z_CMB_csp=data_csp[10]*1.0/c_light
JD_ref=2453000

name_csp=np.array(np.genfromtxt('Data_all_SNe_CSP.dat',usecols=[0],dtype='str'))
N_csp=size(name_csp)


###### On charge la photometrie CSP apres correction AvG,KC, KS #######
filtre=['B','V','g','r','i']
phase_X_final_csp=[]
X_final_csp=[]
err_X_final_csp=[]


for filtre_name in range(size(filtre)):
	phase_mag_final=[]
	mag_AKAS_final=[]
	err_mag_AKAS_final=[]
	for SN in range(N_csp):
		# Probleme mang KC pour 0 40, 46 bk sub
		mag_txt_csp=np.loadtxt('Corrected_Data_CSP/AvG_KC_Data_CSP/%s_%s.dat' %(name_csp[SN],filtre[filtre_name])).transpose()
		err_mag_txt_csp=np.loadtxt('Corrected_Data_CSP/err_AvG_KC_Data_CSP/%s_%s.dat' %(name_csp[SN],filtre[filtre_name])).transpose()
		if size(mag_txt_csp)!=0:

			phase_mag_final.append(around(mag_txt_csp[0][mag_txt_csp[1]!=999.9]*1.0/(1+redshift_csp[SN]), decimals=2))

			mag_AKAS_final.append(mag_txt_csp[1][mag_txt_csp[1]!=999.9])
			err_mag_AKAS_final.append(sqrt((mag_txt_csp[2][mag_txt_csp[1]!=999.9])**2+(err_mag_txt_csp[3][mag_txt_csp[1]!=999.9]-mag_txt_csp[3][mag_txt_csp[1]!=999.9])**2))


		else:
			phase_mag_final.append([0,0])
			mag_AKAS_final.append([0,0])
			err_mag_AKAS_final.append([0,0])

	phase_X_final_csp.append(phase_mag_final)  #phase
	X_final_csp.append(mag_AKAS_final)   #magnitude
	err_X_final_csp.append(err_mag_AKAS_final) #err magnitude 

# Interpolation magnitude to have it at diferent epoch

B_band_func_csp=[0]*N_csp
B_band_func_plus_csp=[0]*N_csp
V_band_func_csp=[0]*N_csp
V_band_func_plus_csp=[0]*N_csp
g_band_func_csp=[0]*N_csp
g_band_func_plus_csp=[0]*N_csp
r_band_func_csp=[0]*N_csp
r_band_func_plus_csp=[0]*N_csp
i_band_func_csp=[0]*N_csp
i_band_func_plus_csp=[0]*N_csp

for i in range(N_csp):
	if size(phase_X_final_csp[0][i])>1:
		B_band_func_csp[i]=interpolate.interp1d(phase_X_final_csp[0][i],X_final_csp[0][i])
		B_band_func_plus_csp[i]=interpolate.interp1d(phase_X_final_csp[0][i],np.array(X_final_csp[0][i])+np.array(err_X_final_csp[0][i]))

	V_band_func_csp[i]=interpolate.interp1d(phase_X_final_csp[1][i],X_final_csp[1][i])
	V_band_func_plus_csp[i]=interpolate.interp1d(phase_X_final_csp[1][i],np.array(X_final_csp[1][i])+np.array(err_X_final_csp[1][i]))
	g_band_func_csp[i]=interpolate.interp1d(phase_X_final_csp[2][i],X_final_csp[2][i])
	g_band_func_plus_csp[i]=interpolate.interp1d(phase_X_final_csp[2][i],np.array(X_final_csp[2][i])+np.array(err_X_final_csp[2][i]))
	r_band_func_csp[i]=interpolate.interp1d(phase_X_final_csp[3][i],X_final_csp[3][i])
	r_band_func_plus_csp[i]=interpolate.interp1d(phase_X_final_csp[3][i],np.array(X_final_csp[3][i])+np.array(err_X_final_csp[3][i]))
	i_band_func_csp[i]=interpolate.interp1d(phase_X_final_csp[4][i],X_final_csp[4][i])
	i_band_func_plus_csp[i]=interpolate.interp1d(phase_X_final_csp[4][i],np.array(X_final_csp[4][i])+np.array(err_X_final_csp[4][i]))
