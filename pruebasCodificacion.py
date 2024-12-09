from Constelacion import *
import numpy as np

d = 2
M = 4
k = int(np.log2(M))

n = 1 #cuantos arrays diferentes queremos, estos luego los promedio. Serian filas!
p = 0.5
n_bits = M*2 #van a ser columnas
bit_array_send = np.random.binomial(n,p,n_bits)

mod_ASK = Constelacion(d,M,'ASK')
simbolos_codificados = mod_ASK.codificarBits(bit_array_send)

sigma = 0.1
std = np.sqrt(sigma)

n_ruido = np.size(simbolos_codificados)
ruido = np.random.normal(0,std,n_ruido)


simbolos_con_ruido = simbolos_codificados + ruido

simbolos_decodificados = mod_ASK.decisor_ASK(simbolos_con_ruido)

print('pos codificado',simbolos_codificados)
print('pos recibida',simbolos_con_ruido)
print('pos decod',simbolos_decodificados)
