# On fait une minimisation least square
M_SCM_final = kmpfit.Fitter(residuals=residual_SCM, data=(H0DL_final,y_DH_bis,vFe_bis,color_bis,err_y_DH_bis))
M_SCM_final.fit(params0=p_SCM)
mag_SCM_final=[M_SCM_final.params[0],M_SCM_final.params[1],M_SCM_final.params[2]]
err_alpha=M_SCM_final.stderr[1]
err_beta=M_SCM_final.stderr[2]
#On calcule l erreur avec les erreurs sur alpha

err_mag_SCM_final=sqrt(np.array(err_y_DH_bis)**2+(mag_SCM_final[1]*np.array(err_vFe_bis)/(log(10)*np.array(vFe_bis)))**2+(mag_SCM_final[2]*np.array(err_color_bis))**2)

# On va faire une iteration pour calculer de nouveau la valeur de beta avec les nouvelles erreurs sur la magnitude
M_SCM_final_new =kmpfit.Fitter(residuals=residual_SCM, data=(H0DL_final,y_DH_bis,vFe_bis,color_bis,err_mag_SCM_final))
M_SCM_final_new.fit(params0=p_SCM)
mag_SCM_final_new=[M_SCM_final_new.params[0],M_SCM_final_new.params[1],M_SCM_final_new.params[2]]
err_alpha_new=M_SCM_final_new.stderr[1]
err_beta_new=M_SCM_final_new.stderr[2]

#magnitude AvG+KC+SCM
err_mag_SCM_final_new=sqrt(np.array(err_y_DH_bis)**2+(mag_SCM_final_new[1]*np.array(err_vFe_bis)/(log(10)*np.array(vFe_bis)))**2+(mag_SCM_final_new[2]*np.array(err_color_bis))**2)

#On veut que le nouveau alpha et ZP soient convergents a 0.001 pres
maxiter=100
while True :
	if (abs(mag_SCM_final[0]-mag_SCM_final_new[0])<0.001) or (abs(mag_SCM_final[1]-mag_SCM_final_new[1])<0.001) or (abs(mag_SCM_final[2]-mag_SCM_final_new[2])<0.001): break

	maxiter = maxiter - 1
	if maxiter <= 0:
		print >>sys.stderr, "Did not converge."
		break

	err_mag_SCM_final_new=sqrt(np.array(err_y_DH_bis)**2+(mag_SCM_final_new[1]*np.array(err_vFe_bis)/(log(10)*np.array(vFe_bis)))**2+(mag_SCM_final_new[2]*np.array(err_color_bis))**2)

	#on pose les nouvelles comme les anciennes valeurs
	mag_SCM_final=[M_SCM_final_new.params[0],M_SCM_final_new.params[1],M_SCM_final_new.params[2]]
	#on calcul de nouveau toutes les variable
	M_SCM_final_new =kmpfit.Fitter(residuals=residual_SCM, data=(H0DL_final,y_DH_bis,vFe_bis,color_bis,err_mag_SCM_final_new))
	M_SCM_final_new.fit(params0=p_SCM)
	mag_SCM_final_new=[M_SCM_final_new.params[0],M_SCM_final_new.params[1],M_SCM_final_new.params[2]]
	err_alpha_SCM_new=M_SCM_final_new.stderr[1]
	err_beta_SCM_new=M_SCM_final_new.stderr[2]


#magnitude corrigee par MW, KC et par alpha vFe
y_SCM_FINAL=(y_DH_bis)+M_SCM_final_new.params[1]*log10(np.array(vFe_bis))-M_SCM_final_new.params[2]*np.array(color_bis)
err_y_SCM_FINAL=sqrt(np.array(err_y_DH_bis)**2+(mag_SCM_final_new[1]*np.array(err_vFe_bis)/(log(10)*np.array(vFe_bis)))**2+(mag_SCM_final_new[2]*np.array(err_color_bis))**2)

ZP_AKAS_SCM=mag_SCM_final_new[0] 
M_abs_SCM=ZP_AKAS_SCM+5*log10(H0)-25
err_M_abs_SCM=M_SCM_final_new.stderr[0]
mu_M_AKAS_SCM=y_SCM_FINAL-M_abs_SCM
err_mu_M_AKAS_SCM=sqrt(np.array(err_y_SCM_FINAL)**2+(err_M_abs_SCM)**2+(np.array(err_z_final)*(5*(1+np.array(z_final))*1.0/(np.array(z_final)*(1+np.array(z_final)*1.0/2)*log(10))))**2)

RMS_finale_SCM=sqrt(sum((mu_th-mu_M_AKAS_SCM)**2)*1.0/(size(mu_M_AKAS_SCM)-3))

print (str('############################################################'))
print (str('Correction SCM!!!'))
print ('ZP: '+str(ZP_AKAS_SCM)) 
print ('err ZP: '+str(M_SCM_final_new.stderr[0]))
print ('alpha: '+str(M_SCM_final_new.params[1])) 
print ('err alpha: '+str(err_alpha_SCM_new)) 
print ('beta: '+str(M_SCM_final_new.params[2])) 
print ('err beta: '+str(err_beta_SCM_new)) 
print ('M abs: '+str(M_abs_SCM)) 
print ('err M abs: '+str(err_M_abs_SCM)) 
print ('Dispersion avec correction SCM '+ str(RMS_finale_SCM))


