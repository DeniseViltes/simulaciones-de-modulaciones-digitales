from enum import Enum
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

def validar_M(M):
    if not (M > 0 and (M & (M - 1)) == 0):
        raise ValueError("M debe ser una potencia de 2.")
    if M > 2 and not (np.sqrt(M).is_integer()):
        raise ValueError("Para QAM, M debe tener una raíz cuadrada entera si M > 2.")



class Constelacion:
    # Elijo la constelación con un string, puede ser 'ASK', 'PSK', 'QAM', 'FSK'
    def __init__(self, d, M,constelacion):
        self.umbrales = None
        self.codigo = None
        validar_M(M)
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
        cantidadBits = len(bits)
        simbolosCodificados = np.zeros(self.M)
        pos_codificados = 0
        for i in range(0,cantidadBits,self.M):
            s= bits[i:i+self.M]
            simbolo = self.codigo.get(binario_a_decimal(s))
            if simbolo is None:
                return None, "Constelacion no válida"
            simbolosCodificados[pos_codificados] = simbolo
            pos_codificados+=1
        return simbolosCodificados



