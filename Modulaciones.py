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
    symbols = np.arange(0, (((M - 1) / 2) + 1) * 2) * d
    n=len(symbols)
    symbols = normalizar_constelacion(symbols)
    symbols = np.real(symbols)
    d_norm = symbols[0]-symbols[1] # lo harcodeo
    umbrales= symbols[1:n-1] + (d_norm / 2)

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
    if M == 2:
        # Caso especial para 2-QAM (idéntico a 2-PSK)
        symbols = np.array([-d / 2, d / 2])
    else:
        # Constelación cuadrada para M-QAM
        size = int(np.sqrt(M))
        x, y = np.meshgrid(np.arange(size) * d, np.arange(size) * d)
        x = x.flatten() - ((size - 1) / 2) * d
        y = y.flatten() - ((size - 1) / 2) * d
        symbols = x + 1j * y

    symbols = normalizar_constelacion(symbols)

    # Calcular el valor normalizado
    size = int(np.sqrt(M))
    d_norm = symbols[0] - symbols[1]

    # Umbrales (para demodulación, en este caso, se usan para el mapeo)
    umbrales = np.arange(1, size)
    umbrales = umbrales * d_norm - (size / 2) * d_norm

    # Generar etiquetas binarias y convertirlas a Gray
    binary_labels = np.arange(M)
    gray_labels = [binary_to_gray(b) for b in binary_labels]

    # Mapeo entre códigos de Gray y los símbolos en la constelación
    gray_map = dict(zip(gray_labels, symbols))

    return gray_map, umbrales


def fsk(d, M):
    frecuencias = np.arange(M) * d
    binary_labels = np.arange(M)
    gray_labels = [binary_to_gray(b) for b in binary_labels]
    gray_map = dict(zip(gray_labels, frecuencias))
    return gray_map, frecuencias


