################## On charge les valeurs de Hbeta #########################
dir=os.getcwd()+'/V_Hbeta/v_Hbeta_CSP/'
files=os.listdir(dir)  #liste les fichiers
files.sort()  #tri alphabetique
nfiles=size(files)

name_Hbeta_csp=[]
for i in range(nfiles):
	if files[i].endswith('snid.dat'):  #on selectionne
		name_Hbeta_csp.append(str.split(files[i],'.')[0])
ntable_csp=size(name_Hbeta_csp)
epoch_Hbeta_csp=[]
Ve_Hbeta_csp=[]
err_Ve_Hbeta_csp=[]
for i in range(ntable_csp):
	data_Hbeta=np.loadtxt('V_Hbeta/v_Hbeta_CSP/%s.dat'%name_Hbeta_csp[i]).transpose()
	epoch_Hbeta_csp.append(data_Hbeta[0]*1.0/(1+redshift_csp[i]))
	Ve_Hbeta_csp.append(data_Hbeta[1])
	err_Ve_Hbeta_csp.append(data_Hbeta[2])


v_Hbeta_func=[0]*ntable_csp
err_v_Hbeta_func=[0]*ntable_csp
power_law_tot_csp=[]
coeff_tot_csp=[]
pw1=[8000]
epoch_fit=np.arange(10,135,3)

for i in range(ntable_csp):
	power_law=[]
	coeff=[]
	if (size(Ve_Hbeta_csp[i])>=2) and (epoch_Hbeta_csp[i][0]!=epoch_Hbeta_csp[i][1]):
		for MC in range(N_MC):
			epoch_MC=epoch_Hbeta_csp[i]
			Ve_Hbeta_csp_MC=Ve_Hbeta_csp[i]
			err_Ve_Hbeta_csp_MC=err_Ve_Hbeta_csp[i]

			y_final_MC_ini=[]
			x_final_MC_ini=[]
			for t in range(size(Ve_Hbeta_csp[i])):	
				xerr_MC_ini=0#(err_JD_explosion[i]*(random(1)*2-1)[0]) # valeur aleatoire
				yerr_MC_ini=(err_Ve_Hbeta_csp[i][t]*(random(1)*2-1)[0]) # valeur aleatoire
				y_final_MC_ini.append((yerr_MC_ini+Ve_Hbeta_csp[i][t]))
				x_final_MC_ini.append((xerr_MC_ini+epoch_Hbeta_csp[i][t]))

			# Compute the median of the non-zero elements
			# Assign the median to the zero elements 
			err_Ve_Hbeta_csp[i][where(np.array(err_Ve_Hbeta_csp[i]) == 0)[0]]=np.median(err_Ve_Hbeta_csp[i][err_Ve_Hbeta_csp[i] > 0])

			fitobj = kmpfit.Fitter(residuals=power_law_vel, data=(x_final_MC_ini,y_final_MC_ini,err_Ve_Hbeta_csp[i]))
			fitobj.fit(params0=pw0)			
			power_law.append(fitobj.params[1])
			coeff.append(fitobj.params[0])
		close("all")

		power_law_tot_csp.append(power_law)
		coeff_tot_csp.append(coeff)


	elif (size(Ve_Hbeta_csp[i])<2) and  (epoch_Hbeta_csp[i]!=0):

		f,(ax1)=subplots(1,sharex=True,sharey=False)
		f.subplots_adjust(hspace=0.0)
		for MC in range(N_MC):
			epoch_MC=epoch_Hbeta_csp[i]
			Ve_Hbeta_csp_MC=Ve_Hbeta_csp[i]
			err_Ve_Hbeta_csp_MC=err_Ve_Hbeta_csp[i]

			y_final_MC_ini=[]
			x_final_MC_ini=[]
			for t in range(size(Ve_Hbeta_csp[i])):	
				xerr_MC_ini=0#(err_JD_explosion[i]*(random(1)*2-1)[0]) # valeur aleatoire
				yerr_MC_ini=(err_Ve_Hbeta_csp[i]*(random(1)*2-1)[0]) # valeur aleatoire
				y_final_MC_ini.append((yerr_MC_ini+Ve_Hbeta_csp[i]))
				x_final_MC_ini.append((xerr_MC_ini+epoch_Hbeta_csp[i]))

			fitobj = kmpfit.Fitter(residuals=power_law_A, data=(x_final_MC_ini,y_final_MC_ini))
			fitobj.fit(params0=pw1)

			power_law.append(gamma_csp)
			coeff.append(fitobj.params[0])


		power_law_tot_csp.append(power_law)
		coeff_tot_csp.append(coeff)

	elif (size(Ve_Hbeta_csp[i])<=2)  and (epoch_Hbeta_csp[i]==0):	
		power_law_tot_csp.append(N_MC*[0])
		coeff_tot_csp.append(N_MC*[0])

### On Calcule les erreurs ####
err_Ve_FINAL_csp=np.zeros((ntable_csp,size(epoch_fit)))
Ve_FINAL_csp=np.zeros((ntable_csp,size(epoch_fit)))
v_Hbeta_func_csp=[0]*ntable_csp
err_v_Hbeta_func_csp=[0]*ntable_csp
for i in range(ntable_csp):
	if (size(Ve_Hbeta_csp[i])>=2) and (epoch_Hbeta_csp[i][0]!=epoch_Hbeta_csp[i][1]):
		for t in range(size(epoch_fit)):
			v_tot=[]
			for n in range(N_MC):
				v_tot.append(coeff_tot_csp[i][n]*((epoch_fit[t])**power_law_tot_csp[i][n]))
			err_Ve_FINAL_csp[i,t]=max(v_tot)-median(v_tot)
			Ve_FINAL_csp[i,t]=median(v_tot)

		v_Hbeta_func_csp[i]=interpolate.interp1d(epoch_fit,Ve_FINAL_csp[i,:]*1.0/5000)
		err_v_Hbeta_func_csp[i]=interpolate.interp1d(epoch_fit,err_Ve_FINAL_csp[i,:]*1.0/5000)

	elif (size(Ve_Hbeta_csp[i])<2)  and (epoch_Hbeta_csp[i]!=0):

		gamma=median(power_law_tot_csp[i])
		err_gamma=0.18
		for t in range(size(epoch_fit)):
			Ve_FINAL_csp[i,t]=median(coeff_tot_csp[i])*((epoch_fit[t])**median(power_law_tot_csp[i]))
			err_Ve_FINAL_csp[i,t]=mean(sqrt((np.array(err_Ve_Hbeta_csp[i])*((np.array(epoch_Hbeta_csp[i])/epoch_fit[t])**-gamma))**2+(np.array(Ve_Hbeta_csp[i])*((np.array(epoch_Hbeta_csp[i])/epoch_fit[t])**-gamma)*log((np.array(epoch_Hbeta_csp[i])/epoch_fit[t])*err_gamma)**2)))


		v_Hbeta_func_csp[i]=interpolate.interp1d(epoch_fit,Ve_FINAL_csp[i,:]*1.0/5000)
		err_v_Hbeta_func_csp[i]=interpolate.interp1d(epoch_fit,err_Ve_FINAL_csp[i,:]*1.0/5000)
	elif (size(Ve_Hbeta_csp[i])<2) and (epoch_Hbeta_csp[i]==0):
		for t in range(size(epoch_fit)):
			v_tot=[]
			for n in range(N_MC):
				v_tot.append(999.9)
			err_Ve_FINAL_csp[i,t]=std(0.0)
			Ve_FINAL_csp[i,t]=mean(0.0)
		v_Hbeta_func_csp[i]=0
		err_v_Hbeta_func_csp[i]=0
