# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:07:11 2019

@author: vpm6
"""

import json

x = '{"name":john","city":"newyork"}'
y = json.loads(x)
print (y["age"])