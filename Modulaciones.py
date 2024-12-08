import numpy as np

def validar_M(M):
    if not (M > 0 and (M & (M - 1)) == 0):
        raise ValueError("M debe ser una potencia de 2.")
    if M > 2 and not (np.sqrt(M).is_integer()):
        raise ValueError("Para QAM, M debe tener una raíz cuadrada entera si M > 2.")


def normalizar_constelacion(symbols):

    symbols = np.array(symbols, dtype=complex)
    potencia_promedio = np.mean(np.abs(symbols)**2)

    return symbols / np.sqrt(potencia_promedio)

def binary_to_gray(binary):
    """Convierte un número binario a código de Gray"""
    return binary ^ (binary >> 1)

def pam(d, M):
    validar_M(M)
    symbols = np.arange(-((M - 1) / 2), ((M - 1) / 2) + 1) * d
    # symbols = normalizar_constelacion(symbols)
    # symbols = np.real(symbols)
    d_norm = symbols[0]-symbols[1] # lo harcodeo
    umbrales= symbols[1:] + (d_norm / 2)

    binary_labels = np.arange(M)  # Etiquetas binarias [0, 1, ..., M-1]
    gray_labels = [binary_to_gray(b) for b in binary_labels]
    pam_gray_map = dict(zip(symbols, gray_labels))


    return symbols,umbrales,pam_gray_map


def psk(d, M):
    validar_M(M)
    alpha = 2 * np.pi / M
    radio = d / (2 * np.sin(alpha / 2))
    angles = np.linspace(0, 2 * np.pi, M, endpoint=False)
    #print("angulos de simbolos: ",angles*180/np.pi)
    #print(range(M-1))
    symbols = normalizar_constelacion(radio * np.exp(1j * angles))

    ang_umbrales= np.zeros(M)

    for n in range(M):
        ang_umbrales[n] = 360 * (2*n + 1) / (2*M)

    binary_labels = np.arange(M)  # Etiquetas binarias [0, 1, ..., M-1]
    gray_labels = [binary_to_gray(b) for b in binary_labels]
    psk_gray_map = dict(zip(symbols, gray_labels))

    return symbols, ang_umbrales, psk_gray_map

d = 2
M = 16
#symbols, umbrales, pam_gray_map = pam(d, M)
symbols, umbrales, psk_gray_map = psk(d, M)


print("Símbolos:", symbols)
print("Umbrales:", umbrales)
print("Mapa PSK a Gray:")
for sym, gray in psk_gray_map.items():
    print(f"Símbolo: {sym:.2f}, Código de Gray: {format(gray, f'0{int(np.log2(M))}b')}")