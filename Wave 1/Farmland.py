print("Welcome to the Farmland Calculator!")
print("-----------------------------------")
while True: 
  lenth = float(input("What is the LENTH of the farmland (feet)? "))
  width = float(input("What is the WIDTH of the farmland (feet)? "))
  print("-----------------------------------")
  print("The LENTH is", lenth)
  print("The WIDTH is", width)
  print("-----------------------------------")
  print("Confirm?")
  print("Yes = Y")
  print("No = N")
  answer = input("Your Answer: ")
  if answer == "Y":
    print("-----------------------------------")
    area = lenth * width
    acres = area // 43560
    print("The Area in SQUARE FEET is:", area )
    print("The Area in ACRES is about:", acres)
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