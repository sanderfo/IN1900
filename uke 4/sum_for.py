"""
Dette er originalkoden:
s = 0; M = 3
for i in range(M):
    s += 1/2*k**2
print(s)

"""
s = 0; k = 1; M = 100 # Summen starter naturlig nok på null, setter k=1 og M=100

for k in range(1, M+1): # Her har jeg byttet ut i med k, og satt range fra 1 til M+1 som i python gir fra 1 til M
    s += 1/((2*k)**2) # Satt inn paranteser i uttrykket for å være sikker
print(s)

s2 = 0; k2 = 1
while k2 < M+1: # Skrevet om til while-løkke
    s2 += 1/((2*k2)**2)
    k2 += 1
print(s2)

if s == s2: # Legger inn en if-test for å sjekke om svarene er like (kunne også lagt inn en toleranse her på grunn av avrundingsproblemer, men er ikke nødvendig i dette tilfellet)
    print("Svarene er like")
else:
    print("Svarene er ikke like")

"""
Terminal > run sum_for
0.40874597504622306
0.40874597504622306
Svarene er like
"""
