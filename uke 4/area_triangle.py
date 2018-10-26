from numpy import abs
c1 = [0,0]; c2 = [1,0]; c3 = [0,2] # Definerer koordinatene til trekanten som lister
vertices = [c1, c2, c3] # Definerer vertices som liste av koordinater

def triangle_area(vertices): # Funksjonen som regner ut arealet av trekanten

    x1 = vertices[0][0]; x2 = vertices[1][0]; x3 = vertices[2][0] # Definerer x og y-koordinatene for hver av punktene
    y1 = vertices[0][1]; y2 = vertices[1][1]; y3 = vertices[2][1]

    A = 0.5*abs(x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1) # formelen fra boka, skrevet om slik at jeg kan putte inn koordinater øverst
    return A

print(triangle_area(vertices)) # Printer arealet

"""
Verify the area of a triangle with vertex coordinates
(0,0), (1,0), and (0,2).
"""
def test_triangle_area(): # Testfunksjonen
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = "computed area=%g != %g (expected)" %(computed, expected)
    assert success, msg

test_triangle_area() # Caller testfunksjonen

"""
Terminal > run area_triangle
1.0
"""
