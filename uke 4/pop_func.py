from numpy import exp
M = 48 # Setter intervallet til 48
def population(t, k, B, C): #Lager funksjonen
    N = B/(1+C*exp(-k*t))
    return N

for t in range(M+1): # Looper gjennom t-verdiene fra 0 til 48
    print("%2.0f %5.0f" %(t, population(t, 0.2, 50000, 9))) # Printf for å få det fint formattert, med verdiene fra tidligere oppgaver

"""
Terminal > run pop_func
 0  5000
 1  5975
 2  7109
 3  8418
 4  9913
 5 11598
 6 13474
 7 15531
 8 17749
 9 20099
10 22543
11 25035
12 27526
13 29968
14 32315
15 34528
16 36580
17 38451
18 40131
19 41620
20 42924
21 44054
22 45025
23 45852
24 46552
25 47141
26 47635
27 48047
28 48390
29 48674
30 48909
31 49103
32 49263
33 49395
34 49504
35 49593
36 49666
37 49726
38 49776
39 49816
40 49849
41 49877
42 49899
43 49917
44 49932
45 49945
46 49955
47 49963
48 49970
"""
