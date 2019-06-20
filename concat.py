# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:09:08 2019

@author: vpm6
"""
""" data wrangling egs"""

import pandas as pd
import numpy as np

one = pd.DataFrame(np.random.randn(5,4))
two = pd.DataFrame(np.random.randn(3,7))
c = pd.concat([one,two])
print (c)

