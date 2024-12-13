from Constelacion import *
from version_coke import *

M=16
d=2

ask=Constelacion(d,M,'ASK')
psk=Constelacion(d,M,'PSK')
qam=Constelacion(d,M,'QAM')

ask.graficar()
psk.graficar()
qam.graficar()

plot_fsk(d,2)
plot_fsk(d,3)