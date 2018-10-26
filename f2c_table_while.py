# C = -20
# dC = 5

F = 0
dF = 10

while F <= 100:
    #F=9/5*C+32
    C=(F-32)/(9/5)
    print(F, C)
    F = F+dF
