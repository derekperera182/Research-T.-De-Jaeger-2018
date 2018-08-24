#xy_final_csp = color chosen
phase_xy_final_csp=[]
xy_final_csp=[]
err_xy_final_csp=[]

color_func_csp=[0]*N_csp
err_color_func_csp=[0]*N_csp

for i in range(N_csp):
	if (size(x1_final_csp[i])>1) and (size(y1_final_csp[i])>1):

		#epoque en commun
		indx_y=where((phase_y1_final_csp[i]>=min(phase_x1_final_csp[i])) & (phase_y1_final_csp[i]<=max(phase_x1_final_csp[i])))[0]

		#epoque final
		phase_xy_final_csp.append(np.array(phase_y1_final_csp[i])[indx_y])
		#Couleur X-Y pour les epoques communes moins le host (X-Ah_X)-(Y-Ah_Y)
		x_y=(np.array(x1_csp[i](np.array(phase_y1_final_csp[i])[indx_y])))-(np.array(np.array(y1_final_csp[i])[indx_y]))
		#erreur sur X
		x_erreur=np.array(x1_err_csp[i](np.array(phase_y1_final_csp[i])[indx_y]))-np.array(x1_csp[i](np.array(phase_y1_final_csp[i])[indx_y]))
		#erreur sur Y
		y_erreur=np.array(y1_err_csp[i](np.array(phase_y1_final_csp[i])[indx_y]))-np.array(y1_csp[i](np.array(phase_y1_final_csp[i])[indx_y]))
		#erreur final sur la couleur
		err_xy_final_csp.append(sqrt((x_erreur)**2+(y_erreur)**2))

		#Couleur finale
		xy_final_csp.append(x_y)
	else:
		phase_xy_final_csp.append(0)
		err_xy_final_csp.append(0)
		xy_final_csp.append(0)


	### On interpole les couleurs #####
	if (size(xy_final_csp[i])>1):
		color_func_csp[i]=interpolate.interp1d(phase_xy_final_csp[i],xy_final_csp[i])
		err_color_func_csp[i]=interpolate.interp1d(phase_xy_final_csp[i],err_xy_final_csp[i])
