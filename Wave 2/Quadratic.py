
# I don't want to do a while loop for this
# This one improves the readability of the answer
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

print("-----------------------------------")
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
  solOne = str(solOne)
  solTwo = str(solTwo)
  solOne = solOne.replace("j", "")
  solTwo = solTwo.replace("j", "")

  if solOne == solTwo:
    print("X =", solOne.replace("+", " + "))
  else:
    print("X =", solOne.replace("+", " + "), "and X =", solTwo.replace("+", " + "))
