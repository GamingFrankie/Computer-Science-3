
# Red = 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
# Black = 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 24, 26, 28, 29, 31, 33, 35
# Green = 0, 00

from random import randrange
spin = randrange(0, 38)
if spin == 37:
  print("The spin resulted in 00...")
else:
  print("The spin resulted in %d..." % spin)
  # I use this %d to sub in the "spin" into the string.
if spin == 37:
  print("Pay 00")
else:
  print("Pay", spin)
# Colour of the number.
if (spin % 2 == 1 and spin >= 1 and spin <= 9) or (spin % 2 == 0 and spin >= 12 and spin <= 18) or (spin % 2 == 1 and spin >= 19 and spin <= 27) or (spin % 2 == 0 and spin >= 30 and spin <= 36):
  print("Pay Red")
elif spin == 0 or spin == 37:
  pass
else:
  print("Pay Black")
# Odd and even.
if spin >= 1 and spin <= 36:
  if spin % 2 == 1:
    print("Pay Odd")
  elif spin % 2 == 0:
    print("Pay Even")
# Number class.
if spin >= 1 and spin <= 18:
  print("Pay 1 to 18")
elif spin >= 19 and spin <= 36:
  print("Pay 19 to 36")
