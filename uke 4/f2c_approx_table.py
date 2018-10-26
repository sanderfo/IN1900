# C = -20
# dC = 5

F = 0 # startverdi i Fahrenheit
dF = 10 # inkrementer i F

while F <= 100: # Looper opp til og med F=100
    C=(F-32)/(9/5) # Formel for å finne celsiusgrader
    Ca = (F-30)/2 # Formel for å approksimere celsiusgrader fra F
    print("%3.0f %6.2f %6.2f" %(F, C, Ca)) #Printer et fint formatert table med to desimalplasser
    F = F+dF #Legger til inkrementer

"""
Terminal > run f2c_approx_table
  0 -17.78 -15.00
 10 -12.22 -10.00
 20  -6.67  -5.00
 30  -1.11   0.00
 40   4.44   5.00
 50  10.00  10.00
 60  15.56  15.00
 70  21.11  20.00
 80  26.67  25.00
 90  32.22  30.00
100  37.78  35.00
"""
