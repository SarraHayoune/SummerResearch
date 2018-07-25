
# coding: utf-8

# In[ ]:


import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('bhfile.dat')
Time= files[:,2]
BHDistance= files[:,5]

plt.plot(Time, BHDistance)
plt.ylabel('BH Distance')
plt.xlabel('Time')
plt.show()


