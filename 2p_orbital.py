#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from matplotlib import pyplot as plt


# In[3]:


a_bohr = 1


# In[5]:


#complete wave function
a = -4*a_bohr
b = 4*a_bohr
x = np.random.rand(7000)*(b-a) + a
y = np.random.rand(7000)*(b-a) + a
z = np.random.rand(7000)*(b-a) + a

def func_cwf_cartesian(x,y,z):
  a_bohr = 1
  awf_2p = (1/2)*np.sqrt(3/np.pi)*np.cos(np.arctan(y/x))
  rwf_2p = np.sqrt(1/24)*np.power((1/a_bohr), (5/2)) * np.sqrt(np.square(x) + np.square(y) + np.square(z)) * np.exp(-(np.sqrt(np.square(x) + np.square(y) + np.square(z))/(2*a_bohr)))
  cwf_2p = rwf_2p*awf_2p
  return cwf_2p


# In[6]:


#3d plotting
from mpl_toolkits import mplot3d
#X,Y,Z = np.meshgrid(x,y,z)
C = func_cwf_cartesian(x, y, z)

mask = C>0.06
C1 = C*mask
#print(C)
fig = plt.figure(figsize = (12,10))
ax = plt.axes(projection = "3d")
img = ax.scatter(x, y, z, c = C1, cmap= 'Greens')
fig.colorbar(img)
#ax.set_title("Density Plotting")

plt.show()

# In[ ]:




