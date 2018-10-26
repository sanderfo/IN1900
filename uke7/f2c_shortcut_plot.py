import matplotlib.pyplot as plt
import numpy as np

F_list = np.linspace(-20, 120, 101) # jevnt fordelte F-verdier mellom -20 og 120

C_list_approx = (F_list-30)/2 # formel for approksimering av C
C_list_exact = (F_list-32)*5/9 # formel for nøyaktig C

plt.plot(F_list, C_list_approx, "r", label="C approximated") # plotter de to grafene
plt.plot(F_list, C_list_exact, "b", label="C exact")
plt.legend()
plt.show()

"""
Terminal > run f2c_shortcut_plot.py
* Får ut fin graf her *

"""
