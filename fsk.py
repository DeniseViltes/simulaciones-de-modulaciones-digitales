import numpy as np
import matplotlib.pyplot as plt
#
#
# # Función para normalizar la constelación
# def normalizar_constelacion(symbols):
#     symbols = np.array(symbols, dtype=complex)
#     potencia_promedio = np.mean(np.abs(symbols) ** 2)
#     return symbols / np.sqrt(potencia_promedio)
#
#
# # Función principal para graficar la constelación 2-FSK con distancia mínima
# def graficar_constelacion_fsk(d):
#     # Calculamos la energía del bit Eb a partir de la distancia mínima
#     Eb = (d ** 2) / 2  # Eb = (d^2) / 2 para 2 símbolos ortogonales
#
#     # Símbolos para 2-FSK, separados por la distancia mínima
#     symbols_fsk = [np.sqrt(Eb) * 1j, np.sqrt(Eb) * 1]  # Un símbolo en eje real, otro en eje imaginario
#
#     # Normalizar la constelación
#     symbols_normalizados = normalizar_constelacion(symbols_fsk)
#
#     # Gráfica de la constelación
#     plt.figure(figsize=(6, 6))
#     plt.scatter(symbols_normalizados.real, symbols_normalizados.imag, color='blue', s=100, label='Símbolos')
#
#     # Línea divisoria a 45° (y = x)
#     x = np.linspace(0, 1.2, 100)
#     plt.plot(x, x, color='red', linestyle='--', lw=1, label='Zona de decisión (45°)')
#
#     # Configuración de la gráfica
#     plt.axhline(0, color='gray', lw=1)
#     plt.axvline(0, color='gray', lw=1)
#     plt.title(f'Constelación 2-FSK Normalizada con d = {d}')
#     plt.xlabel('Parte Real')
#     plt.ylabel('Parte Imaginaria')
#     plt.grid(True)
#     plt.axis('equal')
#     plt.legend()
#     plt.show()
#
#
# # Llamada a la función principal con la distancia mínima deseada
# distancia_minima = 2  # Puedes cambiar este valor según necesites
# graficar_constelacion_fsk(distancia_minima)



from Modulaciones import *


simbolos,umbrales = fsk(2,2)

print(simbolos)