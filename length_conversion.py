# converts length in meters to units
inch = 2.54/100
foot = 12*inch
yard = 3*foot
britmile = 1760*yard

meters = 640
inches = meters/inch
feet = meters/foot
yards = meters/yard
miles = meters/britmile

print("%g meters is %g inches, %g feet, %g yards and %g miles" %(meters,inches,feet,yards,miles))

"""
Terminal> run length_conversion.py
640 meters is 25196.9 inches, 2099.74 feet, 699.913 yards and 0.397678 miles

"""
