import math #importerer math for å finne kvadratrøtter
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
    print(x1, x2) # Printer røttene
else: # Dersom vi får negativt under rottegnet printer jeg melding om det
    print("Her får vi ingen reelle løsninger")

"""
Terminal> run quadratic_roots_error2 1 2 5
Her får vi ingen reelle løsninger

Terminal> run quadratic_roots_error2 1 2 1
-1.0 -1.0
"""
