# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 20:30:07 2020

@author: ESL328
"""


import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from omegaTRH import OmegaTRH

RHsensor = OmegaTRH('COM6')

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []


# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    rh = RHsensor.getRH()

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(rh)

    # Limit x and y lists to 20 items

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()