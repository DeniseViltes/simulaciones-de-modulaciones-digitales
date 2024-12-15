from Constelacion import *
from version_coke import *

M=8
d=2

ask=Constelacion(d,M,'ASK')
psk=Constelacion(d,M,'PSK')
# qam=Constelacion(d,M,'QAM')

ask_plot = ask.graficar()
psk_plot = psk.graficar()
# qam.graficar()
#
# plot_fsk(d,2)
# plot_fsk(d,3)

plt.show()