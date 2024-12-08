import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.stats import norm



#n es la cantidad de veces q lo genera (va a ser cuantos arrays queremos hacer)
n = 1 #cuantos arrays diferentes queremos, estos luego los promedio. Serian filas!
p = 0.5
n_bits = 4*10**1 #van a ser columnas
bit_array_send = np.random.binomial(n,p,n_bits)

#Empezamos con la PAM
EbNoDB = np.arange(0,10,1) #De 0 a 10dB
EbNo = 10**(EbNoDB/10)

sigma = 0.1
std = np.sqrt(sigma)
ruido = np.random.normal(0, std, n_bits)


bit_array_rec = bit_array_send + ruido




M= 16
k = np.log2(M)
Pes = np.zeros_like(EbNo)
j = 0
for i in EbNo:
    x = np.sqrt(6*i*k/(M**2-1))
    Q = norm.sf(x)
    Pes[j] = 2*(1-1/M)*Q
    j+=1

Peb = Pes/k
#PAM

#mi compu anda como el ojete


