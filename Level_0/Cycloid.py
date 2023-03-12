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

# Define the 
t_0 = 0
t_end = 4*np.pi
dt = 0.01
t = np.arange(t_0,t_end+dt,dt) # Pseudo time array

R  = 1
x = R*(t - np.sin(t))
y = R*(1 - np.cos(t))


#exit() # Will stop the code here

## Animating the function
frame_amount = len(t) # Frame for each time step
# interval give the amount of time required to go from one frame
# to another in milliseconds

def update_plot(num):

    plane_trajectory.set_data(x[0:num],y[0:num])

    return plane_trajectory,

fig = pl.figure(figsize = (16, 9), dpi=120, facecolor = (0.8,0.8,0.8))
# figsize specifies the figure size
# dpi gives resolution
# facecolour defines the colour of the figure in (r,g,b) normalized
gs = grid.GridSpec(1,1)  # Cuts the figure into 4 equal parts

#Subplot 1
ax0 = fig.add_subplot(gs[0,0],facecolor = [0.9,0.9,0.9])

# Right now the trajectory is empty but will start get to filled
plane_trajectory,=ax0.plot([],[],'g',linewidth=2) # Line object to animate inside updateplot function
pl.xlim(x[0],x[-1]) # Setting up x axis limit
pl.ylim(y[0],5) # Setting up the y axis limit

#Funcanimation(NameOfThePlot,
#FunctionName(this fucntion is called again and again), 
#FrameAmount, TimeBetweenFrames, Repeat(TorF), Blit(T or F)
#(Redraw the entire thing or not, blit should be true))

cycloid_animation = anim.FuncAnimation(fig, update_plot,
 frames=frame_amount,interval=20,repeat=True,blit=True)
pl.show()
