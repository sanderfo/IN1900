import numpy as np
import matplotlib.pyplot as plt
import sys

g = 9.81
y0, theta, v0 = [float(p) for p in sys.argv[1:]]

# Solve a*x**2 + b*x + c
a = -(1/(2*v0**2))*(g/np.cos(theta)**2)
b = np.tan(theta)
c = y0

x1 = (-b + np.sqrt(b**2-4*a*c))/(2*a)
x2 = (-b - np.sqrt(b**2-4*a*c))/(2*a)

x_max = max(x1, x2)

x = np.linspace(0, x_max, 101)

y = a*x**2+b*x+c

plt.plot(x,y)
plt.show()
