g = 9.81
n = 10
v0 = 5

t_stop = 2*v0/g
dt = t_stop/n

for i in range(n+1):
    t = i * dt
    y = v0*t-0.5*g*t**2
    print("%2.2f %2.2f" %(t,y))

eps = 1e-10

t = 0

while t < t_stop + eps:
    y = v0*t-0.5*g*t**2
    print(t,y)
    t += dt
