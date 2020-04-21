print("This program will check the type of a integer.")
print("-----------------------------------")
while True:
  number = input("Please input a integer: ")
  print("-----------------------------------")
  if type(number) != int:
    print("The input", "'" + number + "'", "is not a INTEGER.")
  elif (number % 2) == 0:
    print("The number", int(number), "is an even number.")
  elif (number % 2) == 1:
    print("The number", int(number), "is an odd number.")
  print("-----------------------------------")
  print("Exit?")
  print("Yes = Y")
  print("No = N")
  answer = input("Your Answer: ")
  if answer == "Y":
      break
  elif answer == "N":
      print("-----------------------------------")
  else:
      print("Invalid answer.")
      print("-----------------------------------")
