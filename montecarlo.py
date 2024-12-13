from Constelacion import *
from almacenador import *
from Probabilidades import *
d = 2
M = 16
k = int(np.log2(M))

#n es la cantidad de veces q lo genera (va a ser cuantos arrays queremos hacer)
m = 1 #cuantos arrays diferentes queremos, estos luego los promedio. Serian m filas de n_bits! Tengo que promediar el resultado de Pe de cada fila.
p = 0.5
n_bits = 4*10**4 #4*10**3 #van a ser columnas
bit_array_send = np.random.binomial(m,p,n_bits)
# bit_array_send = [1,1,1,0]

EbNoDB = np.arange(0, 11, 1)  # Eb/N0 en dB
SNR = 10**(EbNoDB / 10) # Eb/N0 lineal
#PSK -> sigma^2 = No/2

tipoConstelacion = 'PSK'
modulacion = Constelacion(d,M,tipoConstelacion)
#modulacion.graficar() # quiero ver el grafico de PSK

Es,Eb = modulacion.calcularEnergias()



sigma = 1/(2*SNR)
std = np.sqrt(sigma)
#std = np.ones(1) * np.sqrt(0.2)

Pe = []


simbolos_codificados = modulacion.codificarBits(bit_array_send)
for i in std:
    n_ruido = len(simbolos_codificados)

    simbolos_con_ruido= modulacion.ruidoConstelacion(simbolos_codificados,i)
    simbolos_decodificados = modulacion.decodificador(simbolos_con_ruido)

    P_acierto = modulacion.tasaDeExito(simbolos_decodificados,bit_array_send)

    Pe.append( float(1-P_acierto))

guardarCurva(EbNoDB, Pe, f'probasDeError/{M}-{tipoConstelacion}')


teorica = pes_teorica(tipoConstelacion, M, SNR)

plt.figure()
plt.title(f'Probabilidades de error para {M}-{tipoConstelacion}')
plt.xlabel("SNR [dB]")
plt.ylabel("Pe")
plt.loglog(EbNoDB,Pe,label= 'estimada')
plt.loglog(EbNoDB,teorica,label= 'teorica')
plt.legend()
plt.show()




