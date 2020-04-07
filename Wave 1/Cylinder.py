
# input radius and height, calculate for volume of the cylinder.
# I also create a while loop for sake of the completion of the program.

import math
print("Welcome to the Cylinder Volume Calculator!")
print("-----------------------------------")

while True:
  height = float(input("Please input the height of the CYLINDER: "))
  rad = float(input("Please input the base radius the CYLINDER: "))

  print("-----------------------------------")
  print("The HEIGHT is", height)
  print("The RADIUS is", rad)

  print("-----------------------------------")
  print("Confirm?")
  print("Yes = Y")
  print("No = N")
  answer = input("Your Answer: ")

  if answer == "Y":
    print("-----------------------------------")
    circle = rad * rad * math.pi
    area = circle * height
    
    print("The Volume of the CYLINDER is:", round(area, 1))
    again = input("Again? ")
    
    if again == "Y":
      print("-----------------------------------")
      
    else:
      break
      
  elif answer == "N":
    print("-----------------------------------")
    
  else:
    print("Invalid answer.")
    print("-----------------------------------")
