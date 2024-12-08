import matplotlib.pyplot as plt
import numpy as np

def graficar_psk(ang_umbrales, psk_gray_map):
    # Crear figura
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    symbols = psk_gray_map.values()
    # Dibujar círculo unitario
    circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--', linewidth=1)
    ax.add_artist(circle)

    # Graficar símbolos PSK
    for sym, gray in psk_gray_map.items():
        plt.plot(sym.real, sym.imag, 'o', label=f'Gray: {format(gray, f"0{int(np.log2(len(psk_gray_map)))}b")}')
        plt.text(sym.real * 1.1, sym.imag * 1.1, f'{format(gray, f"0{int(np.log2(len(psk_gray_map)))}b")}',
                 color='blue', fontsize=10, ha='center')

    # Graficar umbrales
    angulo_radianes = np.radians(ang_umbrales)

    for theta in angulo_radianes:
        x = np.cos(theta)
        y = np.sin(theta)
        plt.plot([0, x], [0, y], color='red', linestyle='--', linewidth=1)

    # Configurar ejes
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.title("Constelación PSK con Umbrales y Código de Gray")
    plt.xlabel("Eje Real")
    plt.ylabel("Eje Imaginario")
    plt.grid(color='lightgray', linestyle='--', linewidth=0.5)
    # plt.legend(loc='upper right', fontsize=8)
    plt.show()

def graficar_ask(symbols, ang_umbrales, psk_gray_map):
    return


def graficar_fsk(symbols, ang_umbrales, psk_gray_map):
    return

def graficar_qam(symbols, ang_umbrales, psk_gray_map):
    return