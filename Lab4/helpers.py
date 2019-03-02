import numpy as np
from pyexcel_ods import get_data

def getColumnFromSheet(data, sheetName, columnIndex):
    sheetData = np.array(data[sheetName])
    columnData = sheetData[:, columnIndex]
    columnData = np.delete(columnData, 0, 0)
    return np.asfarray(columnData,float).T