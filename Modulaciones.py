from  graficadores import *


def array_binario_a_gray(arr):
    # Aseguramos que el array esté en formato de tipo int
    arr = np.array(arr, dtype=int)
    suma = 0
    j = 0
    for i in arr[::-1]:
        suma += i*2**j
        j += 1
    return binary_to_gray(suma)

def normalizar_constelacion(sim):

    sim = np.array(sim, dtype=complex)
    potencia_promedio = np.mean(np.abs(sim) ** 2)

    return sim / np.sqrt(potencia_promedio)

def binary_to_gray(binary):
    return binary ^ (binary >> 1)

def ask(d, M):
    symbols = np.arange(-((M - 1) / 2), ((M - 1) / 2) + 1) * d
    # symbols = normalizar_constelacion(symbols)
    # symbols = np.real(symbols)
    d_norm = symbols[0]-symbols[1] # lo harcodeo
    umbrales= symbols[1:] + (d_norm / 2)

    binary_labels = np.arange(M)  # Etiquetas binarias [0, 1, ..., M-1]
    gray_labels = [binary_to_gray(b) for b in binary_labels]
    gray_map = dict(zip(gray_labels,symbols))


    return gray_map,umbrales


def psk(d, M):
    alpha = 2 * np.pi / M
    radio = d / (2 * np.sin(alpha / 2))
    angles = np.linspace(0, 2 * np.pi, M, endpoint=False)

    symbols = normalizar_constelacion(radio * np.exp(1j * angles))

    ang_umbrales= np.zeros(M)

    for n in range(M):
        ang_umbrales[n] = 360 * (2*n + 1) / (2*M)

    binary_labels = np.arange(M)  # Etiquetas binarias [0, 1, ..., M-1]
    gray_labels = [binary_to_gray(b) for b in binary_labels]
    gray_map = dict(zip(gray_labels,symbols))

    return gray_map,ang_umbrales

def qam(d, M):
    return

def fsk(d, M):
    return



# d=2
# M = 16
# #symbols, umbrales, pam_gray_map = pam(d, M)
# umbrales, psk_gray_map = psk(d, M)
#
# # graficar_psk(umbrales,psk_gray_map)
#
# print("Umbrales:", umbrales)
# print("Mapa PSK a Gray:")
# for sym, gray in psk_gray_map.items():
#     print(f"Símbolo: {sym:.2f}, Código de Gray: {format(gray, f'0{int(np.log2(M))}b')}")