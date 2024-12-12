import numpy as np


def decisor_PSK(posiciones_originales,umbrales,M, posicion_recibida):
    posicion_recibida = np.angle(posicion_recibida[:]) * 180 / np.pi  # agregar q si es mayor a 360 restarle 360
    simbolos_estimado = np.zeros_like(posicion_recibida, dtype=complex)

    posiciones = posiciones_originales
    indice = 0
    for i in posicion_recibida:
        if i < 0:
            i += 360
        j = 0
        simbolos_estimado[indice] = posiciones[0] ##inicializo
        for umbral in umbrales:
            if i <= umbral:
                simbolos_estimado[indice] = posiciones[j]
                break
            elif i > umbral:
                j += 1
            else:
                simbolos_estimado[indice] = posiciones[0]
        indice += 1

    return simbolos_estimado


def decisor_ASK(posiciones_originales,umbrales,M, posicion_recibida):
    simbolo_estimado = np.zeros_like(posicion_recibida)
    posiciones = list(posiciones_originales)
    sim = 0
    for pos in posicion_recibida:
        indice = 0
        for umbral in umbrales:
            simbolo_estimado[sim] = posiciones[indice]
            if pos > umbral:
                indice += 1
                simbolo_estimado[sim] = posiciones[indice]
        sim += 1

    return np.array(simbolo_estimado)


def decisor_QAM(posiciones_originales,umbrales,M, posicion_recibida):
    k_filas = int(np.log2(M))
    simbolos_estimado = np.zeros_like(posicion_recibida, dtype=complex)
    posiciones = np.sort(posiciones_originales)
    umbrales = np.sort(np.real(umbrales))
    indice = 0

    for pos in posicion_recibida:

        x = np.real(pos)
        y = np.imag(pos)

        # forma 1

        indice_x = 0
        indice_y = 0

        for i in umbrales:
            if x <= i:
                break
            else:
                indice_x += 1
        for j in umbrales:
            if y <= j:
                break
            else:
                indice_y += 1
        simbolos_estimado[indice] = posiciones[indice_x * k_filas + indice_y]
        indice += 1

    return simbolos_estimado


def decisor_FSK(posiciones,umbrales,M, posicion_recibida):
    indices_estimados = []
    for pos in posicion_recibida:
        correlacion = np.dot(pos, posiciones)
        detected_symbol = np.argmax(correlacion)
        indices_estimados.append(detected_symbol)
    return np.array(indices_estimados)
