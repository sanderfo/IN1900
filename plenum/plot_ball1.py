import numpy as np
import matplotlib.pyplot as plt

v0 = 10
g = 9.81
t_stop = 2*v0/g

t = np.linspace(0, t_stop, 101)

y = v0*t - 0.5*g*t**2

plt.xlabel("time, (s)")
plt.ylabel("height, (m)")
plt.title("height of ball")
plt.plot(t,y)
plt.show()
