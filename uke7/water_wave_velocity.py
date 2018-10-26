import numpy as np
import matplotlib.pyplot as plt

def c(Lambda): # Funksjon fra formel
    g = 9.81
    rho = 1000
    h = 50
    s = 7.9e-2
    faktor1 = g*Lambda/(2*np.pi)
    faktor2 = (1+s*(4*np.pi**2)/(rho*g*Lambda**2))
    faktor3 = np.tanh(2*np.pi*h/Lambda)
    return np.sqrt(faktor1*faktor2*faktor3)

small_L = np.linspace(0.001,0.1, 101) # Velger x-verdier, bølgelengder vi skal se på
large_L = np.linspace(1,2000, 101)

plt.plot(small_L, c(small_L), "r")
plt.savefig("small_L") # Lagrer til fil
plt.figure() # Nullstiller plot med figure
plt.plot(large_L, c(large_L), "b")
plt.savefig("large_L") # Lagrer til fil

"""
Terminal > run water_wave_velocity.py
*Fine figurer her*

De blir også lagret til fil.

"""
