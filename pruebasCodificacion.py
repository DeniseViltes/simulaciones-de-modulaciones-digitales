from Constelacion import *
import numpy as np

d = 2
M = 4
k = int(np.log2(M))

n = 1 #cuantos arrays diferentes queremos, estos luego los promedio. Serian filas!
p = 0.5
n_bits = M*2 #van a ser columnas
# bit_array_send = np.random.binomial(n,p,n_bits)
bit_array_send = [0,0,1,0,0,1,1,1]


mod_PSK = Constelacion(d,M,'PSK')

mod_PSK.graficar()
simbolos_codificados = mod_PSK.codificarBits(bit_array_send)

sigma = 0.1
std = np.sqrt(sigma)

n_ruido = np.size(simbolos_codificados)
ruido = np.random.normal(0,std,n_ruido)


simbolos_con_ruido = simbolos_codificados + ruido

simbolos_decodificados = mod_PSK.decodificador(simbolos_con_ruido)

print(f" Desvio: {std} \n"
      f" array bits: {bit_array_send}\n"
      f" simbolos enviados: {simbolos_codificados}\n "
      f"simbolos recibidos: {simbolos_con_ruido}\n"
      f"simbolos decodificados: {simbolos_decodificados}")

fig = plt.figure()

plt.scatter(simbolos_codificados, np.zeros_like(simbolos_codificados), label= 'pos codificado', marker='o', facecolors='none',edgecolors='blue')
plt.scatter(simbolos_con_ruido, np.zeros_like(simbolos_con_ruido),label ='pos reciida', marker='o')
plt.scatter(simbolos_decodificados, np.zeros_like(simbolos_decodificados),label='pos decod', marker='.')

plt.legend()
# plt.show()
