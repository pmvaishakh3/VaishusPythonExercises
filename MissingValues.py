# -*- coding: utf-8 -*-
"""
Created on Fri May  3 12:46:29 2019

@author: vpm6
"""

import pandas as pd
import numpy as np

a = pd.DataFrame(np.random.randn(5,3), index = ['a','c','e','f','h'], columns = ['one','two','three'])
a = a.reindex(['a','b','c','d','e','f','g','h'])

print (a)


"""a.Check for Missing Values"""
print (a['one'].isnull())  """To make detecting missing values easier (and across different array dtypes),Pandas provides the isnull() and notnull() functions, which are also methods on Series and DataFrame objects"""
print (a['two'].notnull())"""here not null fun gets printed"""


#
"""b.filling missing datas"""

#1b.replace NaN with  scalar value

#2b.NaN with "0"
"""eg"""
df = pd.DataFrame(np.random.randn(3,3),index=['a','c','e'],columns=['one','two','three'])
df = df.reindex(['a','b','c'])
print (df)
print ("Nan replace with 0:")
print (df.fillna(0))



#3b.Fill NA Forward and Backward
"""eg"""
#pad/fill--->Fill methods Forward
df= pd.DataFrame(np.random.randn(5,3),index=['a','c','e','g','i'],columns=['one','two','three'])
df = df.reindex(['a','b','c','d','e','f','g','h','i'])
print (df.fillna(method='pad'))

#bfill/backfill-->Fill methods Backward +replace NaN with '0'
df= pd.DataFrame(np.random.randn(4,3),index=['a','c','e','g'],columns=['one','two','three'])
df = df.reindex(['a','b','c','d','e','f','g','h','i'])
print (df.fillna(method='bfill'))
print (df.fillna(0))

#4b=Drop Missing Values
"""simply exclude the missing values, then use the dropna function along with the axis argument. By default, axis=0, i.e., along row,which means that if any value within a row is NA then the whole row is excluded."""
df=pd.DataFrame(np.random.randn(2,3),index=['a','b'],columns=['one','two','three'])
df = df.reindex(['a','b','c','d','e','f','g'])
print (df.dropna())

#5b.Replace Missing values

df = pd.DataFrame({'one':[10,2,30,72,00,98,78],'two':[1000,2000,2000,3000,4000,3000,5000]})
print (df.replace({1000:10,4000:90,2000:30}))











