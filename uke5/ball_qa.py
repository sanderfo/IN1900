t = float(input("t=? \n")) # Spør om t-verdien, konverterer til flyttall
v0 = float(input("v0=? \n")) # Samme for startfart her
g = 9.81 # Setter g konstant da den vanligvis ikke endrer seg så mye

y = v0*t - 0.5*g*t**2 #Formelen for høyden over bakken
print(y) # Printer høyden til terminalen

"""
Terminal> run ball_qa

t=?
1

v0=?
5
0.09499999999999975
"""
