from math import factorial
import numpy as np
import matplotlib.pyplot as plt

def S(x, n): # funksjon for å beregne sinus med taylor-polynomer
    sum = 0
    for i in range(n):
        sum = sum + ((-1)**i)*(x**(2*i+1))/factorial(2*i+1) # her får jeg feilmelding ved bruk av +=, så bruker den litt mindre elegante sum = sum +
    return sum

x_array = np.linspace(0,4*np.pi, 101) # jevnt fordelte x-er mellom 0 og 4pi

plt.title("Taylor-tilnærming av sinus-funksjonen")
plt.plot(x_array, S(x_array, 1), label="n=1")
plt.plot(x_array, S(x_array, 2), label="n=2")
plt.plot(x_array, S(x_array, 3), label="n=3")
plt.plot(x_array, S(x_array, 6), label="n=6")
plt.plot(x_array, S(x_array, 12), label="n=12")
plt.plot(x_array, np.sin(x_array), label="sin(x)")
plt.legend()
plt.ylim(-1.1, 1.1) # begrenser til å bare vise y-verdier mellom -1 og 1, som er det interessante å se på her
plt.show()

"""
Terminal> run plot_taylor_sin.py

*fin graf her*

"""
