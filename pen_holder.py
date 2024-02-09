#Pen holder to fix on a table
# %%
from build123d import *
from ocp_vscode import *

# Function to fillet all edges of a shape
def fillet_all_edges(shape, radius):
    return fillet(shape.edges(), radius=radius)

width = 30
height = 30
length = 30
hole_diameter_up = 15
hole_diameter_down = 14.5
hole_lenght = 19.6
hole_height = height -hole_lenght
tap_diameter = 4.5
filet_radius = 1


r = extrude(Rectangle(width, length), height)
tap = Pos(Z =hole_height/2)* Cylinder(tap_diameter/2, hole_height) 
c1 = Pos(Z=hole_height)*Circle(hole_diameter_down/2)
c2 = Pos(Z=height)*Circle(hole_diameter_up/2)
h = loft([c1, c2])
p = fillet_all_edges(r-h-tap, radius=filet_radius)

show(p)
# %%
