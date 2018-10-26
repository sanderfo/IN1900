import numpy as np
import matplotlib.pyplot as plt

x_list = np.linspace(-4,4,101) # jevnt fordelte x-verdier

def function(x,t): # multivariabel funksjon som gir y-verdier etter formelen
    return np.exp(-(x-3*t)**2)*np.sin(3*np.pi*(x-t))

y_list = function(x_list, 0) # ser kun på t=0

plt.plot(x_list,y_list) # plotter
plt.show() # viser i teminalen

"""
Terminal> run plot_wavepacket.py
*Får ut fin graf her*


"""
