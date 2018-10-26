import numpy as np

x = np.zeros(15)
x[0] = 1
x[1] = 1
for n in range(2,len(x)):
    x[n] = x[n-1]+x[n-2]

print(x)

"""
Terminal > run fibonacci.py
[  1.   1.   2.   3.   5.   8.  13.  21.  34.  55.  89. 144. 233. 377.
 610.]
"""
