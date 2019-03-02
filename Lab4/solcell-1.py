import numpy as np
import matplotlib.pyplot as plt
from pyexcel_ods import get_data
import helpers as helpers

spreadsheetData = get_data("Lab4-13.ods")
sheetName = "Solcell 2013-Si-02"
Vm = helpers.getColumnFromSheet(spreadsheetData, sheetName, 0)
Temp = helpers.getColumnFromSheet(spreadsheetData, sheetName, 1)

coeff = np.polyfit(Temp, Vm, 2)
print(coeff)
p3 = np.poly1d(coeff)
xp = np.linspace(np.amin(Temp), np.amax(Temp), 100)

plt.plot(
    Temp,
    Vm,
    color='black',
    marker='.',
    linestyle='None',
    label="Mätdata"
)
plt.plot(
    xp,
    p3(xp),
    color='red',
    linestyle="dotted",
    label="Polyfit (2:a grad)"
)
plt.xlabel('Temp (°C)')
plt.ylabel('Vm (V)')
#plt.title("Spänning från solcell med olika temperatur")
plt.legend()
plt.show()
