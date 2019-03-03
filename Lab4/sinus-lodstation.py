import numpy as np
import matplotlib.pyplot as plt
import math as math

f = 50
ω = 2 * math.pi * f
T = 1/f
xp = np.linspace(0, T, 100)
yp = 230 * np.sin(ω * xp)


fig, ax1 = plt.subplots()
ax1.plot(xp * 1000 ,yp, color='green',linestyle='-')
ax1.set_xlabel('tid (ms)')
ax1.set_ylabel('Nätspänning (V)', color='green')

ax2 = ax1.twinx()
Vmpp = 57 / 1000
Ymax = Vmpp * 738 / (503 * 2)
ax2.plot(5, Vmpp*1000/2, marker='.', color='yellow', label='Låg värme')
ax2.plot(5, Vmpp*1000/2, marker='.', color='orange', label='Mellan värme')
ax2.plot(5, Vmpp*1000/2, marker='.', color='red', label='Hög värme')
ax2.set_ylabel('Strömsensor mätspänning (mV)')
ax2.set_ylim(-Ymax*1000, Ymax*1000)
ax1.axhline(linewidth=1, color='lightgray', linestyle=':')



plt.legend()
plt.show()

#fig.tight_layout()
plt.show()