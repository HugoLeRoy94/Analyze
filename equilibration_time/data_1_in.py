import numpy as np
from Cluster import Cluster
from ISF import ISF
from MSD import MSD
from Energy import NRG
from PCF import PCF
from PCF import PCF_L
from Time import Time

from scipy.special import erfc

# gillespie parameter
Nlinker = 5
ell_tot = 10**2
kdiff = 0.1/ell_tot
Energy = -15

avR = lambda L,N : 2*(np.exp(-1.5/(L/N)) * np.sqrt(L/N*6/np.pi)*(3+2*L/N) - 9*erfc(np.sqrt(3/2/(L/N))))/(9*L/N) #average distance between equilibrated nodes
print(avR(ell_tot,Nlinker))
print(np.sqrt(2*ell_tot/Nlinker/3))

Nprocess = 100
seeds = set()
while len(seeds) < Nprocess:
    seeds.add(np.random.randint(1000000))
seeds = list(seeds)
args = [[ell_tot,Energy,kdiff,seeds[_],Nlinker,3] for _ in range(Nprocess)]

# argument of the different classes
cluster_arg = tuple([avR(ell_tot,Nlinker)]) # max distance
MSD_arg = () # no argument 
ISF_arg = (0.5,10) # q_norm, q_num_sample
NRG_arg = ()
PCF_arg = (np.sqrt(ell_tot)/2,50) # max_distance,numb_bin
PCF_L_arg = (ell_tot,30) # max_distance,numb_bin
Time_arg = ()

measurement_args = {
    'Cluster': (Cluster, cluster_arg),
    'MSD': (MSD, MSD_arg),
    'ISF': (ISF, ISF_arg),
    'PCF':(PCF,PCF_arg),
    'PCF_L':(PCF_L,PCF_L_arg),
    'NRG':(NRG,NRG_arg)#,
    #'Time':(Time,Time_arg)
    # Add other measurements as needed
}

measurement_flags = {
    'NRG':True,
    'Cluster': True,
    'MSD': False,
    'ISF': False,
    'PCF':False,
    'PCF_L':False#,
    #'Time':True
    # Set each measurement to True/False as desired
}

# Simulation parameters
step_tot = 2*10**5
#check_steps = 10**2
initial_check_steps = 10**3
coarse_grained_step = 10**1
log_base=1.5