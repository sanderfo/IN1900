

def read_file(file):
    infile = open(file, "r")
    line = infile.readline(); infile.readline(); infile.readline()

    pos = [k for k in range(len(line)) if line[k].isupper()]
    result = {}
    line = infile.readline()
    while line[0] == "H":
        spec = line[pos[0]:pos[1]].strip()
        when = line[pos[1]:pos[2]].strip()
        heig = line[pos[2]:pos[3]].strip()
        mass = line[pos[3]:pos[4]].strip()
        bvol = line[pos[4]:].strip()
        result[spec] = dict(when=when, height=heig, mass=mass, brainvol=bvol)
        line = infile.readline()
    return result

humans = read_file("human_evolution.txt")
print(humans)
