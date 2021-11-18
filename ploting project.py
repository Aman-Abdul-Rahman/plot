# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:08:32 2021

@author: mx
"""

import matplotlib.pyplot as plt

data=[[0,0,0,0,0,0,0,0,],
      [0,0,0,1,1,0,0,0,],
      [0,0,1,0,0,1,0,0,],
      [0,0,1,0,0,1,0,0,],
      [0,0,1,1,1,1,0,0,],
      [0,0,1,0,0,1,0,0,],
      [0,0,1,0,0,1,0,0,]]
     

plt.imshow(data,cmap='terrain')
plt.show()