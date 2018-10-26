import numpy as np
import matplotlib.pyplot as plt
import sys

v0_list = [float(v) for v in sys.argv[1:]]

g = 9.81

for v0 in v0_list:
    t_stop = 2*v0/g
    t = np.linspace(0, t_stop, 101)
    y = v0*t - 0.5*g*t**2
    plt.plot(t,y)
    

plt.xlabel("time, (s)")
plt.ylabel("height, (m)")
plt.title("height of ball")

plt.show()
