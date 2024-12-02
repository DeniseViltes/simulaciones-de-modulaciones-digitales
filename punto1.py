import numpy as np
import matplotlib.pyplot as plt


def validar_M(M):
    if not (M > 0 and (M & (M - 1)) == 0):
        raise ValueError("M debe ser una potencia de 2.")
    if M > 2 and not (np.sqrt(M).is_integer()):
        raise ValueError("Para QAM, M debe tener una raíz cuadrada entera si M > 2.")


def normalizar_constelacion(symbols):

    symbols = np.array(symbols, dtype=complex)
    potencia_promedio = np.mean(np.abs(symbols)**2)

    return symbols / np.sqrt(potencia_promedio)


# Función para graficar ASK
def plot_ask(d, M):
    validar_M(M)
    symbols = np.arange(-((M - 1) / 2), ((M - 1) / 2) + 1) * d
    symbols = normalizar_constelacion(symbols)

    d_norm = symbols[0]-symbols[1] # lo harcodeo
    plt.figure(figsize=(8, 4))
    plt.axhline(0, color='k', linewidth=0.8, linestyle='--')
    plt.scatter(symbols, np.zeros_like(symbols), c='plum')
    for pos in symbols[1:] + (d_norm / 2):
        plt.axvline(pos, color='crimson', linewidth=0.8, linestyle='--')
    plt.title(f'Constelación PAM (M={M})')
    plt.xlabel('I')
    plt.yticks([])
    plt.xticks(symbols, fontsize=10, rotation=45)
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(f'results/{M}-PAM.png')
    plt.show()


# Función para graficar QAM
def plot_qam(d, M):
    validar_M(M)

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

    # Normalizar la constelación
    symbols = normalizar_constelacion(symbols)
    size = int(np.sqrt(M))  # Número de filas y columnas en la cuadrícula
    d_norm = symbols[0]-symbols[1]
    # Graficar
    plt.figure(figsize=(6, 6))
    for i in range(1, size):
        plt.axhline(i * d_norm - (size / 2) * d_norm, color='crimson', linestyle='--', lw=1)
        plt.axvline(i * d_norm - (size / 2) * d_norm, color='crimson', linestyle='--', lw=1)

    for i in range(size - 1):
        for j in range(size - 1):
            # Coordenadas de las esquinas opuestas de la celda (i, j)
            x1 = symbols[i + j * size].real
            y1 = symbols[i + j * size].imag
            x2 = symbols[(i + 1) + (j + 1) * size].real
            y2 = symbols[(i + 1) + (j + 1) * size].imag

            # Dibujar la primera diagonal (de la esquina inferior izquierda a la superior derecha)
            plt.plot([x1, x2], [y1, y2], '--', lw=1,color='peru')

            # Segunda diagonal (de la esquina inferior derecha a la superior izquierda)
            x1 = symbols[(i + 1) + j * size].real
            y1 = symbols[(i + 1) + j * size].imag
            x2 = symbols[i + (j + 1) * size].real
            y2 = symbols[i + (j + 1) * size].imag

            plt.plot([x1, x2], [y1, y2], '--', lw=1,color='peru')

    plt.scatter(symbols.real, symbols.imag, c='plum')
    plt.axhline(0, color='k', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='k', linewidth=0.8, linestyle='--')
    plt.title(f'Constelación QAM (M={M})')
    plt.xlabel('I')
    plt.xlabel('Q')
    # plt.grid(True)
    plt.axis('equal')
    plt.savefig(f'results/{M}-QAM.png')
    plt.show()


# Función para graficar PSK
def plot_psk(d, M):
    validar_M(M)
    alpha = 2 * np.pi / M
    radio = d / (2 * np.sin(alpha / 2))
    angles = np.linspace(0, 2 * np.pi, M, endpoint=False)
    symbols = normalizar_constelacion(radio * np.exp(1j * angles))

    plt.figure(figsize=(6, 6))
    plt.scatter(symbols.real, symbols.imag, c='plum', label='Símbolos')
    plt.axhline(0, color='k', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='k', linewidth=0.8, linestyle='--')
    for n in range(M):
        x1 = np.cos((n + 0.5) * alpha) * 0.3 * radio
        y1 = np.sin((n + 0.5) * alpha) * 0.3 * radio
        plt.plot([x1, 0], [y1, 0], '--', lw=1, color= 'crimson')
    plt.title(f'Constelación PSK (M={M})')
    plt.xlabel('I')
    plt.xlabel('Q')
    # plt.grid(True)
    plt.axis('equal')
    plt.savefig(f'results/{M}-PSK.png')
    plt.show()


def plot_2fsk(d):
    # Símbolos para 2-FSK con energía Eb
    Eb = (d ** 2) / 2  # Eb = (d^2) / 2 para 2 símbolos ortogonales

    # Símbolos para 2-FSK, separados por la distancia mínima
    symbols_fsk = [np.sqrt(Eb) * 1j, np.sqrt(Eb) * 1]  # Un símbolo en eje real, otro en eje imaginario

    # Normalizar la constelación
    symbols_normalizados = normalizar_constelacion(symbols_fsk)

    # Gráfica de la constelación
    plt.figure(figsize=(6, 6))
    plt.scatter(symbols_normalizados.real, symbols_normalizados.imag, color='plum', s=100)


    x = np.linspace(0, 1.2, 100)
    plt.plot(x, x, color='crimson', linestyle='--', lw=1)

    # Configuración de la gráfica
    plt.axhline(0, color='gray', lw=1)
    plt.axvline(0, color='gray', lw=1)
    plt.title(f'Constelación 2-FSK')
    plt.xlabel('I')
    plt.ylabel('Q')
    plt.grid(True)
    plt.axis('equal')
    plt.savefig('results/2-FSK.png')
    plt.show()


# Configuración general
M =16  # Cantidad de símbolos
d = 2  # Distancia mínima entre símbolos

# plot_ask(d, M)
plot_qam(d, M)
# plot_psk(d, M)
# plot_2fsk(d)
