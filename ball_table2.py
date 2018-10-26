t = []; y = [] # lager noen tomme lister
g = 9.81 # tyngdeaksellerasjon
n = 10
v0 = 5 # startfart

t_stop = 2*v0/g
dt = t_stop/n

for i in range(n+1):
    time = i * dt
    t.append(time)
    height = v0*time-0.5*g*time**2
    y.append(height)

for e, e1 in zip(t, y):
    print("%5.2f %5.2f" %(e,e1))

"""
Terminal > run ball_table2
 0.00  0.00
 0.10  0.46
 0.20  0.82
 0.31  1.07
 0.41  1.22
 0.51  1.27
 0.61  1.22
 0.71  1.07
 0.82  0.82
 0.92  0.46
 1.02  0.00
"""
