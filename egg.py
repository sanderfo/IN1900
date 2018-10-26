from math import pi, log

M = 67
p = 1.038
c = 3.7
K = 5.4*10**(-3)
Tw = 100
Ty = 70
T0 = 4

t1 = (M**(2/3)*c*p**(1/3))/(K*pi**2*(4*pi/3)**(2/3))
t2 = log(0.76*((T0-Tw)/(Ty-Tw)))

t = t1*t2
minutes = t/60

print("The perfect cooking time for an egg with temperature %g celsius is %g minutes or %g seconds." %(T0,minutes,t))
