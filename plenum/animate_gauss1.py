import numpy as np
import matplotlib.pyplot as plt

def f(x,m,s):
    return (1/(np.sqrt(2*np.pi)*s))*np.exp(-0.5*((x-m)/s)**2)

m = 0
s_start = 2
s_stop = 0.2

s_values = np.linspace(s_start, s_stop, 20)

x = np.linspace(-3*s_start, 3*s_start, 100)

f_max = f(m,m,s_stop)
plt.axis([-3*s_start, 3*s_start, 0, f_max])

y = f(x,m,s_start)

lines = plt.plot(x,y)

def next_frame(frame):
    y = f(x, m , frame)
    lines[0].set_ydata()

counter = 0
for s in s_values:
    y = f(x,m,s)
    lines[0].set_ydata(y)
    plt.draw()
    plt.savefig("gauss_%04d.png" %(counter))
    counter += 1
