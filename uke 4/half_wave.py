from math import sin
from math import pi

def half_wave(x): # Definerer funksjonen
    if sin(x) > 0: # Regner ut sin(x) og sjekker om det er større enn 0
        return sin(x) # Funksjonen skal gi sin(x) dersom sin(x) er positiv
    else:
        return 0 # Skal gi null for alle negative verdier og 0

print(half_wave(pi/2)) # Printer ut et par verdier
print(half_wave(4))

def test_half_wave(): # Testfunksjonen, sjekker noen kjente verdier
    input = [pi/2, 4] # Liste over x-verdier
    expected = [1, 0] # Liste over forventede verdier av half_wave
    computed = [half_wave(pi/2), half_wave(4)] # Liste over utregnede verdier av half_wave
    assert expected == computed, "Ikke likhet" # Gir feilmelding dersom utregning ikke er likt forventede verdier

test_half_wave() # Caller testfunksjonen

"""
Terminal > run half_wave
1.0
0
"""
