import sys

try:
    F = float(sys.argv[1])
    if F < -200:
        raise ValueError
except IndexError:
    print("Please give a command line argument")
    sys.exit(1)
except ValueError:
    print("Command argument must be a number")
    sys.exit(1)



C = 5/9*(F-32)
print ("%4.2f degrees F is %4.2f degrees C" %(F, C))
