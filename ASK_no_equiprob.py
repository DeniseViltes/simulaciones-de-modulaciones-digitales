import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# Parámetros
p = 1/4
q = 1 - p
M = 2  # 2-ASK
EbN0_dB = np.arange(0, 19, 1)  # Eb/N0 en dB
EbN0 = 10**(EbN0_dB / 10)  # Eb/N0 lineal
N = int(1e6)  # Número de símbolos simulados
Eb = 1
# Amplitudes de los símbolos
s0 = 0
s1 = np.sqrt(2*Eb)
# Probabilidad de error teórica
Pe_teorica = []
for ebn0 in EbN0:
    sigma = np.sqrt(Eb / (2 * ebn0))
    T = ((sigma**2) * np.log(p / q) + Eb)/np.sqrt(2*Eb)
    Pe = (p * 0.5 * erfc((T - s0) / (np.sqrt(2) * sigma)) +
          q * 0.5 * erfc((s1 - T) / (np.sqrt(2) * sigma)))
    Pe_teorica.append(Pe)

# Simulación Monte Carlo
Pe_simulada = []
for ebn0 in EbN0:
    sigma = np.sqrt(Eb / (2 * ebn0))
    ruido = np.random.normal(0, sigma, N)
    enviados = np.random.choice([s0, s1], size=N, p=[p, q])
    #elije N veces cual enviar entre s0 y s1 según cual es mas probable

    recibidos = enviados + ruido
    T = ((sigma ** 2) * np.log(p / q) + Eb) / np.sqrt(2 * Eb)
    decisiones = np.where(recibidos >= T, s1, s0)
    errores = (decisiones != enviados).sum()
    Pe_simulada.append(errores / N) #Divido porque promedio la cant de errores para obtener la Pe

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.semilogy(EbN0_dB, Pe_teorica, label="Teórica", linestyle='-', marker='o')
plt.semilogy(EbN0_dB, Pe_simulada, label="Simulada", linestyle='--', marker='x')
plt.xlabel(r"$E_b/N_0$ [dB]")
plt.ylabel(r"Probabilidad de error $P_e$")
plt.title(r"Probabilidad de error para 2-ASK con $p=1/4$ y $q=3/4$")
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.show()
