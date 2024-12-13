import numpy as np
from scipy.special import erfc
def peb_fsk(pes, M ):
    return pes * 2 *(M-1)/M

def peb_ask(pes, M):
    return pes / np.log2(M)

def peb_psk(pes, M):
    return pes / np.log2(M)

def peb_qam(pes, M):
    return pes/np.log2(M)


def Q(x):
    return 0.5 * erfc(x / np.sqrt(2))


def pes_teorica(tipoConstelacion,M,eb_no):
        k = np.log2(M)
        if tipoConstelacion == 'FSK':
            Neig = (M-1)
            argumento = np.sqrt(eb_no*k)
        elif tipoConstelacion == 'ASK':
            Neig = 2*(1-1/M)
            argumento = np.sqrt(6*eb_no*k/(M**2-1))
        elif tipoConstelacion == 'PSK':
            Neig = 1
            if M>2:
                Neig = 2
            argumento = np.sqrt(2*eb_no*k)*np.sin(np.pi/M)
        else:
            Neig =4*(1-1/np.sqrt(M))
            argumento = np.sqrt((3*eb_no*k/(M-1)))
        return Neig * Q(argumento)

