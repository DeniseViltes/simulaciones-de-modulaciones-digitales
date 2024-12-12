import matplotlib.pyplot as plt
import numpy as np

from Constelacion import *

#DEFINICION DE PARAMETROS

d = 2
M = 4
k = int(np.log2(M))

#n es la cantidad de veces q lo genera (va a ser cuantos arrays queremos hacer)
m = 1 #cuantos arrays diferentes queremos, estos luego los promedio. Serian m filas de n_bits! Tengo que promediar el resultado de Pe de cada fila.
p = 0.5
n_bits = 4*10**4 #4*10**3 #van a ser columnas
bit_array_send = np.random.binomial(m,p,n_bits)
# bit_array_send = [1,1,1,0]

EbNoDB = np.arange(0, 11, 1)  # Eb/N0 en dB
SNR = 10**(EbNoDB / 10)  # Eb/N0 lineal
#FSK -> sigma^2 = No/2

modulacion = Constelacion(d,M,'FSK')
#modulacion.graficar() # quiero ver el grafico de FSK

Es,Eb = modulacion.calcularEnergias()



sigma = Eb/SNR
std = np.sqrt(sigma)
#std = np.ones(1) * np.sqrt(0.2)

Pe = []


# simbolos_codificados = modulacion.codificarBits(bit_array_send)
# n_ruido = len(simbolos_codificados)
# ruido_x = np.random.normal(0,std[10],n_ruido)
# ruido_y =1j* np.random.normal(0,std[10], n_ruido)
# ruido = ruido_x + ruido_y

# simbolos_con_ruido = simbolos_codificados + ruido_x + ruido_y #pruebo FSK
# simbolos_decodificados = modulacion.decodificador(simbolos_con_ruido)
# print(f" Desvio: {std[10]} \n"
#       f" array bits: {bit_array_send}\n"
#       f" simbolos enviados: {simbolos_codificados}\n "
#       f"simbolos recibidos: {simbolos_con_ruido}\n"
#       f"simbolos decodificados: {simbolos_decodificados}")


for i in std:
    simbolos_codificados = modulacion.codificarBits(bit_array_send)
    n_ruido = len(simbolos_codificados)
    ruido_x = np.random.normal(0,i,n_ruido)
    ruido_y =1j*ruido_x
    # ruido_y =1j* np.random.normal(0,i, n_ruido)
    #ruido = ruido_x + ruido_y
    # ruido = ruido_x
    ruido_fsk = np.random.normal(0,i,(modulacion.M,n_ruido)) # para modelar el ruido fsk, cada elemento de la "dimension/base/eje" tiene componente de ruido
    #simbolos_con_ruido = simbolos_codificados + ruido_x  #Estoy en ask, solo tengo componente en x
    simbolos_con_ruido = simbolos_codificados + np.transpose(ruido_fsk) #pruebo FSK
    simbolos_decodificados = modulacion.decodificador(simbolos_con_ruido)

    P_acierto = modulacion.tasaDeExito(simbolos_decodificados,bit_array_send)
    Pe.append( float(1-P_acierto))
    # print(f" Desvio: {i} \n"
    #       f" simbolos enviados: {simbolos_codificados}\n "
    #       f"simbolos recibidos: {simbolos_con_ruido}\n"
    #       f"simbolos decodificados: {simbolos_decodificados}")

plt.figure()
plt.xlabel("SNR [dB]")
plt.ylabel("Pe")
plt.semilogx(EbNoDB,Pe)

plt.show()




