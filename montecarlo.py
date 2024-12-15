import matplotlib.pyplot as plt

from Constelacion import *
from almacenador import *
from Probabilidades import *
d = 2
M = 16

k = int(np.log2(M))

#n es la cantidad de veces q lo genera (va a ser cuantos arrays queremos hacer)
m = 1 #cuantos arrays diferentes queremos, estos luego los promedio. Serian m filas de n_bits! Tengo que promediar el resultado de Pe de cada fila.
p = 0.5
n_bits = 4*10**6#4*10**3 #van a ser columnas
bit_array_send = np.random.binomial(m,p,n_bits)
# bit_array_send = [1,1,1,0]

EbNoDB = np.arange(0, 11, 1)  # Eb/N0 en dB
SNR = 10**(EbNoDB / 10) # Eb/N0 lineal en veces


tipoConstelacion = 'FSK'
modulacion = Constelacion(d,M,tipoConstelacion)
modulacion.graficar() # quiero ver el grafico de ASK

Es,Eb = modulacion.calcularEnergias()

#psk y QAM-> sigma_cuad = No
#ASK , FSK-> sigma^2 = No/2
#SNR = Eb/No o ES/No

sigma_cuad = 1/(2*SNR)
std = np.sqrt(sigma_cuad)

print(f"Eb: {Eb} \n std: {std}")
#std = np.ones(11) * np.sqrt(0.2)

Pe = []


simbolos_codificados = modulacion.codificarBits(bit_array_send)

teorica = pes_teorica(tipoConstelacion, M, SNR)
#print(f"Probabilidad de error teorica con SNR {SNR}: {teorica}\n")
j=0
for i in std:
    n_ruido = len(simbolos_codificados)

    simbolos_con_ruido= modulacion.ruidoConstelacion(simbolos_codificados,i)
    simbolos_decodificados = modulacion.decodificador(simbolos_con_ruido)

    #P_acierto = modulacion.tasaDeError(simbolos_decodificados, bit_array_send) tasa de error esta contando las diferencias por lo que ya devuelve el Perror, no el de acierto
    p_error = modulacion.tasaDeError(simbolos_decodificados,bit_array_send)
    Pe.append( p_error )
    print(f"Desvio: {i} Probabilidad de error estimada: {p_error} Teorica: {teorica[j]}\n")
    j+=1
guardarCurva(EbNoDB, Pe, f'probasDeError/{M}-{tipoConstelacion}')




plt.figure()
plt.title(f'Probabilidades de error para {M}-{tipoConstelacion}')
plt.grid(True,which='both')
plt.xlabel("SNR [dB]")
plt.ylabel("Pe")
plt.semilogx(EbNoDB,Pe,label= 'estimada')
plt.semilogx(EbNoDB,teorica,label= 'teorica')
plt.legend()
plt.show()




