s = 0; k = 1; M = 100
while k < M+1:
    s += 1/k
    k += 1
print(s)

"""
Feilene var følgende:
k < M og ikke k < M+1
Det manglet økning i k, så la til k+=1
Bare 2 feil utover at det opprinnelig var skrevet for python 2 i oppgaven,
men dette programmet gir korrekt svar

Terminal > run sum_while
5.187377517639621


"""
