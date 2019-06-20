# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:27:38 2019

@author: vpm6
"""

import numpy as np
import pandas as pd

#dataoperations
#a = np.array([[2,3,4],[5,5,6]])
#print (a)
#print(a[1])
#print(a[0][2])
#print (a[1][2])
#b = np.array([3,4,5],[3,2,5])
#c=a+b
#print(c)

a=np.array([1,2,3,4,5],dtype =complex)
print(a)

a=np.array([1,2,3,4,5],ndmin = 2)
print(a)

#Data Operations in Pandas

#1.series
"""Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.). 
The axis labels are collectively called index.

A pandas Series can be created using the following constructor −
pandas.Series( data, index, dtype, copy)"""


#eg:
data = np.array([1,2,3,4,5])
s=pd.Series(data)
print(s)


#2.dataframe
"""A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns. 
A pandas DataFrame can be created using the following constructor −
pandas.DataFrame( data, index, columns, dtype, copy)"""

#eg:
data={'Name':['Tom','Jack','Steve','Ricky'],'Age':[28,34,22,30]}
df= pd.DataFrame(data,index=['rank 1','rank 2','rank 3','rank 4'])
print (df)

#3.Panel
"""A panel is a 3D container of data. The term Panel data is derived from econometrics and is partially responsible 
for the name pandas − pan(el)-da(ta)-s.

A Panel can be created using the following constructor −
pandas.Panel(data, items, major_axis, minor_axis, dtype, copy)"""

#eg:creatig a empty panel
data={'Item 1':pd.DataFrame(np.random.randn(4,3)),'Item2': pd.DataFrame(np.random.randn(5,6))}
p=pd.Panel(data)
print (p)


#numpy:
#NumPy is a Python package which stands for 'Numerical Python'. 
#It is a library consisting of multidimensional array objects and a collection of routines for processing of array.

#Using NumPy, a developer can perform the following operations −
#1.Mathematical and logical operations on arrays.
#2.Fourier transforms and routines for shape manipulation.
#3.Operations related to linear algebra. NumPy has in-built functions for linear algebra and random number generation.











