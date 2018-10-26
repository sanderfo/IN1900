from math import pi

phi = 1.2 # density of air measured in kg*m^(-3)
g = 9.81 # acceleration of gravity in m/s^2
m = 0.43 # mass of the football in kg
Fg = m*g # force of gravity in Newtons / kgm/s^2
a = 0.11 # radius of the ball in meters
A = pi*a**2 # area of the ball in m^2
Cd = 0.4 # drag coefficient
Vhard = 120/3.6 # Velocity in m/s
Vsoft = 30/3.6 # Velocity in m/s
V = Vhard

Fd = 0.5*Cd*phi*A*V**2 # Force of drag

print("For a hard kick, the force of gravity \
on the ball is %.1f \
Newtons and the drag force is %.1f Newtons." %(Fg,Fd))

print("The ratio of the drag force and the gravity force is %.2f" %(Fd/Fg))

V = Vsoft # Changing the variable V to the soft velocity
Fd = 0.5*Cd*phi*A*V**2 # Changing the variable Fd to reflect the change in velocity

print("For a soft kick, the force of gravity on the ball is \
%.1f and the drag force is %.1f" %(Fg,Fd))
print("The ratio of the drag force and the gravity force is %.2f" %(Fd/Fg))

"""
Terminal > run kick.py
For a hard kick, the force of gravity on the ball is 4.2 Newtons and the drag force is 10.1 Newtons.
The ratio of the drag force and the gravity force is 2.40
For a soft kick, the force of gravity on the ball is 4.2 and the drag force is 0.6
The ratio of the drag force and the gravity force is 0.15
"""
