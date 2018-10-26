import numpy as np
import matplotlib.pyplot as plt

k1 = 5.01e-7; k2 = 4.79e-11 # konstanter

ph = np.linspace(4,12,101) # jevnt fordelte ph-verdier
h = 10**(-ph) # fant denne likheten på wikipedia

co2 = (h**2)/((h**2)+k1*h+k1*k2) # formler
hco3 = k1*h/(h**2+k1*h+k1*k2)
co32 = k1*k2/(h**2+k1*h+k1*k2)

plt.plot(ph, co2, label="co2") #plotting
plt.plot(ph, hco3, label="hco3")
plt.plot(ph, co32, label="co32")
plt.legend()
plt.show()
"""
Terminal > run bjerrum_plot.py
*graf her*
"""

# b)
# co2-grafen krysser hco3-grafen når h = k1
# det gir k1 = 10**(-ph)
# log10(k1) = -ph, ph = -log10(k1)

print("co2-grafen krysser hco3-grafen når ph =", -np.log10(k1))

# på samme måte krysser hco3 co32 når ph = -log10(k2)
print("hco3-grafen krysser co32-grafen når ph=",-np.log10(k2))
