def lnlike(p, z_cmb,m,v_Fe,color,err_z_cmb,err_mag,err_v_Fe,err_color):
	alpha, beta, ZP,sig_sys = p
	model = ZP+5*log10(c_light*z_cmb)-(alpha)*log10(v_Fe)+beta*(color)


	sig_mag=err_mag
	sig_vel=(alpha*1.0/log(10))*err_v_Fe*1.0/(v_Fe)
	sig_color=beta*err_color	
	sig_z=err_z_cmb*(5*(1+z_cmb)*1.0/(z_cmb*(1+z_cmb*1.0/2)*log(10)))


	sigma_total=sig_mag**2+np.array(sig_vel)**2+np.array(sig_color)**2+np.array(sig_z)**2+(sig_sys)**2
	inv_sigma_total = 1.0/sigma_total

	return -0.5*(np.sum((m-model)**2*inv_sigma_total-np.log(inv_sigma_total)))


nll = lambda *args: -lnlike(*args)

result=minimize(nll, [5, 1.0, 10,0.3],args=(np.array(z_final), np.array(y_DH_bis), np.array(vFe_bis),np.array(color_bis),np.array(err_z_final), np.array(err_y_DH_bis),np.array(err_vFe_bis),np.array(err_color_bis)))

alpha_sol, beta_sol, ZP_sol,sig_int_sol = result["x"]
covariance_matrix=result["hess_inv"]
errors_tot=np.diagonal(covariance_matrix)**.5
err_alpha_sol, err_beta_sol, err_ZP_sol,err_sig_int_sol = errors_tot


#################################################################################
#
#                                 EMCEE
#
#

import emcee
import corner

#prior function

#seulement omega M a une restriction
def lnprior(p):
	alpha, beta, ZP,sig_sys = p
	if (0.1<sig_sys<0.7) and (alpha!=0) and (beta!=0) and (ZP!=0):
		return 0.0
	return -np.inf
def lnprob(p,z_cmb,m,v_Fe,color,err_z_cmb,err_mag,err_v_Fe,err_color):
	lp=lnprior(p)
	if not np.isfinite(lp):
		return -np.inf
	return lp+lnlike(p, z_cmb,m,v_Fe,color,err_z_cmb,err_mag,err_v_Fe,err_color)


#nombre d inconnue et de walkers
ndim,nwalkers=4,500
#position intitial
pos=[result['x']+1.e-1*np.random.randn(ndim) for i in range(nwalkers)]

sampler=emcee.EnsembleSampler(nwalkers, ndim, lnprob,args=(np.array(z_final), np.array(y_DH_bis), np.array(vFe_bis),np.array(color_bis),np.array(err_z_final), np.array(err_y_DH_bis),np.array(err_vFe_bis),np.array(err_color_bis)))
pos,prob,state=sampler.run_mcmc(pos,400)

pos, prob, state  = sampler.run_mcmc(pos, 600)

#flatten the chain and remove the 50 first steps
samples=sampler.chain[:, 50:, :].reshape((-1,ndim))

alpha_mcmc, beta_mcmc, ZP_mcmc,sig_sys_mcmc = map(lambda v: (v[1], v[2]-v[1],v[1]-v[0]),zip(*np.percentile(samples, [16, 50, 84],axis=0)))
alpha_bis,beta_bis,ZP_bis,sig_sys_bis = median(sampler.flatchain, axis=0)


z_final_test=np.arange(0.01,0.045,0.001)
mu_th=[]
mu_th_2=[]
mu_th_tot=[]
mu_th_2_tot=[]		
for p in range(size(y_DH_bis)):
	mu_th.append(5*log10(d_lum(z_final[p]))+25)
	mu_th_2.append(5*log10(d_lum_2(z_final[p]))+25)
for p in range(size(z_final_test)):
	mu_th_tot.append(5*log10(d_lum(z_final_test[p]))+25)
	mu_th_2_tot.append(5*log10(d_lum_2(z_final_test[p]))+25)

print (str('LIKEHOOD!!!'))
print ('ZP: '+str(ZP_sol)) 
print ('err ZP: '+str(err_ZP_sol)) 
print (str('EMCEE!!!')) 
print ('ZP: '+str(ZP_mcmc[0])) 
print ('err ZP: '+str(ZP_mcmc[1])+str('   ')+str(ZP_mcmc[2]))
print (str('###################################################t#########'))
print (str('LIKEHOOD!!!'))
print ('alpha: '+str(alpha_sol)) 
print ('err alpha: '+str(err_alpha_sol)) 
print (str('EMCEE!!!'))  
print ('alpha: '+str(alpha_mcmc[0])) 
print ('err alpha: '+str(alpha_mcmc[1])+str('   ')+str(alpha_mcmc[2])) 
print (str('############################################################'))
print (str('LIKEHOOD!!!'))
print ('beta: '+str(beta_sol)) 
print ('err beta: '+str(err_beta_sol)) 
print (str('EMCEE!!!'))  
print ('beta: '+str(beta_mcmc[0])) 
print ('err beta: '+str(beta_mcmc[1])+str('   ')+str(beta_mcmc[2])) 
print (str('############################################################'))
print (str('LIKEHOOD!!!'))
print ('M abs: '+str(ZP_sol+5*log10(H0)-25)) 
print ('err M abs: '+str(err_ZP_sol)) 
print (str('EMCEE!!!')) 
print ('M abs: '+str(ZP_mcmc[0]+5*log10(H0)-25)) 
print ('err Mabs: '+str(ZP_mcmc[1])+str('   ')+str(ZP_mcmc[2])) 
print (str('############################################################'))
print (str('LIKEHOOD!!!'))
print ('Dispersion avec correction SCM '+ str(abs(sig_int_sol)))
print ('err sig sys: '+str(err_sig_int_sol)) 
print (str('EMCEE!!!')) 
print ('Dispersion avec correction SCM '+ str(sig_sys_mcmc[0]))
print ('err sig sys: '+str(sig_sys_mcmc[1])+str('   ')+str(sig_sys_mcmc[2])) 


