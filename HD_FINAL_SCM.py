import sys # system commands
import string as string # string functions4
import math
import numpy as np # numerical tools
from scipy import *
from pylab import *
import os
from scipy import integrate
from scipy import interpolate
import itertools
from scipy.optimize import leastsq,minimize
import math as maths
from matplotlib.pyplot import figure, show, rc
from scipy.optimize import curve_fit
from kapteyn import kmpfit
import shutil
import numdifftools
from scipy.stats.stats import pearsonr


rcParams['legend.numpoints']=1
plt.rcParams['xtick.major.size'] = 11
plt.rcParams['xtick.minor.size'] = 5
plt.rcParams['ytick.major.size'] = 11
plt.rcParams['ytick.minor.size'] = 5
rc('font', weight='bold')
matplotlib.rcParams['text.latex.preamble'] = [r'\boldmath']
params = {'text.usetex': True, 'mathtext.fontset': 'stixsans'}
rcParams.update(params)

########################################## Constantes #######################
c_light=299792.458#in km/s
c_AA=299792458*1.0e10#in AA/s
kB=1.38066e-23; # Boltzmanns constant in J/K
h_erg = 6.63e-27 #Plancks constant (erg.s)
h=0.70
H0 = 100.0 * h  #Hubble constant in Km/s/Mpc
d_h=c_light*1.0/H0 #Hubble distance in Mpc

#LCDM
omega_m=0.30   # Dark matter density for standard model
omega_k=0.     #Universe curvature for standard model
omega_lambda=0.70 #Dark energy density for standard model

# de Sitter
omega_m_Sitter=1.0  # Dark matter density for standard model
omega_k_Sitter=0.     #Universe curvature for standard model
omega_lambda_Sitter=0.0 #Dark energy density for standard model

# Upload the magnitude
exec(open("Import_magnitude.py").read())
'''
  phase_X_final_CSP[filtre][SN] = phase
  X_AKAS_final_CSP[filtre][SN] = magnitude 
  err_X_AKAS_final_CSP[filtre][SN] = err magnitude
'''

#Median des alphas avec CSP est -0.407
gamma_csp=-0.407
def power_law_A(p,data):
	x,y=data
	A=p              	
	return (y-A*np.array(x)**(gamma_csp))

def power_law_vel(p,data):
	x,y,err=data
	A,alpha= p              	
	return (y-A*(x)**(alpha))*1.0/err
pw0=[8000,-0.5]
N_MC=2000

exec(open("Velocity_CSP.py").read())

#on choisit les filtres

exec(open("filters_choice.py").read())


#on calcule les couleur avec ces filtres
exec(open("color_choice.py").read())


## On cherche la meilleure epoque pour le diagramme de Hubble!!
exec(open("HD_Best_epoch.py").read())
print ('Best epoch after explosion '+ str(X_days))

exec(open("likehood_SCM.py").read())
exec(open("Hubble_diagram.py").read())

residuals_HD=np.array(mu_M_AKAS_SCM)-np.array(mu_th)
err_residuals_HD=np.array(err_mu_M_AKAS_SCM)


sys.exit("tot")

