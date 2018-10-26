

def area(vertices):
    x1,y1 = vertices[1]
    x2,y2 = vertices[2]
    x3,y3 = vertices[3]
    A = 0.5 * abs(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1)
    return A

vertices = {1: (0,0), 2: (1,0), 3: (0,2)}
print(area(vertices))
