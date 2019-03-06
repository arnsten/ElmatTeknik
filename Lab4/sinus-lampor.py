import numpy as np
import matplotlib.pyplot as plt
import math as math

f = 50
ω = 2 * math.pi * f
T = 1/f
xp = np.linspace(0, T, 100)
yp = 230 * math.sqrt(2) * np.sin(ω * xp)

#
fig, ax1 = plt.subplots()
ax1.plot(xp * 1000 ,yp, color='green',linestyle='-')
ax1.set_xlabel('tid (ms)')
ax1.set_ylabel('Nätspänning (V)', color='green')

ax2 = ax1.twinx()
Vmpp = 43 / 1000
Ymax = Vmpp * 738 / (368*2)
ax2.plot(5, 43/2, marker='.', color='pink', label='Glödlampa')
ax2.plot(5, 17/2, marker='.', color='violet', label='LED-lampa')
ax2.set_ylabel('Strömsensor mätspänning (mV)')
ax2.set_ylim(-Ymax*1000, Ymax*1000)
ax1.axhline(linewidth=1, color='lightgray', linestyle=':')



plt.legend()
plt.show()

#fig.tight_layout()
plt.show()