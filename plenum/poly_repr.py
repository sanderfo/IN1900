
# Store p(x) = -0.5 + 2x^100
# list:
coefList = [0]*101
coefList[0] = -0.5
coefList[100] = 2
coefDict = {0: -0.5, 100: 2}

print(coefList)
print(coefDict)

# Evaluate p(x) in x=1.05

x= 1.05
px = sum(coefList[i]*x**i for i in range(len(coefList)))
print(px)
