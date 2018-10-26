#x_list = []
n=10
a=0
b=20

dx = (b-a)/n

x_list = [a+i*dx for i in range(n+1)]

#for i in range(n+1):
#    x_list.append(a+i*dx)



print(x_list)
