t = []; y = [] # Lager tomme lister
g = 9.81 # Tyngdeakselerasjon
n = 10 # Hvor mange intervaller vi deler tiden i
v0 = 5 # Startfart

t_stop = 2*v0/g # finner verdien for t når y = 0
dt = t_stop/n # Her deler jeg opp grafen i snitt med like mellomrom

for i in range(n+1): # Her fyller jeg listene med verdiene
    time = i * dt
    t.append(time)
    height = v0*time-0.5*g*time**2
    y.append(height)

print("Skriver ut kolonnene:")
ty1 = [t, y] # lager liste med listene t og y
for t, y in zip(ty1[0], ty1[1]): # Looper gjennom listene og printer ut verdiene i et fint format
    print("%5.2f %5.2f" %(t, y))

ty2 = [] # Lager en tom liste for radene
for t,y in zip(ty1[0], ty1[1]): # Looper gjennom verdiene og legger de til i listen
    ty2.append([t, y])

print("Skriver ut radene:")
for i in range(len(ty2)): # Looper gjennom ty2 for å printe ut radene
    print("%5.2f %5.2f" %(ty2[i][0], ty2[i][1]))


"""
Har samarbeidet med Christopher Pavelich på denne, kan være noen likheter

Terminal > run ball_table3
Skriver ut kolonnene:
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
Skriver ut radene:
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
