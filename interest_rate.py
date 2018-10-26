A = 1000
p = 5
n = 3

A1 = A*(1+p/100)**n

print("With an initial amount of %g euros \
and an interest rate of %g percent, the amount\
 will have grown to %g euros after %g years." %(A,p,A1,n))

"""
terminal > run interest_rate.py
With an initial amount of 1000 euros and an interest rate of 5 percent, the amount will have grown to 1157.63 euros after 3 years.
"""
