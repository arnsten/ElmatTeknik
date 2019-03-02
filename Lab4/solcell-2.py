import numpy as np
import matplotlib.pyplot as plt
from pyexcel_ods import get_data
from scipy.interpolate import BSpline
import helpers as helpers

#
spreadsheetData = get_data("Lab4-13.ods")
sheetNames = ["Vänster koppling", "Höger koppling"]
colors = ["red", "blue"]
for index, sheetName in enumerate(sheetNames):
    color = colors[index]
    data = helpers.getColumnFromSheet(spreadsheetData, sheetName, [0,1]).T
    sortedData = data[data[:,1].argsort()]
    Im = sortedData[:, 1].T
    Vm = sortedData[:, 0].T
    cs = BSpline(Im, Im*Vm, 1)
    xp = np.linspace(np.amin(Im), np.amax(Im), 100)
    #plt.plot(
    plt.plot(
        Vm,
        Im,
        color=color,
        marker='.',
        linestyle='-',
        label=sheetName  
    )
    
    # plt.plot(
    #     xp,
    #     cs(xp),
    #     color=color,
    #     linestyle="dotted",
    #     label=sheetName        
    # )

plt.xlabel('Vm (V)')
plt.ylabel('Im (A)')

#plt.title("Spänning och ström från solcell med olika motstånd.")
plt.legend()
plt.show()
