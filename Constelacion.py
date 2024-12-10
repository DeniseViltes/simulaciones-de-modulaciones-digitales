from enum import Enum

from numpy.ma.core import zeros_like

from Modulaciones import *
from graficadores import *


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
    shift = gray_decimal >> 1
    while shift:
        binary_decimal ^= shift
        shift >>= 1
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
        else:
            simbolosCodificados = np.zeros(int(cantidadBits / k))
        pos_codificados = 0
        for i in range(0,cantidadBits-k,k):
            s= bits[i:i+k]
            simbolo = self.codigo.get(array_binario_a_decimal(s))
            # if simbolo is None:
            #     return None, "Constelacion no válida"
            simbolosCodificados[pos_codificados] = simbolo
            pos_codificados+=1
        return simbolosCodificados


            for i in umbrales:
                if x <= i :
                    break
                else:
                    indice_x +=1
            for j in umbrales:
                if y <= j :
                    break
                else:
                    indice_y +=1
            simbolos_estimado[indice] = posiciones[indice_x + indice_y * 4]

        return simbolos_estimado

'''
            #forma 2
            simbolos_estimado = np.zeros_like(posicion_recibida, dtype=complex)
            posiciones = list(self.codigo.values())
            contador_y = 0


            for a in umbrales:
                contador_x = 0
                for b in umbrales:

                    if x <= b and y <= a:
                        simbolos_estimado[indice] = posiciones[contador_x + contador_y*4]
                        break
                    elif x > b and y > a:
                        simbolos_estimado[indice] = posiciones[contador_x + contador_y * 4]
                        break
                    else:
                        contador_x +=1
                contador_y +=1

            indice += 1
        return simbolos_estimado
        #bueno no funca, mañana veo de si hay forma mas optima, para mi con lo de usarlo en coordenadas sea mas facil
        #o de hacer con mas if menos iteraciones para recorrer la matriz.
    '''


'''
        def hallar_umbral_superior(posicion , umbrales):
            contador = 0
            umbrales = np.sort(self.umbrales)
            while posicion <= umbrales[contador]:
                contador +=1
            return contador
        '''







