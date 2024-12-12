import matplotlib.pyplot as plt
import numpy as np

def graficar_psk(ang_umbrales, psk_gray_map):
    # Crear figura
    plt.figure(figsize=(8, 8))
    ax = plt.gca()

    # Dibujar círculo unitario
    circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--', linewidth=1)
    ax.add_artist(circle)

    # Graficar símbolos PSK
    for gray,sym in psk_gray_map.items():
        plt.plot(sym.real, sym.imag, 'o',color = 'crimson', label=f'Gray: {format(gray, f"0{int(np.log2(len(psk_gray_map)))}b")}')
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

def graficar_ask(umbrales, gray_map):
    symbols = list(gray_map.values())
    M = len(symbols)
    plt.figure(figsize=(8, 4))
    plt.axhline(0, color='k', linewidth=0.8, linestyle='--')

    for pos in umbrales:
        plt.axvline(pos, color='crimson', linewidth=0.8, linestyle='--')

    for gray,sym in gray_map.items():
        plt.plot(sym.real, sym.imag, 'o',color = 'crimson', label=f'Gray: {format(gray, f"0{int(np.log2(len(gray_map)))}b")}')
        plt.text(sym.real * 1, sym.imag +0.01, f'{format(gray, f"0{int(np.log2(len(gray_map)))}b")}',
                 color='blue', fontsize=10, ha='center')
    plt.title(f'Constelación ASK (M={M})')
    plt.xlabel('I')
    plt.yticks([])
    plt.xticks(symbols, fontsize=10, rotation=45)
    plt.grid(False)
    plt.tight_layout()
    plt.savefig(f'results/{M}-PAM.png')
    plt.show()


def graficar_fsk(umbrales, gray_map):
    # symbols = list(gray_map.values())
    # codigo = list(gray_map.keys())
    # M = len(symbols)
    # if M != 2 :
    #     return None
    # for i in range(M):
    #     plt.plot(symbols[i][0],symbols[i][1])
    #     plt.text(symbols[i][0],symbols[i][1], f'{codigo[i]}', color='red', fontsize=10, ha='center')
    # fig = plt.figure()
    # plt.title(f'Constelación FSK (M={M})')
    # plt.xlabel('I')
    # plt.xlabel('Q')
    # # plt.grid(True)
    # plt.axis('equal')
    # plt.savefig(f'results/{M}-PAM.png')
    # plt.show()
    return

def graficar_qam(umbrales, gray_map):
    symbols = list(gray_map.values())

    M = len(symbols)
    fig = plt.figure()
    plt.axhline(0, color='k', linewidth=0.8, linestyle='--')
    plt.axvline(0, color='k', linewidth=0.8, linestyle='--')
    for i in umbrales.real:
        plt.axhline(i, color='crimson', linestyle='--', lw=1)
        plt.axvline(i, color='crimson', linestyle='--', lw=1)


    for gray, sym in gray_map.items():
        sym = complex(sym)
        plt.plot(sym.real, sym.imag, 'o', color='crimson',
                 label=f'Gray: {format(gray, f"0{int(np.log2(len(gray_map)))}b")}')
        plt.text(sym.real * 1, sym.imag +0.05, f'{format(gray, f"0{int(np.log2(len(gray_map)))}b")}',
                 color='blue', fontsize=10, ha='center')

    plt.title(f'Constelación QAM (M={M})')
    plt.xlabel('I')
    plt.xlabel('Q')
    # plt.grid(True)
    plt.ylim([-1.3, 1.3])
    plt.xlim([-1.3, 1.3])
    plt.savefig(f'results/{M}-QAM.png')
    plt.show()