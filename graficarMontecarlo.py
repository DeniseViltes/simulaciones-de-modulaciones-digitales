import numpy as np
from matplotlib import pyplot as plt

from Probabilidades import *
def procesarPuntos2VA(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    return y


tipoConstelacion='PSK'


EbNoDB = np.arange(0, 11, 1)  # Eb/N0 en dB
SNR = 10**(EbNoDB / 10)


Pe2_PSK = procesarPuntos2VA(f'probasDeError/2-{tipoConstelacion}')
Pe4_PSK= procesarPuntos2VA(f'probasDeError/4-{tipoConstelacion}')
Pe8_PSK = procesarPuntos2VA(f'probasDeError/8-{tipoConstelacion}')
Pe16_PSK = procesarPuntos2VA(f'probasDeError/16-{tipoConstelacion}')


teorica_2_PSK = pes_teorica(tipoConstelacion, 2, SNR)
teorica_4_PSK = pes_teorica(tipoConstelacion, 4, SNR)
teorica_8_PSK = pes_teorica(tipoConstelacion, 8, SNR)
teorica_16_PSK = pes_teorica(tipoConstelacion, 16, SNR)


fig=plt.figure()
plt.grid(True)
plt.loglog(EbNoDB, Pe2_PSK,'o', label=f'2-{tipoConstelacion} simulada')
plt.loglog(EbNoDB, teorica_2_PSK, label=f'2-{tipoConstelacion} teorica')
plt.loglog(EbNoDB, Pe4_PSK,'o', label=f'4-{tipoConstelacion} simulada')
plt.loglog(EbNoDB, teorica_4_PSK, label=f'4-{tipoConstelacion} teorica')
plt.loglog(EbNoDB, Pe8_PSK,'o', label=f'8-{tipoConstelacion} simulada')
plt.loglog(EbNoDB, teorica_8_PSK, label=f'8-{tipoConstelacion} teorica')
plt.loglog(EbNoDB, Pe16_PSK,'o', label=f'16-{tipoConstelacion} simulada')
plt.loglog(EbNoDB, teorica_16_PSK, label=f'16-{tipoConstelacion} teorica')


plt.ylabel('Probabilidad de error')
plt.xlabel('EbNo')
plt.legend()
plt.show()