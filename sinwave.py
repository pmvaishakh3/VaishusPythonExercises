# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:52:46 2019

@author: vpm6
"""


"""data wranling egs"""

import numpy as np
import matplotlib.pyplot as plt

#sin Wave
x = np.arange(0,10*np.pi,0.10)
y = np.sin(x)
plt.title("sin wave form")

plt.plot(x,y)
plt.show()

#cos Wave
x = np.arange(0,5*np.pi, 0.99)
y = np.cos(x)
plt.title("cos wave form")

plt.plot(x,y)
plt.show()

#tan Wave
x=np.arange(0,5*np.pi,0.55)
y=np.tan(x)
plt.title("tan wave 2")

plt.plot(x,y)
plt.show()