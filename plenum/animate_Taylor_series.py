import numpy as np
from math import factorial
import matplotlib.pyplot as plt

def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact):

    x = np.linspace(xmin, xmax, n)
    s = np.zeros(n)

    plt.axis([xmin, xmax, ymin, ymax])

    plt.plot(x, exact(x))

    lines = plt.plot(x, s)

    for k in range(M, N+1):
        s = s + fk(x, k)
        lines[0].set_ydata(s)
        plt.draw()
        plt.pause(0.4)

def fk_sin(x, k):
    return (-1)**k*x**(2*k+1)/factorial(2*k+1)

animate_series(fk_sin, 0, 40, 0, 13*np.pi, -2, 2, 200, np.sin)
