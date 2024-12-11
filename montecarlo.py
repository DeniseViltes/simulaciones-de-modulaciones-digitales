import matplotlib.pyplot as plt

from Constelacion import *

#DEFINICION DE PARAMETROS

d = 2
M = 4
k = int(np.log2(M))

#n es la cantidad de veces q lo genera (va a ser cuantos arrays queremos hacer)
m = 1 #cuantos arrays diferentes queremos, estos luego los promedio. Serian m filas de n_bits! Tengo que promediar el resultado de Pe de cada fila.
p = 0.5
n_bits = 8 #4*10**3 #van a ser columnas
bit_array_send = np.random.binomial(m,p,n_bits)
# bit_array_send = [1,1,1,0]

EbNoDB = np.arange(0, 11, 1)  # Eb/N0 en dB
SNR = 10**(EbNoDB / 10)  # Eb/N0 lineal
#PSK -> sigma^2 = No/2

modulacion = Constelacion(d,M,'PSK')
modulacion.graficar() # quiero ver el grafico de PSK

Es,Eb = modulacion.calcularEnergias()



sigma = Eb/SNR # SNR = Es / desvio^2 = Es / varianza --> random.mnormal usa (media,desvio,n_muestras) ;
# aca sigma estaria siendo la varianza en vez del desvio. Chequear si mejora usando sigma = np.sqrt(Eb/SNR)
std = np.sqrt(sigma)


Pe = []


simbolos_codificados = modulacion.codificarBits(bit_array_send)
n_ruido = len(simbolos_codificados)
ruido_x = np.random.normal(0,std[10],n_ruido)
ruido_y =1j* np.random.normal(0,std[10], n_ruido)
ruido = ruido_x + ruido_y

simbolos_con_ruido = simbolos_codificados + ruido_x + ruido_y #pruebo PSK
simbolos_decodificados = modulacion.decodificador(simbolos_con_ruido)
print(f" Desvio: {std[10]} \n"
      f" array bits: {bit_array_send}\n"
      f" simbolos enviados: {simbolos_codificados}\n "
      f"simbolos recibidos: {simbolos_con_ruido}\n"
      f"simbolos decodificados: {simbolos_decodificados}")

'''
for i in std:
    simbolos_codificados = modulacion.codificarBits(bit_array_send)
    n_ruido = len(simbolos_codificados)
    ruido_x = np.random.normal(0,i,n_ruido)
    ruido_y =1j* np.random.normal(0,i, n_ruido)
    ruido = ruido_x + ruido_y

    #simbolos_con_ruido = simbolos_codificados + ruido_x  #Estoy en ask, solo tengo componente en x
    simbolos_con_ruido = simbolos_codificados + ruido_x + ruido_y #pruebo PSK
    simbolos_decodificados = modulacion.decodificador(simbolos_con_ruido)

    P_acierto = modulacion.tasaDeExito(simbolos_decodificados,bit_array_send)
    Pe.append( float(1-P_acierto))
    print(f" Desvio: {i} \n"
          f" simbolos enviados: {simbolos_codificados}\n "
          f"simbolos recibidos: {simbolos_con_ruido}\n"
          f"simbolos decodificados: {simbolos_decodificados}")

plt.figure()
plt.xlabel("SNR [dB]")
plt.ylabel("Pe")
plt.plot(EbNoDB,Pe)

plt.show()
'''



