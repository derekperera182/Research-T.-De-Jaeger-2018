import sys # system commands
import string as string # string functions4
import math
import numpy as np # numerical tools

'''

Sert a choisir les filtres et a charger toutes les donnees

'''
filtre=['B','V','g','r','i']
print('Filter available: ' +str(filtre))
x11=input("Input first filter color:  B,V,g,r,i  ")
y11=input("Input second filter color:  B,V,g,r,i  ")

y12=input("Choice filter magnitude:  B,V,g,r,i  ")

if x11==str('B'):
	x1_csp=B_band_func_csp
	x1_err_csp=B_band_func_plus_csp
	phase_x1_final_csp=phase_X_final_csp[0]	
	x1_final_csp=X_final_csp[0]
	err_x1_final_csp=err_X_final_csp[0]
	x1_name=filtre[0]

elif x11==str('V'):
	x1_csp=V_band_func_csp
	x1_err_csp=V_band_func_plus_csp
	phase_x1_final_csp=phase_X_final_csp[1]	
	x1_final_csp=X_final_csp[1]
	err_x1_final_csp=err_X_final_csp[1]
	x1_name=filtre[1]

elif x11==str('g'):
	x1_csp=g_band_func_csp
	x1_err_csp=g_band_func_plus_csp
	phase_x1_final_csp=phase_X_final_csp[2]	
	x1_final_csp=X_final_csp[2]
	err_x1_final_csp=err_X_final_csp[2]

	x1_name=filtre[2]

elif x11==str('r'):
	x1_csp=r_band_func_csp
	x1_err_csp=r_band_func_plus_csp
	phase_x1_final_csp=phase_X_final_csp[3]	
	x1_final_csp=X_final_csp[3]
	err_x1_final_csp=err_X_final_csp[3]
	x1_name=filtre[3]

elif x11==str('i'):
	x1_csp=i_band_func_csp
	x1_err_csp=i_band_func_plus_csp
	phase_x1_final_csp=phase_X_final_csp[4]	
	x1_final_csp=X_final_csp[4]
	err_x1_final_csp=err_X_final_csp[4]

	x1_name=filtre[4]

if y11==str('B'):
	y1_csp=B_band_func_csp
	y1_err_csp=B_band_func_plus_csp
	phase_y1_final_csp=phase_X_final_csp[0]	
	y1_final_csp=X_final_csp[0]
	err_y1_final_csp=err_X_final_csp[0]
	y1_name=filtre[0]

elif y11==str('V'):
	y1_csp=V_band_func_csp
	y1_err_csp=V_band_func_plus_csp
	phase_y1_final_csp=phase_X_final_csp[1]	
	y1_final_csp=X_final_csp[1]
	err_y1_final_csp=err_X_final_csp[1]
	y1_name=filtre[1]

elif y11==str('g'):
	y1_csp=g_band_func_csp
	y1_err_csp=g_band_func_plus_csp
	phase_y1_final_csp=phase_X_final_csp[2]	
	y1_final_csp=X_final_csp[2]
	err_y1_final_csp=err_X_final_csp[2]
	y1_name=filtre[2]


elif y11==str('r'):
	y1_csp=r_band_func_csp
	x1_err_csp=r_band_func_plus_csp
	phase_y1_final_csp=phase_X_final_csp[3]	
	y1_final_csp=X_final_csp[3]
	err_y1_final_csp=err_X_final_csp[3]
	y1_name=filtre[3]

elif y11==str('i'):
	y1_csp=i_band_func_csp
	y1_err_csp=i_band_func_plus_csp
	phase_y1_final_csp=phase_X_final_csp[4]	
	y1_final_csp=X_final_csp[4]
	err_y1_final_csp=err_X_final_csp[4]
	y1_name=filtre[4]

if y12==str('B'):
	y2_csp=B_band_func_csp
	y2_err_csp=B_band_func_plus_csp
	phase_y2_final_csp=phase_X_final_csp[0]	
	y2_final_csp=X_final_csp[0]
	err_y2_final_csp=err_X_final_csp[0]
	y2_name=filtre[0]

elif y12==str('V'):
	y2_csp=V_band_func_csp
	y2_err_csp=V_band_func_plus_csp
	phase_y2_final_csp=phase_X_final_csp[1]	
	y2_final_csp=X_final_csp[1]
	err_y2_final_csp=err_X_final_csp[1]
	y2_name=filtre[1]

elif y12==str('g'):
	y2_csp=g_band_func_csp
	y2_err_csp=g_band_func_plus_csp
	phase_y2_final_csp=phase_X_final_csp[2]	
	y2_final_csp=X_final_csp[2]
	err_y2_final_csp=err_X_final_csp[2]
	y2_name=filtre[2]


elif y12==str('r'):
	y2_csp=r_band_func_csp
	x1_err_csp=r_band_func_plus_csp
	phase_y2_final_csp=phase_X_final_csp[3]	
	y2_final_csp=X_final_csp[3]
	err_y2_final_csp=err_X_final_csp[3]
	y2_name=filtre[3]

elif y12==str('i'):
	y2_csp=i_band_func_csp
	y2_err_csp=i_band_func_plus_csp
	phase_y2_final_csp=phase_X_final_csp[4]	
	y2_final_csp=X_final_csp[4]
	err_y2_final_csp=err_X_final_csp[4]
	y2_name=filtre[4]

