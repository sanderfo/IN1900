from numpy import exp
# Definerer initialbetingelser:
B = 50000 # Makspopulasjon
k = 0.2 # Sier noe om hvor fort populasjonen vokser
N = 5000 # Startpopulasjon
t = 0 # Tid i timer, starter på 0

C = (B/N - 1)/(exp(-k*t)) # Finner C ved å skrive om uttrykket med hensyn på C

tlist = [] # Lager tomme lister for t og N
Nlist = []
n = 48 # Definerer området vi vil undersøke, i antall timer

for t in range(0, n+1): # Fyller listene ved en for-loop, som starter på 0 og går til og med 48
    N = B/(1+C*exp(-k*t)) # Her er uttrykket skrevet om til å ha hensyn på N, da det er denne verdien vi vil ha
    Nlist.append(N) # Legger til N-verdien i lista
    tlist.append(t) # Legger til t-verdien i lista


for t, N in zip(tlist, Nlist): # Går gjennom listene for å printe ut verdiene i inkrementer
    print("Timer: %2.0f Populasjon: %5.0f" %(t, N))



"""
Terminal > run population_table
Timer:  0 Populasjon:  5000
Timer:  1 Populasjon:  5975
Timer:  2 Populasjon:  7109
Timer:  3 Populasjon:  8418
Timer:  4 Populasjon:  9913
Timer:  5 Populasjon: 11598
Timer:  6 Populasjon: 13474
Timer:  7 Populasjon: 15531
Timer:  8 Populasjon: 17749
Timer:  9 Populasjon: 20099
Timer: 10 Populasjon: 22543
Timer: 11 Populasjon: 25035
Timer: 12 Populasjon: 27526
Timer: 13 Populasjon: 29968
Timer: 14 Populasjon: 32315
Timer: 15 Populasjon: 34528
Timer: 16 Populasjon: 36580
Timer: 17 Populasjon: 38451
Timer: 18 Populasjon: 40131
Timer: 19 Populasjon: 41620
Timer: 20 Populasjon: 42924
Timer: 21 Populasjon: 44054
Timer: 22 Populasjon: 45025
Timer: 23 Populasjon: 45852
Timer: 24 Populasjon: 46552
Timer: 25 Populasjon: 47141
Timer: 26 Populasjon: 47635
Timer: 27 Populasjon: 48047
Timer: 28 Populasjon: 48390
Timer: 29 Populasjon: 48674
Timer: 30 Populasjon: 48909
Timer: 31 Populasjon: 49103
Timer: 32 Populasjon: 49263
Timer: 33 Populasjon: 49395
Timer: 34 Populasjon: 49504
Timer: 35 Populasjon: 49593
Timer: 36 Populasjon: 49666
Timer: 37 Populasjon: 49726
Timer: 38 Populasjon: 49776
Timer: 39 Populasjon: 49816
Timer: 40 Populasjon: 49849
Timer: 41 Populasjon: 49877
Timer: 42 Populasjon: 49899
Timer: 43 Populasjon: 49917
Timer: 44 Populasjon: 49932
Timer: 45 Populasjon: 49945
Timer: 46 Populasjon: 49955
Timer: 47 Populasjon: 49963
Timer: 48 Populasjon: 49970

"""
