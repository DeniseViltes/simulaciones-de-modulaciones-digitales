from  graficadores import *

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

    symbols = normalizar_constelacion(symbols)

    # Calcular el valor normalizado
    size = int(np.sqrt(M))
    d_norm = np.abs(symbols[0] - symbols[1])

    umbrales = []
    for i in range(1, size):
        umbrales.append( i * d_norm - (size / 2) * d_norm)
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


# simbolos posibles posicion {d000 0d00 00d0 000d } M = 4 (coordenadas) -- codigo --> {00 01 10 11} M = 4 --> n_b = log2(M)
# originales (coord) [ 0d00 d000  00d0 ...] -- codigo -->  bitArraySend = [01 00 10 ...]

#analogico con ruido [r1 dr2 r3 r4] --deco--> [0 d 0 0]

# bits -> coord -> ruido -> correlado -> decisor -> bits

'''
d 0 0 0 0 0 0 0= 0 --> bin 000
0 d 0 0 0 0 0 0= 1 --> bin 001
0 0 d 0 0 0 0 0= 2 --> bin 010
0 0 0 d 0 0 0 0= 3 --> bin 011
0 0 0 0 d 0 0 0= 4 --> bin 100 
0 0 0 0 0 d 0 0= 5 --> bin 101
0 0 0 0 0 0 d 0= 6 --> bin 110
0 0 0 0 0 0 0 d= 7 --> bin 111
    0
    .
    .
    M * d

Peb -->  Peb = (M-2)/M Pes

'''

'''
pos * eye_simb
[r d_r r r]  d 0 0 0 = [dr d_r*d rd dr] --> buscar indice elem max {coord} --> 
            0 d 0 0
            0 0 d 0
            0 0 0 d
'''