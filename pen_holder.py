#Pen holder to fix on a table
# %%
from build123d import *
from ocp_vscode import *

# Function to fillet all edges of a shape
def fillet_all_edges(shape, radius):
    return fillet(shape.edges(), radius=radius)

width = 30
height = 25
length = 30
hole_diameter_up = 15
hole_diameter_down = 14.5
hole_lenght = 19.6
hole_height = height -hole_lenght
tap_diameter = 4.5
wall_tickness = 2
filet_radius = 0.5


b = Pos(Z=height/2)*Box(length, width, height)
tap = Pos(Z =hole_height/2)* Cylinder(tap_diameter/2, hole_height) 
c1 = Pos(Z=hole_height)*Circle(hole_diameter_down/2)
c2 = Pos(Z=height)*Circle(hole_diameter_up/2)
h = loft([c1, c2])
b = b-h-tap
#bottomf = b.faces().sort_by().first
#b= offset(b, amount=-wall_tickness, openings=bottomf)

show(b)


b.export_stl("pen_holderV2.stl")


"""
Pen holder to ease the robot grip on the pen, 
we use a 8 side polygon rather than a square to create a more forgiving grip
Indeed it as 4 set of parallel faces to grip on, rather than 2 for a square
"""
# %%
from build123d import *
from ocp_vscode import *

hole_radius = 7.6
polygon_side_count = 6
height = 20
hole_height = 20
polygon_radius = 12

# Function to fillet all edges of a shape
def fillet_all_edges(shape, radius):
    return fillet(shape.edges(), radius=radius)


p = extrude(RegularPolygon(radius=polygon_radius, side_count=8), height)
h = Pos(Z=height-hole_height)*extrude(Circle(hole_radius), hole_height)
p = p-h
show(p)
p.export_stl("pen_holder_robot_side.stl")
# %%
