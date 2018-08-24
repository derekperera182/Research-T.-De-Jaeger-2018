#### DATA host
data_host=np.loadtxt('HostCSP',usecols=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]).transpose()
MB_host=data_host[0]
err_MB_host=data_host[1]
Mu_host=data_host[2]
err_Mu_host=data_host[3]
Mg_host=data_host[4]
err_Mg_host=data_host[5]
Mr_host=data_host[6]
err_Mr_host=data_host[7]
Mi_host=data_host[8]
err_Mi_host=data_host[9]
Mz_host=data_host[10]
err_Mz_host=data_host[11]
Mstellar_host=data_host[12]
err_Mstellar_host=data_host[13]

host_param=[MB_host,Mu_host,Mr_host,Mi_host,Mz_host,Mstellar_host]
err_host_param=[err_MB_host,err_Mu_host,err_Mr_host,err_Mi_host,err_Mz_host,err_Mstellar_host]
name_host_param=['MB host','Mu host','Mr host','Mi host','Mz host','Mstellar host']

name_SN_host=np.array(np.genfromtxt('HostCSP',usecols=[0],dtype='str'))


for n in range(size(name_host_param)):
	x_plot=[]
	err_x_plot=[]
	y_plot=[]
	err_y_plot=[]
	n_params=n
	for i in range(size(residuals_HD)):
		for j in range(size(name_SN_host)):
			if (name_SN_host[j]==table_bis[i]) and (host_param[n_params][j]!=999.9):
				x_plot.append(residuals_HD[i])
				err_x_plot.append(err_residuals_HD[i])
				y_plot.append(host_param[n_params][j])
				err_y_plot.append(err_host_param[n_params][j])

	from scipy.stats.stats import pearsonr
	r_pearson=pearsonr(x_plot,y_plot)		

	f,(ax1)=subplots(1,sharex=True,sharey=False)
	f.subplots_adjust(hspace=0.0)
	ax1.errorbar(y_plot,x_plot,xerr=err_y_plot,yerr=err_x_plot,marker='o',color='k',markersize=10,linestyle='None')

	ax1.text(0.68, 0.85,r'$N_{\mathrm{SNe}}$ = %s'%size(x_plot),horizontalalignment='center',verticalalignment='center',color='black',fontsize=20,transform = ax1.transAxes)
	ax1.text(0.70, 0.75,r'$r$ = %s'%(round(r_pearson[0],2)),horizontalalignment='center',verticalalignment='center',color='black',fontsize=20,transform = ax1.transAxes)

	ax1.set_ylabel(r'residuals_HD [mag]',fontsize=30,fontweight='bold')
	ax1.set_xlabel(r'%s '%(name_host_param[n_params]),fontsize=30,fontweight='bold')
	tick_params(axis='both', which='major', labelsize=23)
	ax1.minorticks_on()
	for tick in ax1.yaxis.get_major_ticks():
		tick.label.set_weight('bold')
	for tick in ax1.xaxis.get_major_ticks():
		tick.label.set_weight('bold')
	ax1.tick_params(axis='x', pad=10)
	savefig('Figures/%s.png'%name_host_param[n_params])
	#show()
	close("all")


