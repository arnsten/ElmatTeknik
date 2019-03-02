import numpy as np
import matplotlib.pyplot as plt
from pyexcel_ods import get_data
import helpers as helpers

spreadsheetData = get_data("Lab4-18.ods")
sheetName = "Kalibrering"
Im = helpers.getColumnFromSheet(spreadsheetData, sheetName, 1)
Vut = helpers.getColumnFromSheet(spreadsheetData, sheetName, 2)

coeff = np.polyfit(Im, Vut, 1)
print(coeff)
p3 = np.poly1d(coeff)
xp = np.linspace(np.amin(Im), np.amax(Im), 100)

plt.axhline(p3(0), color='lightgray', linestyle='--', linewidth=1)
plt.axvline(0, color='lightgray', linestyle='--', linewidth=1)
plt.plot(
    Im,
    Vut,
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
    label="Vut = %.2f * Im + %.2f" % (coeff[0], coeff[1])
)
plt.xlabel('Im (A)')
plt.ylabel('Vut (V)')
#plt.title("Kalibrering av strömsensor")
plt.legend()
plt.show()
