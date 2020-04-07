
import math
print("Welcome to the Cylinder Volume Calculator!")
print("-----------------------------------")

height = float(input("Please input the height of the CYLINDER: "))
rad = float(input("Please input the base radius the CYLINDER: "))
print("-----------------------------------")

circle = rad * rad * math.pi
area = circle * height  
print("The Volume of the CYLINDER is:", round(area, 1))
