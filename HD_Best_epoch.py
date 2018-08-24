# INTEGRATION FUNCTION E(z)
# SCIPY RETURNS THE INTEGRATION RESULT AS A TWO DIMENSIONAL ARRAY.
#FIRST ELEMENT IS THE RESULT. SECOND ELEMENT IS THE ERROR ASSOCIATED

def e_z_LCDM(z):
    return (1.0/math.sqrt(omega_m*((1+z)**3)+ omega_k*((1+z)**2) + omega_lambda))
    e_z_int_LCDM, e_z_int_err_LCDM = integrate.quad(e_z_LCDM,0.,z)

def r_com(z):                   # We define comoving distance for flat universe in Mpc
    return (d_h*integrate.quad(e_z_LCDM,0.,z)[0])

def d_lum(z):                   # We define luminosity distance for flat universe in Mpc
    return (r_com(z)*(1+z))

def d_mod(z):                   # We define modulus distance for flat universe
    return (5.0 * np.log10(d_lum(z)*10**6/10))

# (1.0,0.0)
def e_z_2(z):
    return (1.0/math.sqrt(omega_m_Sitter*((1+z)**3)+ omega_k_Sitter*((1+z)**2) + omega_lambda_Sitter))
    e_z_int_2, e_z_int_err_2 = integrate.quad(e_z_2,0.,z)

def r_com_2(z):                   # We define comoving distance for flat universe in Mpc
    return (d_h*integrate.quad(e_z_2,0.,z)[0])

def d_lum_2(z):                   # We define luminosity distance for flat universe in Mpc
    return (r_com_2(z)*(1+z))

def d_mod_2(z):                   # We define modulus distance for flat universe
    return (5.0 * np.log10(d_lum_2(z)*10**6/10))

## Fonction pour le fit, lineaire, couleur et totale

def model_SCM(p,x,vFe,color):
	ZP,alpha,beta=p              
	return (5*log10(np.array(x))+ZP-alpha*log10(np.array(vFe))+beta*(np.array(color)))

def residual_SCM(p,data):
	x,m,vFe,color,err=data	
	ZP,alpha,beta= p              
	return (m-model_SCM(p,x,vFe,color))/err

p_lin=[0.5]
p_col=[0.5,0.8]
p_SCM=[0.5,0.8,0.9]

# On choisie le sample que l on veut utilise
sample_SNe=input("Which sample, tot, 3000  ")
outlier_CSP=['SN2004ej','SN2005hd','SN2006iw','SN2007X','SN2007ld','SN2008K','SN2008bk','SN2008bp','SN2009au','SN2008in']

indice_cut=[]
if sample_SNe==str('tot'):
	v_cut=0
	for i in range(N_csp):
		if (c_light*z_CMB_csp[i]>v_cut) and (name_csp[i] not in outlier_CSP):
			indice_cut.append(i)
elif sample_SNe==str('3000'):
	v_cut=3000
	for i in range(N_csp):
		if (c_light*z_CMB_csp[i]>v_cut) and (name_csp[i] not in outlier_CSP):
			indice_cut.append(i) 

ind_csp_SNe=np.arange(0,69,1)
indice_c=list(set.intersection(set(indice_cut),set(ind_csp_SNe)))
indice=indice_c
indice.sort()


sig_pecu=150*1.0/5000
X_days=43
epoque_choisie=np.zeros(N_csp)
for ep in range(N_csp):
	epoque_choisie[ep]=X_days

#On initialise l abscisse
z_final=[]
err_z_final=[]
#On initialise l ordonne avec magnitude AvG+KC
y_DH_bis=[]
err_y_DH_bis=[]
#On initialise l ordonne avec raw mag
y_DH_bis_raw=[]
err_y_DH_bis_raw=[]
#On initialise la couleur avec MW et KC
color_bis=[]
err_color_bis=[]
#On initialise s2
vFe_bis=[]
err_vFe_bis=[]
#On initialise le nom des SNe
table_bis=[]
indice_bis=[]

for i in range(N_csp):
	# on choisit que les SNe dans notre sample mais aussi celle pour laquelle la couleur existe a cette epoque
	if (i in indice) and (epoque_choisie[i]<max(phase_y2_final_csp[i])) and (epoque_choisie[i]>min(phase_y2_final_csp[i])) and (epoque_choisie[i]<max(phase_xy_final_csp[i])) and (epoque_choisie[i]>min(phase_xy_final_csp[i])) and (v_Hbeta_func_csp[i]!=0) and (math.isfinite(color_func_csp[i](epoque_choisie[i]))) and (v_Hbeta_func_csp[i](epoque_choisie[i])>0.0):
		#cz en abscisse
		z_final.append((z_CMB_csp[i]))
		err_z_final.append((err_z_CMB_csp[i]))
		#magnitude corrigee par MW et KC		
		y_DH_bis.append(y2_csp[i](epoque_choisie[i])*1)
		err_y_DH_bis.append(y2_err_csp[i](epoque_choisie[i])-y2_csp[i](epoque_choisie[i])*1)
		#color
		color_bis.append(color_func_csp[i](epoque_choisie[i])*1)
		err_color_bis.append(err_color_func_csp[i](epoque_choisie[i])*1)
		#velocity
		vFe_bis.append(v_Hbeta_func_csp[i](epoque_choisie[i])*1)
		err_vFe_bis.append(sqrt((err_v_Hbeta_func_csp[i](epoque_choisie[i])*1)**2+(sig_pecu)**2))
		#name
		table_bis.append(name_csp[i])
		indice_bis.append(i)

mean_color=mean(color_bis)
color_bis=np.array(color_bis)-mean_color

mean_VHb=mean(vFe_bis)
vFe_bis=np.array(vFe_bis)*1.0/(mean_VHb)
