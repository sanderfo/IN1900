from math import e
# Definerer initialbetingelser:
B = 50000
k = 0.2
N = 5000
t = 0

C = (B/N - 1)/(e**(-k*t)) # Finner C ved å skrive om uttrykket med hensyn på C

print("C=%g" %(C)) # Printer C for syns skyld

t = 24 # Ser på hva som skjer etter 24 timer
N = B/(1+C*e**(-k*t)) # Omdefinerer N til et funksjonsuttrykk
print("Etter %g timer er populasjonen på %g." %(t,N)) # Printer populasjonen etter 24 timer

"""
Terminal >run population.py
C=9
Etter 24 timer er populasjonen på 46552.
"""
