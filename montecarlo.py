from Constelacion import *
import numpy as np


d = 2
M = 16
k = int(np.log2(M))

#n es la cantidad de veces q lo genera (va a ser cuantos arrays queremos hacer)
n = 1 #cuantos arrays diferentes queremos, estos luego los promedio. Serian filas!
p = 0.5
n_bits = M*2 #van a ser columnas
bit_array_send = np.random.binomial(n,p,n_bits)


modulacion = Constelacion(d,M,'PSK')
#modulacion.graficar()
simbolos_codificados = modulacion.codificarBits(bit_array_send)

mod_qam = Constelacion(d,M,'QAM')
simbolos_codif_qam = mod_qam.codificarBits(bit_array_send)


EbNoDB = np.arange(0,10,1) #De 0 a 10dB
EbNo = 10**(EbNoDB/10)

sigma = 0.1
std = np.sqrt(sigma)

n_ruido = np.size(simbolos_codificados)
ruido_x = np.random.normal(0,std,n_ruido)
ruido_y =1j* np.random.normal(0, std, n_ruido)
ruido = ruido_x + ruido_y

simbolo_ruido_qam = simbolos_codif_qam + ruido

simbolos_con_ruido = simbolos_codificados + ruido
#print(np.angle(simbolos_codificados)*180/np.pi+180)
#print(np.angle(simbolos_con_ruido)*180/np.pi+180)

simbolos_decodificados = modulacion.decisor_PSK(simbolos_con_ruido)

simbolos_decodif_qam = mod_qam.decisor_QAM(simbolo_ruido_qam)

print('pos codificado',simbolos_codif_qam)
print('pos recibida',simbolo_ruido_qam)
print('pos decod',simbolos_decodif_qam)
'''
print('umbrales')
print('angulos codificado',np.angle(simbolos_codificados)*180/np.pi)
print('angulos recibido',np.angle(simbolos_con_ruido)*180/np.pi)
print('angulo decod',np.angle(simbolos_decodificados)*180/np.pi)
'''

modQAM = Constelacion(d,M,'QAM')
modASK = Constelacion(d,M,'ASK')

modASK.graficar()
modQAM.graficar()


# #Empezamos con la PSK
# EbNoDB = np.arange(0,10,1) #De 0 a 10dB
# EbNo = 10**(EbNoDB/10)
#
# sigma = 0.1
# std = np.sqrt(sigma)
# ruido = np.random.normal(0, std, n_bits)
#

# Pes = np.zeros_like(EbNo)
# j = 0
# for i in EbNo:
#     x = np.sqrt(6*i*k/(M**2-1))
#     Q = norm.sf(x)
#     Pes[j] = 2*(1-1/M)*Q
#     j+=1
#
# Peb = Pes/k
# #PAM
#
# #mi compu anda como el ojete


