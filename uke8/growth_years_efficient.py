
x0 = 100                      # initial amount
p = 5                         # interest rate
N = 4                         # number of years

# Compute solution
xn = x0
count = 0
outfile = open("out.txt", "w") # åpner ny txt-fil
while count < N+1:
    xn1 = xn + (p/100.0)*xn #formelen for x(n+1)
    outfile.write("year: %g amount: %g \n" %(count, xn)) #skriver til fil
    xn = xn1
    count += 1 #teller i while-løkka, er også antall år

outfile.write("year: %g amount: %g \n" %(count, xn1)) # skriver ut siste verdi x(n+1).
# Kunne også bare økt N med en for å få ut siste verdi, men da gjør vi en utregning mer
# enn vi trenger
print(xn)
outfile.close()

"""
Terminal> run growth_years_efficient.py
127.62815624999999
