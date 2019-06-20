# -*- coding: utf-8 -*-
"""
Created on Thu May  2 15:42:46 2019

@author: vpm6
"""

import pandas as pd
#loc = "D:\python\numpy\issue.csv"
#wb = xlrd.open_workbook(loc)
#sheet = wb.sheet_by_index(0)
#sheet.cell_value(0,0)

d = pd.read_excel('D:\python\numpy\\issue.csv')
print (d)