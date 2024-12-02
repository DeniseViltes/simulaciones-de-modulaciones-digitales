import numpy as np
import matplotlib.pyplot as plt


# Función para graficar ASK
def plot_ask(d, M):
    symbols = np.arange(-((M - 1) / 2), ((M - 1) / 2) + 1) * d
    plt.figure(figsize=(8, 4))
    plt.scatter(symbols, np.zeros_like(symbols), c='b', label='Símbolos')
    plt.axhline(0, color='k', linewidth=0.8, linestyle='--')
    for pos in symbols + (d / 2):
        plt.axvline(pos, color='k', linewidth=0.8, linestyle='--')
    plt.title(f'Constelación ASK (M={M})')
    plt.xlabel('Amplitud')
    plt.yticks([])
    plt.xticks(symbols)
    plt.grid(False)
    plt.legend()
    plt.show()

# Función para graficar QAM
def plot_qam(d, M):
    size = int(np.sqrt(M))
    # hago una grilla de raiz de M * raiz de M
    x, y = np.meshgrid(np.arange(size) * d, np.arange(size) * d)

    # Depslazo las posiciones para que me den simétricas respecto a 0
    x = x.flatten() - ((size - 1) / 2) * d
    y = y.flatten() - ((size - 1) / 2) * d
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c='b', label='Símbolos')
    plt.axhline(0, color='k', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='k', linewidth=0.8, linestyle='--')
    plt.title(f'Constelación QAM (M={M})')
    plt.xlabel('')
    plt.ylabel('')
    plt.grid(True)
    plt.legend(loc='best')
    plt.axis('equal')
    plt.show()

# Función para graficar PSK
def plot_psk(d, M):
    #calculo el radio en func de dmin
    alpha = 2*np.pi / M
    radio = d / (2 * np.sin(alpha/2))
    angles = np.linspace(0, 2 * np.pi, M, endpoint=False) #endpoint para q no se repita 0 y 2pi
    x = np.cos(angles) * radio
    y = np.sin(angles) * radio
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c='b', label='Símbolos')
    plt.axhline(0, color='k', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='k', linewidth=0.8, linestyle='--')
    #zonas de decision
    for n in np.linspace(0, M-1, M):
        x1 = np.cos((n+0.5)*alpha) * 1.2 * radio
        y1 = np.sin((n+0.5)*alpha) * 1.2 * radio
        plt.plot([x1, 0], [y1, 0], 'k--', lw=1)
    plt.title(f'Constelación PSK (M={M})')
    plt.xlabel('')
    plt.ylabel('')
    plt.xticks(x[::2])
    plt.grid(True)
    plt.legend(loc='best')
    plt.axis('equal')
    plt.show()

def plot_fsk(d, M):

    if (M==2):
        alpha = np.pi / 4
        radio = np.sqrt(d)
        x = [radio, 0]
        y = [0, radio]
        plt.figure(figsize=(6, 6))
        plt.scatter(x, y, c='b', label='Símbolos')
        plt.axhline(0, color='k', linewidth=0.8, linestyle='--')
        plt.axvline(0, color='k', linewidth=0.8, linestyle='--')

        # zonas de decision
        x1 = np.cos(alpha) * 1.2 * radio
        y1 = np.sin(alpha) * 1.2 * radio
        plt.plot([x1, 0], [y1, 0], 'k--', lw=1)

    elif M == 3:
        coordinates = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
        # Crear el gráfico 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Etiquetas de los ejes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        # Dibujar los ejes coordenados
        ax.plot([0, 2], [0, 0], [0, 0], color='b', label="cos(f1)")  # Eje X
        ax.plot([0, 0], [0, 2], [0, 0], color='b', label="cos(f2)")  # Eje Y
        ax.plot([0, 0], [0, 0], [0, 2], color='b', label="cos(f3)")  # Eje Z
        # Dibujar zonas de decision
        ax.plot([0, 2], [0, 2], [0, 0], color='r', linestyle='--')  # Eje X
        ax.plot([0, 0], [0, 2], [0, 2], color='r', linestyle='--')  # Eje Y
        ax.plot([0, 2], [0, 0], [0, 2], color='r', linestyle='--')  # Eje Z
        # Graficar los puntos
        ax.scatter(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2], c='r', marker='o')
        # Añadir etiquetas a los puntos
        for i, (x, y, z) in enumerate(coordinates):
            ax.text(x, y, z, f'({x},{y},{z})', fontsize=12)
        # Ajustar límites para centrar el origen
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-0.5, 1.5])
        # Ajustar la vista
        ax.view_init(elev=30, azim=45)  # Cambiar la vista para una mejor perspectiva

    else:
        x = [0, d]
        y = [0, 0]
        plt.figure(figsize=(6, 6))
        plt.scatter(x, y, c='b', label='Símbolos')
        plt.axhline(0, color='k', linewidth=0.8, linestyle='--')
        plt.axvline(0, color='k', linewidth=0.8, linestyle='--')

        # zonas de decision
        plt.axvline(d/2, color='r', linewidth=0.8, linestyle='--')

    # Mostrar el gráfico
    plt.title(f'Gráfico FSK M={M}')
    plt.legend()
    plt.show()


# Configuración general
M = 16  #Cantidad de símbolos
d = 2  # Distancia mínima entre símbolos

plot_ask(d, M)
plot_qam(d, M)
plot_psk(d, M)
if M <= 3:
    plot_fsk(d, M)
