
# The lines is under 24 after delete those comments

# Number of roots: b * b - 4ac
# If ans > 0, number of roots = 2
# If ans = 0, number of root = 1
# If ans < 0, number of root = 0

# Quadratic Formula:
# ax**2 + bx + c = 0
import cmath
a = float(input("What is the 'a' value? "))
b = float(input("What is the 'b' value? "))
c = float(input("What is the 'c' value? "))

if (b ** 2 - 4 * a * c) > 0:
  print("There are two roots.")
  root = 2
elif (b ** 2 - 4 * a * c) == 0:
  print("There is one root.")
  root = 1
elif (b ** 2 - 4 * a * c) < 0:
  print("There is no root.")
  root = 0
if root == 2 or root == 1:
  solOne = (-b - cmath.sqrt((b ** 2 - 4 * a * c))) / (2 * a)
  solTwo = (-b + cmath.sqrt((b ** 2 - 4 * a * c))) / (2 * a) 

  if solOne == solTwo:
    print(solOne)
  else:
    print(solOne, "and", solTwo)
