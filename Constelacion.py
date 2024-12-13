from enum import Enum
from Modulaciones import *
from graficadores import *
from Decisores import *
from Energia import *
import numpy as np

#from montecarlo import simbolos_codificados, simbolos_con_ruido


class TipoConstelacion(Enum):
    ASK = 1
    PSK = 2
    QAM = 3
    FSK = 4

fuciones_constelaciones = {
    TipoConstelacion.ASK: ask,
    TipoConstelacion.PSK: psk,
    TipoConstelacion.QAM: qam,
    TipoConstelacion.FSK: fsk
}

def array_binario_a_decimal(arr):
    arr = np.array(arr, dtype=int)
    suma = 0
    j = 0
    for i in arr[::-1]:
        suma += i*2**j
        j += 1
    return suma

def gray_to_binary_array(gray_decimal, num_bits):
    # Convertir de Gray a binario estándar
    binary_decimal = gray_decimal
    # shift = gray_decimal >> 1
    # while shift:
    #     binary_decimal ^= shift
    #     shift >>= 1
    binary_array = np.array([int(bit) for bit in format(binary_decimal, f'0{num_bits}b')], dtype=int)
    return binary_array


def validar_M(M):
    if not (M > 0 and (M & (M - 1)) == 0):
        raise ValueError("M debe ser una potencia de 2.")
    # if M > 2 and not (np.sqrt(M).is_integer()):
    #     raise ValueError("Para QAM, M debe tener una raíz cuadrada entera si M > 2.")



class Constelacion:
    # Elijo la constelación con un string, puede ser 'ASK', 'PSK', 'QAM', 'FSK'
    def __init__(self, d, M,constelacion):
        validar_M(M)
        self.umbrales = None
        self.codigo = None
        self.d = d
        self.M = M
        self.tipoConstelacion = self.crear_simbolos(constelacion)



    def crear_simbolos(self,constelacion_str):
        try:
            constelacion_enum = TipoConstelacion[constelacion_str.upper()]

            funcion = fuciones_constelaciones[constelacion_enum]

            gray_map,umbral = funcion(self.d, self.M)
            self.umbrales = umbral
            self.codigo= gray_map
            return constelacion_enum
        except KeyError:
            return None, "Constelacion no válida"

    def graficar(self):

        graficadores = {
            TipoConstelacion.ASK : graficar_ask,
            TipoConstelacion.PSK : graficar_psk,
            TipoConstelacion.QAM : graficar_qam,
            TipoConstelacion.FSK : graficar_fsk
        }
        tipo = self.tipoConstelacion
        funcion = graficadores[tipo]
        funcion(self.umbrales, self.codigo)

    def codificarBits(self, bits):
        k = int(np.log2(self.M))
        cantidadBits = len(bits)
        cantidadBits = (cantidadBits // k) * k

        if self.tipoConstelacion == TipoConstelacion.QAM or self.tipoConstelacion == TipoConstelacion.PSK:
            simbolosCodificados = np.zeros(int(cantidadBits/k), dtype=complex)
        elif self.tipoConstelacion == TipoConstelacion.FSK:
            simbolosCodificados = list(np.zeros(int(cantidadBits / k)))
        else:
            simbolosCodificados = np.zeros(int(cantidadBits / k))
        pos_codificados = 0
        for i in range(0,cantidadBits,k): #estaba como cantidadBits-k y por eso no entraba a la ultima palabra
            s= bits[i:i+k]
            simbolo = self.codigo.get(array_binario_a_decimal(s))
            # if simbolo is None:
            #     return None, "Constelacion no válida"

            simbolosCodificados[pos_codificados] = simbolo
            pos_codificados+=1
        return simbolosCodificados


    def decodificador (self, posicion_recibida):
        decisores = {
            TipoConstelacion.ASK: decisor_ASK,
            TipoConstelacion.PSK: decisor_PSK,
            TipoConstelacion.QAM: decisor_QAM,
            TipoConstelacion.FSK: decisor_FSK
        }
        tipo = self.tipoConstelacion
        funcion = decisores[tipo]
        k =int( np.log2(self.M))
        posiciones_originales =list(self.codigo.values())
        posiciones_decodificadas = funcion(posiciones_originales,self.umbrales,self.M, posicion_recibida)

        simbolos_decodificados = np.zeros(len(posiciones_decodificadas) * k, dtype=int) #pasando de nuevo a bits
        pos_simbol = 0
        for i in posiciones_decodificadas:
            if self.tipoConstelacion == TipoConstelacion.FSK:
                codigo = i
            else:
                codigo = next((clave for clave, valor in self.codigo.items() if valor == i), None)
            simbolo_en_array = gray_to_binary_array(codigo, k)
            simbolos_decodificados[pos_simbol:pos_simbol+k]= simbolo_en_array
            pos_simbol+=k
        return simbolos_decodificados.astype(int)


    def calcularEnergias(self):
        energias={
            TipoConstelacion.ASK: energiaDeSimbolo_ASK,
            TipoConstelacion.PSK: energiaDeSimbolo_PSK,
            TipoConstelacion.QAM: energiaDeSimbolo_QAM,
            TipoConstelacion.FSK: energiaDeSimbolo_FSK
        }
        tipo = self.tipoConstelacion
        funcion = energias[tipo]
        k = int(np.log2(self.M))
        energiaDeSimbolo = funcion(self.d,self.M)
        energiaDeBit = energiaDeSimbolo/k
        return energiaDeSimbolo,energiaDeBit

    def tasaDeExito(self,recibido, transmitido):
        exitos = 0
        cantidad_bits = len(recibido)
        k = int(np.log2(self.M))
        for i in range(0,cantidad_bits,k):
            palabra_recibida = recibido[i:i+k]
            palabra_transmitida = transmitido[i:i+k]
            exitos += np.all(palabra_recibida == palabra_transmitida)
        cantidad_palabras = cantidad_bits/k
        return exitos /cantidad_palabras



    def ruidoConstelacion(self,simbolos_codif,desvio):
        n_ruido = len(simbolos_codif)
        if self.tipoConstelacion == TipoConstelacion.FSK:
           ruido = np.transpose(np.random.normal(0, desvio, (self.M, n_ruido)))
        elif self.tipoConstelacion == TipoConstelacion.ASK:
            ruido = np.random.normal(0, desvio, n_ruido)
        else:
            ruido = np.random.normal(0, desvio, n_ruido)
            ruido = ruido + 1j*ruido # si queremos que sea simetrico el ruido. Sino poner np.random.normal(0,desvio,n_ruido)

        simbolos_con_ruido = simbolos_codif + ruido
        return simbolos_con_ruido

