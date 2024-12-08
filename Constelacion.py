from enum import Enum
from Modulaciones import *


class TipoConstelacion(Enum):
    ASK = 1
    PSK = 2
    QAM = 3
    FSK = 4


fuciones_constelaciones = {
        'ASK': ask,
        'PSK': psk,
        'QAM': qam,
        'FSK': fsk
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
        self.simbolos = None
        validar_M(M)
        self.d = d
        self.M = M
        self.tipoConstelacion = self.crear_simbolos(constelacion)


    def crear_simbolos(self,constelacion_str):
        try:
            constelacion_enum = TipoConstelacion[
                constelacion_str.upper()]  # Aseguramos que el string esté en mayúsculas

            funcion = fuciones_constelaciones[constelacion_str.lower()]
            simbolos, umbral, gray_map = funcion()
            self.simbolos = simbolos
            self.umbrales = umbral
            self.codigo= gray_map
            return constelacion_enum
        except KeyError:
            return None, "Constelacion no válida"
