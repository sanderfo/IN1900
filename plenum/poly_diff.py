

# coef: {0: 0.5, 2: 4.2, 100: 8.0}
# svarer til p(x) = 0.5 + 4.2x^2 + 8x^100
# den deriverte er 2*4.2*x + 100*8x^99
# -> coef = {1: 8.4, 99:800.0}
# altså skal vi gå fra {0: 0.5, 2: 4.2, 100: 8.0} til {1: 8.4, 99:800.0}

def diff(coef):
    if 0 in coef:
        del coef[0]
    dcoef = {}
    for k in coef:
        dcoef[k-1] = k*coef[k]
    return dcoef

c = {0:1, 1:0.5, 2:4, 100:1.8}
print(c)
print(diff(c))
print(diff(diff(c)))
