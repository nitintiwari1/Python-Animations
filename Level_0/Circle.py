'''
LICENSE AGREEMENT
In relation to this Python file:
1. Copyright of this Python file is owned by the author: Nitin Tiwari 
2. This Python code can be freely used and distributed

# This code plots a circle
'''
import matplotlib.pyplot as plt
import numpy as np

n = 1000
t0=0 # [hrs]
t_end=2*np.pi # [hrs]
dt=0.005 # [hrs]
# Create the array for

t=np.arange(t0,t_end+dt,dt)

x = np.sin(t)
y = np.cos(t)

plt.plot(x,y,'r')
xl
plt.show()
