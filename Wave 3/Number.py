print("Prime Number")
while True: 
  print()
  print("Your number will be rounded if it is not a integer.")
  dec = float(input("Enter a number: "))
  number = int(round(dec))
  print()
  if number >= 2:

    def prime(number):
      for value in range(2, number):
        if number % value == 0:
          return False
      return True

    if prime(number):
      print(number, "is prime.")
    else:
      print(number, "is NOT prime.")
    
  elif number == 1:
    print("YOUR INPUT IS INVALID")
    print()
    print("By Defination:")
    print("Prime numbers are any integer that greater than one,")
    print("and it also has only 1 and themselve as factors.")
    print("If a number is not a prime number,")
    print("it could be divisible prime numbers.")
