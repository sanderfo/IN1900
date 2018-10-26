import numpy as np
import matplotlib.pyplot as plt

T = 2*np.pi
t_list = np.linspace(0,2*np.pi, 1001) # Jevnt fordelte t-verdier mellom 0 og 2pi

def S(t,n): # Funksjonen for tilnærming
    sum = 0
    for i in range(1,n+1):
        sum += 1/(2*i-1)*np.sin((2*(2*i-1)*np.pi*t)/T)
    return (4/np.pi)*sum

def f(t):
    y_list = np.piecewise(t,[ t < T/2, t==T/2, t > T/2], [1,0,-1] )
    #piecewise-funksjonen til numpy, funker fjell. Tar t-verdiene, boolske sjekker og funksjonsverdien
    return y_list





# plotting
plt.plot(t_list, S(t_list, 1), "r", label="n = 1")
plt.plot(t_list, S(t_list, 3), "b", label="n = 3")
plt.plot(t_list, S(t_list, 20), "g", label="n = 20")
plt.plot(t_list, S(t_list, 200), "y", label="n = 200")
plt.plot(t_list, f(t_list), label="f(t)")
plt.legend()
plt.show()

"""
Terminal> run sinesum1_plot.py
*Fine plots her*
"""
