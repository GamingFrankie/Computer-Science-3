
# I feel no meaning to do a seperate version for wave 3,
# because I am dealing with while loops in this wave.
factor = 2
while True:
  dec = float(input("Enter a number: "))
  number = int(round(dec))
  if number < 2:
    print()
    print("Please enter a number greater or equal to 2.")
    print()
  if number >= 2:
    if dec == number:
      print()
      print("The prime numbers for " + str(number) + ":")
      print()
    elif dec != number:
      print()
      print(str(dec) + " has been rounded to " + str(number) + ", the prime numbers for " + str(number) + ":")
      print()
  while (factor <= number) == True:
    if number % factor == 0:
      print(factor)
      number = int(number / factor)
      print()
    else:
      factor += 1
