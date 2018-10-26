import numpy as np
import matplotlib.pyplot as plt
import sys

v0_list = [float(v) for v in sys.argv[1:]]

g = 9.81

v0_max = max(v0_list)
t_max = 2*v0_max/g

y_max = 0

for v0 in v0_list:
    t_stop = 2*v0/g
    t = np.linspace(0, t_stop, 101)
    y = v0*t - 0.5*g*t**2
    if max(y) > y_max:
        y_max = max(y)
    plt.plot(t,y)


plt.xlabel("time, (s)")
plt.ylabel("height, (m)")
plt.title("height of ball")
plt.axis([0,t_max, 0, y_max*1.1])
plt.grid()
plt.show()
