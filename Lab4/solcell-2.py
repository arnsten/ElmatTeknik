import numpy as np
import matplotlib.pyplot as plt
from pyexcel_ods import get_data
from scipy.interpolate import CubicSpline
import helpers as helpers

def sortAndRemoveDuplicates(X,Y):
    i = np.argsort(X)
    sortedX = X[i]
    sortedY = Y[i]
    (newX, uniqueIndx) = np.unique(sortedX, return_index=True)
    newY = sortedY[uniqueIndx]
    return (newX, newY)
#
spreadsheetData = get_data("Lab4-13.ods")
sheetName = "Höger koppling"
data = helpers.getColumnFromSheet(spreadsheetData, sheetName, [0,1]).T

(Vm, Im) = sortAndRemoveDuplicates(data[:, 0].T, data[:, 1].T)
cs = CubicSpline(Vm, Im)
xp = np.linspace(np.amin(Vm), np.amax(Vm), 100)

fig, ax1 = plt.subplots()
ax1.plot(0.11, 22.25, clip_on=False, marker='o', markersize='10', linestyle='none', color='red', label='Isc = 22.3 A')
ax1.plot(7.58, -0.1, clip_on=False, marker='v', markersize='10', linestyle='none', color='black', label='Voc = 7.58 V')

ax1.plot(
    Vm,
    Im,
    color='red',
    marker='.',
    linestyle='none'
)
ax1.plot(
    xp,
    cs(xp),
    color='red',
    linestyle="dotted"
)
ax1.legend(loc='center left')
ax1.set_xlabel('Spänning (V)')
ax1.set_ylabel('Ström (A)', color='red')
ax1.set_xlim(0, 8)
ax1.set_ylim(0, 24)

Pm = Im*Vm
ax2 = ax1.twinx()
ax2.set_ylabel('Effekt (W)', color='blue')
ax2.set_ylim(0, 200)
ax2.plot(
    Vm,
    Pm,
    color='blue',
    marker='.',
    linestyle='none',
    label='Mätdata'
)
cs = CubicSpline(Vm, Pm)
xp = np.linspace(np.amin(Vm), np.amax(Vm), 100)
ax2.plot(
    xp,
    cs(xp),
    color='blue',
    linestyle="dotted",
    label='Kubisk spline interpolation'
)

#plt.title("Spänning och ström från solcell med olika motstånd.")
#plt.legend()
plt.show()
