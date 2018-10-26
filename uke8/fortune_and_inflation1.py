import matplotlib.pyplot as plt
import numpy as np

def fortune(F, p=5, I=2, N=5): # funksjon av formue, rente, inflasjon og antall år
    q = p # q er renten det første året
    x = np.zeros(N+1)
    c = np.zeros(N+1)

    x[0] = F # startverdier
    c[0] = p*q*F/10000
    for n in range(1,N+1): # for loop for å lage følgen
        x[n]=x[n-1]+p/100*x[n-1]-c[n-1]
        c[n] = c[n-1] + I/100*c[n-1]
    return x

plt.plot(fortune(1000000, 2, 2, 10))
plt.show()

"""
Terminal > run fortune_and_inflation1.py
* graf her*
"""
