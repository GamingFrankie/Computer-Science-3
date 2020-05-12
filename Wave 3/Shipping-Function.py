
# Shipping Calculator Function

def charge(number):
  if type(number) != int:
    print("Please input an integer.")
  else:
    number -= 1
    initial = 10.95
    if number != 0:
      final = number * 2.95 + initial
      final = round(final, 2)
      final = format(final, ".2f")
      print("Total Charge is", str(final), "dollars.")
    else:
      final = initial
      print("Total Charge is", str(final), "dollars.")
      
# Below is the testing.

x = input("Give an integer: ")
i = int(x)
charge(i)
