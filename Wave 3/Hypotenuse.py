# Hypotenuse

# h ** 2 = x ** 2 + y ** 2

def hyp(x, y):
  import cmath
  square = x ** 2 + y ** 2
  normal = cmath.sqrt(square)
  print("The hypotenuse of the triangle is", normal, "nuits.")
      
# Below is the testing.

x = float(input("Give the first side lenth: "))
y = float(input("Give the second side lenth: "))

hyp(x, y)
