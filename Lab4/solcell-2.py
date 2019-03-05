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

print(Vm)
plt.plot(
    Vm,
    Im,
    color='black',
    marker='.',
    linestyle='none',
    label='Mätdata'
)
    
plt.plot(
    xp,
    cs(xp),
    color='gray',
    linestyle="dotted",
    label='Kubisk spline interpolation'
)

plt.xlabel('Vm (V)')
plt.ylabel('Im (A)')

#plt.title("Spänning och ström från solcell med olika motstånd.")
plt.legend()
plt.show()
