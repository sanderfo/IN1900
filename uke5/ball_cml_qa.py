import sys

g = 9.81 # Setter g konstant da den vanligvis ikke endrer seg så mye
try:
    t = float(sys.argv[1]) # Første argument er t-verdien, konverterer til flyttall

except IndexError:
    t = float(input("t=? \n")) # Om indexerror på første argument spør den om verdi for t

try:
    v0 = float(sys.argv[2]) # Samme for startfart her, andre argument
except IndexError:
    v0 = float(input("v0=? \n")) # Om indexerror på andre argument spør den om verdi for v0

y = v0*t - 0.5*g*t**2 #Formelen for høyden over bakken
print(y) # Printer høyden til terminalen

"""
Terminal> run ball_cml_qa

t=?
4

v0=?
6
-54.480000000000004

Terminal> run ball_cml_qa 3

v0=?
4
-32.145

Terminal> run ball_cml_qa 3 10
-14.145000000000003
"""
