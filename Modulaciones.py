from  graficadores import *

def normalizar_constelacion(sim):

    # sim = np.array(sim, dtype=complex)
    potencia_promedio = np.mean(np.abs(sim) ** 2)
    return sim / np.sqrt(potencia_promedio)

def binary_to_gray(binary):
    return binary ^ (binary >> 1)

def ask(d, M):
    symbols = np.arange(0, M) * d
    n=len(symbols)
    # symbols = normalizar_constelacion(symbols)
    # symbols = np.real(symbols)
    umbrales= symbols[0:n-1] + (d / 2)

    binary_labels = np.arange(M)  # Etiquetas binarias [0, 1, ..., M-1]
    gray_labels = [binary_to_gray(b) for b in binary_labels]
    gray_map = dict(zip(gray_labels,symbols))


    return gray_map,umbrales


def psk(d, M):
    alpha = 2 * np.pi / M
    radio = d / (2 * np.sin(alpha / 2))
    angles = np.linspace(0, 2 * np.pi, M, endpoint=False)

    symbols= radio * np.exp(1j * angles)
    # symbols = normalizar_constelacion(symbols)

    ang_umbrales= np.zeros(M)

    for n in range(M):
        ang_umbrales[n] = 360 * (2*n + 1) / (2*M)

    binary_labels = np.arange(M)  # Etiquetas binarias [0, 1, ..., M-1]
    gray_labels = [binary_to_gray(b) for b in binary_labels]
    gray_map = dict(zip(gray_labels,symbols))

    return gray_map,ang_umbrales


def qam(d, M):
    if M == 2:
        # Caso especial para 2-QAM
        symbols = np.array([-d/2 , d/2]) # = [a,b]
        umbral = [0]
        gray_labels = {0 , 1}
        gray_map = dict(zip(gray_labels, symbols))
        return gray_map,umbral
    else:
        # Constelación cuadrada para M-QAM
        size = int(np.sqrt(M))
        x, y = np.meshgrid(np.arange(size) * d, np.arange(size) * d)
        x = x.flatten() - ((size - 1) / 2) * d
        y = y.flatten() - ((size - 1) / 2) * d
        symbols = x + 1j * y

    # symbols = normalizar_constelacion(symbols)

    # Calcular el valor normalizado
    size = int(np.sqrt(M))

    umbrales = []
    for i in range(1, size):
        umbrales.append( i * d - (size / 2) * d)
    umbrales = np.array(umbrales)


    snake_indices = []
    for row in range(size):
        if row % 2 == 0:
            # Recorrer de izquierda a derecha
            snake_indices.extend(range(row * size, (row + 1) * size))
        else:
            # Recorrer de derecha a izquierda
            snake_indices.extend(range((row + 1) * size - 1, row * size - 1, -1))

    symbols = symbols[snake_indices]
    # Etiquetas en Gray para las coordenadas I y Q
    gray_i = [binary_to_gray(i) for i in range(size)]
    gray_q = [binary_to_gray(q) for q in range(size)]

    # Construir el mapeo final (Gray para I y Q)
    gray_map = {}
    for idx, symbol in enumerate(symbols):
        i_idx = int(idx % size)  # Índice para I
        q_idx = int(idx // size)  # Índice para Q
        gray_code = (gray_q[q_idx] << (size.bit_length() - 1)) | gray_i[i_idx]
        gray_map[gray_code] = symbol


    binary_labels = np.arange(M)
    gray_labels = [binary_to_gray(b) for b in binary_labels]

    gray_map = dict(zip(gray_labels, symbols))
    return gray_map, umbrales

# Revsar fsk
def fsk(d, M):
    # devuelvo el umbral vacio, no uso el umbral en el decisor
    # symbols = np.eye(M)
    umbrales = []
    map = {} # diccionario
    for i in range(M):
        simbolo = np.zeros(M)
        simbolo[i] = d
        map[i] = simbolo
    #binary_labels = np.arange(M)
    #gray_labels = [binary_to_gray(b) for b in binary_labels]
    #gray_map = dict(zip(gray_labels, symbols))
    return map, umbrales

