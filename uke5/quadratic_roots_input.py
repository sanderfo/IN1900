import math
import cmath # Importer math og cmath for å ta med komplekse løsninger

a = float(input("a=? \n")) # spør om input
b = float(input("b=? \n"))
c = float(input("c=? \n"))

if b**2-4*a*c >= 0: # Sjekker om vi får positivt under rottegnet før jeg definerer løsningene
    x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
else: # Finner komplekse løsninger dersom vi får negativt under rottegnet
    x1 = (-b+cmath.sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b-cmath.sqrt(b**2-4*a*c))/(2*a)

print(x1, x2) # Printer løsninger

"""
Terminal > run quadratic_roots_input

a=?
1

b=?
2

c=?
6
(-1+2.23606797749979j) (-1-2.23606797749979j)
