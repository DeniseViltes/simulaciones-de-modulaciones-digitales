import matplotlib.pyplot as plt
import numpy as np

from Constelacion import *
from almacenador import *
from Probabilidades import *


d = 2
M = 4
tipoConstelacion = 'ASK'
EbNoDB = np.array([0,3,6,10])  # Eb/N0 en dB



k = int(np.log2(M))

m = 1
p = 0.5
n_bits = 4*10**3#4*10**3 #van a ser columnas
bit_array_send = np.random.binomial(m,p,n_bits)


SNR = 10**(EbNoDB / 10) # Eb/N0 lineal en veces

modulacion = Constelacion(d,M,tipoConstelacion)

Es,Eb = modulacion.calcularEnergias()

sigma_cuad = Eb/(2*SNR)
std = np.sqrt(sigma_cuad)


simbolos_codificados = modulacion.codificarBits(bit_array_send)


n_ruido = len(simbolos_codificados)

fig = modulacion.graficar()
colores = ['yellowgreen','skyblue','red','slateblue']
j = 0
for i in std:
    simbolos_con_ruido= modulacion.ruidoConstelacion(simbolos_codificados,i)
    x = np.zeros_like(simbolos_con_ruido)
    y = np.zeros_like(simbolos_con_ruido)
    indice = 0
    for sym in simbolos_con_ruido:
        x[indice] = sym.real
        y[indice] = sym.imag
        indice +=1
    plt.plot(x, y, 'o', markersize=2, markerfacecolor='none', color=colores[j], alpha=0.5,label = f'{EbNoDB[j]} dB')
    j += 1
plt.legend()
plt.savefig(f'{M}-{tipoConstelacion}.png')
plt.show()