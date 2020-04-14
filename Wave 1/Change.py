print("Welcome to Change Calculator!")
print("-----------------------------------")

while True:
  toonie = 200
  loonie = 100
  quarter = 25
  dime = 10
  nickle = 5
  cent = int(input("How many cents do you have? "))
  print("-----------------------------------")

  print("The number of toonies are:", cent // toonie)
  remain = cent % toonie
  cent = remain
  print("The number of loonies are:", cent // loonie)
  remain = cent % loonie
  cent = remain
  print("The number of quarters are:", cent // quarter)
  remain = cent % quarter
  cent = remain
  print("The number of dimes are:", cent // dime)
  remain = cent % dime
  cent = remain
  print("The number of nickles are:", cent // nickle)
  remain = cent % nickle
  cent = remain
  print("The number of cents remain:", cent)
  
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
