from matplotlib import pyplot as plt

from Probabilidades import *
def procesarPuntos2VA(nombreArchivo):
    datos_simul = np.genfromtxt(nombreArchivo, delimiter='\t', skip_header=1)
    x = datos_simul[:, 0]
    y = datos_simul[:, 1]
    return y

#Usar CTRL + R para cambiar la modulacion en todos las variables del archivo
tipoConstelacion='FSK'


EbNoDB = np.arange(0, 11, 1)  # Eb/N0 en dB
SNR = 10**(EbNoDB / 10)


Pe2_FSK = procesarPuntos2VA(f'probasDeError/2-{tipoConstelacion}')
Pe4_FSK= procesarPuntos2VA(f'probasDeError/4-{tipoConstelacion}')
Pe8_FSK = procesarPuntos2VA(f'probasDeError/8-{tipoConstelacion}')
Pe16_FSK = procesarPuntos2VA(f'probasDeError/16-{tipoConstelacion}')


teorica_2_FSK = pes_teorica(tipoConstelacion, 2, SNR)
teorica_4_FSK = pes_teorica(tipoConstelacion, 4, SNR)
teorica_8_FSK = pes_teorica(tipoConstelacion, 8, SNR)
teorica_16_FSK = pes_teorica(tipoConstelacion, 16, SNR)


fig=plt.figure()
plt.grid(True)
plt.semilogy(EbNoDB, Pe2_FSK,'o', label=f'2-{tipoConstelacion} simulada', color='hotpink')
plt.semilogy(EbNoDB, teorica_2_FSK, label=f'2-{tipoConstelacion} teorica', color='hotpink')
plt.semilogy(EbNoDB, Pe4_FSK,'o', label=f'4-{tipoConstelacion} simulada', color='cornflowerblue')
plt.semilogy(EbNoDB, teorica_4_FSK, label=f'4-{tipoConstelacion} teorica', color='cornflowerblue')
plt.semilogy(EbNoDB, Pe8_FSK,'o', label=f'8-{tipoConstelacion} simulada', color='peru')
plt.semilogy(EbNoDB, teorica_8_FSK, label=f'8-{tipoConstelacion} teorica', color='peru')
plt.semilogy(EbNoDB, Pe16_FSK,'o', label=f'16-{tipoConstelacion} simulada', color='orchid')
plt.semilogy(EbNoDB, teorica_16_FSK, label=f'16-{tipoConstelacion} teorica', color='orchid')

plt.title('Probabilidad de error de simbolo')
plt.ylabel('Probabilidad de error')
plt.xlabel('EbNo')
plt.legend()


fig2 = plt.figure()

Pb2_FSK = peb_psk(Pe2_FSK,2)
Pb4_FSK = peb_psk(Pe4_FSK,4)
Pb8_FSK = peb_psk(Pe8_FSK,8)
Pb16_FSK = peb_psk(Pe16_FSK,16)


Pb_teorica_2_FSK = peb_psk(teorica_2_FSK,2)
Pb_teorica_4_FSK = peb_psk(teorica_4_FSK,4)
Pb_teorica_8_FSK = peb_psk(teorica_8_FSK,8)
Pb_teorica_16_FSK = peb_psk(teorica_16_FSK,16)

plt.grid(True)
plt.semilogy(EbNoDB, Pb2_FSK,'o', label=f'2-{tipoConstelacion} simulada', color='hotpink')
plt.semilogy(EbNoDB, Pb_teorica_2_FSK, label=f'2-{tipoConstelacion} teorica', color='hotpink')
plt.semilogy(EbNoDB, Pb4_FSK,'o', label=f'4-{tipoConstelacion} simulada', color='cornflowerblue')
plt.semilogy(EbNoDB, Pb_teorica_4_FSK, label=f'4-{tipoConstelacion} teorica', color='cornflowerblue')
plt.semilogy(EbNoDB, Pb8_FSK,'o', label=f'8-{tipoConstelacion} simulada', color='peru')
plt.semilogy(EbNoDB, Pb_teorica_8_FSK, label=f'8-{tipoConstelacion} teorica', color='peru')
plt.semilogy(EbNoDB, Pb16_FSK,'o', label=f'16-{tipoConstelacion} simulada', color='orchid')
plt.semilogy(EbNoDB, Pb_teorica_16_FSK, label=f'16-{tipoConstelacion} teorica', color='orchid')

plt.ylabel('Probabilidad de error')
plt.xlabel('EbNo')
plt.title('Probabilidad de error de bit')
plt.legend()

plt.show()
