import sys

t = float(sys.argv[1]) # Første argument er t-verdien, konverterer til flyttall
v0 = float(sys.argv[2]) # Samme for startfart her, andre argument
g = 9.81 # Setter g konstant da den vanligvis ikke endrer seg så mye

y = v0*t - 0.5*g*t**2 #Formelen for høyden over bakken
print(y) # Printer høyden til terminalen

"""
Terminal> run ball_cml 1 9.81
4.905
"""
