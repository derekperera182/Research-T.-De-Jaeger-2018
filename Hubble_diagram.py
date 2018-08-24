y_SCM_FINAL=(y_DH_bis)+alpha_sol*log10(np.array(vFe_bis))-beta_sol*np.array(color_bis)
err_y_SCM_FINAL=sqrt(np.array(err_y_DH_bis)**2+(alpha_sol*np.array(err_vFe_bis)/(log(10)*np.array(vFe_bis)))**2+(beta_sol*np.array(err_color_bis))**2)

ZP_AKAS_SCM=ZP_sol 
M_abs_SCM=ZP_AKAS_SCM+5*log10(H0)-25
err_M_abs_SCM=err_ZP_sol
mu_M_AKAS_SCM=y_SCM_FINAL-M_abs_SCM
err_mu_M_AKAS_SCM=sqrt(np.array(err_y_SCM_FINAL)**2+(err_M_abs_SCM)**2+(np.array(err_z_final)*(5*(1+np.array(z_final))*1.0/(np.array(z_final)*(1+np.array(z_final)*1.0/2)*log(10))))**2)

size_SN_finale=size(y_SCM_FINAL)

rcParams['legend.numpoints']=1
plt.rcParams['xtick.major.size'] = 11
plt.rcParams['xtick.minor.size'] = 5
plt.rcParams['ytick.major.size'] = 11
plt.rcParams['ytick.minor.size'] = 5
rc('font', weight='bold')
rc('axes', linewidth=2)
rc('text', usetex=True)
params = {'text.usetex': True, 'mathtext.fontset': 'stixsans'}
rcParams.update(params)

text_font = {'fontname':'sans-sherif', 'size':'25', 'color':'black', 'weight':'heavy',
              'verticalalignment':'center','horizontalalignment':'center'}
axis_font = {'fontname':'sans-sherif', 'size':'30','weight':'heavy'}

fig = plt.figure(figsize=(8, 6))
ax0 = plt.subplot2grid((3, 3), (0, 0),colspan=3,rowspan=2)	


ax0.errorbar(np.array(z_final)*c_light,np.array(mu_M_AKAS_SCM),xerr=np.array(err_z_final),yerr=np.array(err_mu_M_AKAS_SCM),marker='o',color='k',markersize=9,linestyle='None',label=r'\textbf{CSP}')


ax0.plot(z_final_test*c_light,mu_th_tot,'r',linewidth=2.0,label=r'\textbf{($\Omega_{m}$=0.3,$\Omega_{\Lambda}$=0.7)}')
ax0.set_ylabel(r'\textbf{$\mu_\mathrm{\textbf{SCM}}$ (mag)}',fontsize=20,fontweight='bold')
ax0.text(0.15, 0.60,r'\textbf{$N_\mathrm{\textbf{SNe}}$ = %s}'%size_SN_finale,horizontalalignment='center',verticalalignment='center',fontsize=17,transform = ax0.transAxes)
ax0.text(0.20, 0.70,r'\textbf{$\sigma_\mathrm{\textbf{obs}}$ = %s mag}'%(round((abs(sig_int_sol)),2)),horizontalalignment='center',verticalalignment='center',fontsize=17,transform = ax0.transAxes)
ax0.text(0.8, 0.10,r'\textbf{Epoch = %s days}'%(X_days),horizontalalignment='center',verticalalignment='center',fontsize=17,transform = ax0.transAxes)
ax0.text(0.8, 0.30,r'\textbf{i band}',horizontalalignment='center',verticalalignment='center',fontsize=17,transform = ax0.transAxes)
ax0.text(0.8, 0.20,r'\textbf{Color: (r-i)}',horizontalalignment='center',verticalalignment='center',fontsize=17,transform = ax0.transAxes)

tick_params(axis='both', which='major', labelsize=17)
tick_params(axis='both', which='minor', labelsize=17)

ax0.set_ylim([32.5,38.1])
ax0.set_yticks([33,34,36,38])


ax1 = plt.subplot2grid((3, 1), (2, 0),colspan=3,sharex=ax0)


ax1.errorbar(np.array(z_final)*c_light,np.array(mu_M_AKAS_SCM-mu_th),xerr=np.array(err_z_final),yerr=np.array(err_mu_M_AKAS_SCM),marker='o',ms=8,color='k',linestyle='None')
ax1.plot(z_final_test*c_light,np.array(mu_th_tot)-np.array(mu_th_tot),color='r',linestyle='-',linewidth=2.0)

ax1.plot([(min(z_final_test))*c_light,(max(z_final_test))*c_light],[0+round((abs(sig_int_sol)),2),0+round((abs(sig_int_sol)),2)],color='r',linestyle='--')
ax1.plot([(min(z_final_test))*c_light,(max(z_final_test))*c_light],[0-round((abs(sig_int_sol)),2),0-round((abs(sig_int_sol)),2)],color='r',linestyle='--')
ax1.set_ylabel(r'\textbf{$\Delta$[$\mu$ (mag)]}',fontsize=20,fontweight='bold')
ax1.set_xlabel(r'\textbf{$cz_\mathrm{CMB} (km s$^{-1}$)$}',fontsize=20,fontweight='bold')

ax1.set_yticks([-1.0,-1.0,-0.5,0.0, 0.5, 1.0])
ax1.set_xticks([3000, 5000,12000])
ax1.set_xlim([3000,12000])
ax1.tick_params(axis='both', which='major', labelsize=17,top='on')
ax1.tick_params(axis='both', which='minor', labelsize=17,top='on')
fig.subplots_adjust(hspace=0)  
ax0.axes.get_xaxis().set_visible(False)
 

ax0.legend(loc=2,markerscale=1.0,prop={'size':11},ncol=2) 
ax1.ticklabel_format(useOffset=False, style='plain')
ax0.set_xscale('log')
savefig('Figures/Hubble_diagram.png')
show()
close("all")
