'''
Code to animate a cycloid function
LICENSE AGREEMENT
In relation to this Python file:
1. Copyright of this Python file is owned by the author: Nitin Tiwari 
2. This Python code can be freely used and distributed
'''

import matplotlib.pylab as pl
import matplotlib.gridspec as grid
import matplotlib.animation as anim
import numpy as np

# Define the end points
t_0 = 0
t_end = 4*np.pi
dt = 0.01
t = np.arange(t_0,t_end+dt,dt) # Pseudo time array
t2 = np.arange(t_0,t_end+dt,dt) 

param = np.arange(0,2*np.pi,0.01)


R  = 1
x = R*(t - np.sin(t))
y = R*(1 - np.cos(t))

r = np.arange(0,R,0.001)
#exit() # Will stop the code here
#np.linalg
# Circle
#x2 = R*t + R*np.cos(t2)*np.ones Older

x2_temp = R*np.cos(t2)
x2 = np.tile(x2_temp,(len(t),1))

for q in range(len(t)):
    x2[q,:] = x2[q,:] + R*t[q]

y2_temp =R + R*np.sin(t2)
y2 = np.tile(y2_temp,(len(t),1))

x3 =np.tile(r,(len(t),1)) 
y3 =np.tile(r,(len(t),1)) 

for q in range(len(t)):
    x3[q,:] = R*t[q] - r*np.sin(t[q])
    y3[q,:] = R - r*np.cos(t[q])

#pl.plot(x3[-1,:],y3[-1,:])
#pl.show()
#exit()

#pl.plot(x2[-1,:],y2[-1,:])
#pl.show()
#exit()
## Animating the function
frame_amount = len(t) # Frame for each time step
# interval give the amount of time required to go from one frame
# to another in milliseconds

def update_plot(num):

    plane_trajectory.set_data(x[0:num],y[0:num])
    plane_circle.set_data(x2[num,:],y2[num,:])
    Rot_line.set_data(x3[num,:],y3[num,:])

    return plane_trajectory,plane_circle,Rot_line

fig = pl.figure(figsize = (8,8), dpi=120, facecolor = (0.8,0.8,0.8))
# figsize specifies the figure size
# dpi gives resolution
# facecolour defines the colour of the figure in (r,g,b) normalized
gs = grid.GridSpec(1,1)  # Cuts the figure into 4 equal parts

#Subplot 1
ax0 = fig.add_subplot(gs[0,0],facecolor = [0.9,0.9,0.9])
ax0.set_aspect('equal')

# Right now the trajectory is empty but will start get to filled
plane_trajectory,=ax0.plot([],[],'g',linewidth=2) # Line object to animate inside updateplot function
pl.xlim(x[0] - R*2,x[-1] + R*2) # Setting up x axis limit
pl.ylim(y[0],5) # Setting up the y axis limit

plane_circle,=ax0.plot([],[],'r',linewidth=2) # Line object to animate inside updateplot function
pl.xlim(x[0] - R*2,x[-1] + R*2) # Setting up x axis limit
pl.ylim(y[0],5) 

Rot_line, = ax0.plot([],[],'k',linewidth=2)
pl.xlim(x[0] - R*2,x[-1] + R*2) # Setting up x axis limit
pl.ylim(y[0],5) 

#Funcanimation(NameOfThePlot,
#FunctionName(this fucntion is called again and again), 
#FrameAmount, TimeBetweenFrames, Repeat(TorF), Blit(T or F)
#(Redraw the entire thing or not, blit should be true))

cycloid_animation = anim.FuncAnimation(fig, update_plot,
 frames=frame_amount,interval=20,repeat=True,blit=True)
pl.show()

