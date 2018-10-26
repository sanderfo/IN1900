import numpy as np

w = np.linspace(0,3,31)

"""
Slicing of lists and arrays:
w[start:stop:step], where start, stop, step and the last : are optional 
"""

print("w[:] \n", w[:])
print("w[:-2] \n", w[:-2])
print("w[::5] \n", w[::5])
print("w[2:-2:6] \n", w[2:-2:6])
