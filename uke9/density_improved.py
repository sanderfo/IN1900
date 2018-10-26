# a)
def read_densities(filename):
    infile = open(filename, "r")
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])
        substancelist = words[:-1] # liste over ordene i navnet/nøkkelen
        substance = ''.join(str(e)+" " for e in substancelist) # setter sammen ordene til en string
        substance = substance.strip() # fjerner whitespace før og etter


        densities[substance] = density
    infile.close()
    return densities
densities = read_densities("densities.dat")
print(densities)


# b)

def read_dens(file):
    infile = open(file, "r")
    densities = {}
    for line in infile:
        substance = line[:12]
        density = float(line[12:])
        substance = substance.strip()
        densities[substance] = density
    infile.close()
    return densities

print(read_dens("densities.dat"))

# c)

def test_densities():
    success = read_densities("densities.dat") == read_dens("densities.dat")
    assert success, "Test feilet"

test_densities()

"""
Terminal> run density_improved.py
{'air': 0.0012, 'gasoline': 0.67, 'ice': 0.9, 'pure water': 1.0, 'seawater': 1.025, 'human body': 1.03, 'limestone': 2.6, 'granite': 2.7, 'iron': 7.8, 'silver': 10.5, 'mercury': 13.6, 'gold': 18.9, 'platinium': 21.4, 'Earth mean': 5.52, 'Earth core': 13.0, 'Moon': 3.3, 'Sun mean': 1.4, 'Sun core': 160.0, 'proton': 230000000000000.0}
{'air': 0.0012, 'gasoline': 0.67, 'ice': 0.9, 'pure water': 1.0, 'seawater': 1.025, 'human body': 1.03, 'limestone': 2.6, 'granite': 2.7, 'iron': 7.8, 'silver': 10.5, 'mercury': 13.6, 'gold': 18.9, 'platinium': 21.4, 'Earth mean': 5.52, 'Earth core': 13.0, 'Moon': 3.3, 'Sun mean': 1.4, 'Sun core': 160.0, 'proton': 230000000000000.0}

"""
