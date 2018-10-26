import math #importerer moduler for å finne kvadratrøtter
import cmath # tar hensyn til komplekse løsninger
import sys

try:
    a = float(sys.argv[1]) #Prøver å lese av argument fra terminal
except IndexError:
    a = float(input("a=? \n")) # Spør om input dersom det ikke er lagt inn noe
try:
    b = float(sys.argv[2]) # Gjør det samme for b og c
except IndexError:
    b = float(input("b=? \n"))
try:
    c = float(sys.argv[3])
except IndexError:
    c = float(input("c=? \n"))

if b**2-4*a*c >= 0: # Sjekker om vi får positivt tall eller 0 under rot-tegnet
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
else: #Bruker cmath dersom det er negativt slik at vi får med komplekse løsninger
    x1 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)

print(x1, x2) # Printer røttene

"""
> run quadratic_roots_error

a=?
2

b=?
1

c=?
-5
1.3507810593582121 -1.8507810593582121

> run quadratic_roots_error 1 3 4
(-1.5+1.3228756555322954j) (-1.5-1.3228756555322954j)

> run quadratic_roots_error 1 3

c=?
-5
1.1925824035672519 -4.192582403567252
