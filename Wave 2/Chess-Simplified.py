print("What is the position of your chess piece? Please use lower case letters")
position = str(input())
horizontal = position[0]
vertical = position[1]
if horizontal == "a" or horizontal == "c" or horizontal == "e" or horizontal == "g":
  if int(vertical) % 2 == 0 and int(vertical) <= 8:
    print("The chess piece is in a white square.")
  elif int(vertical) % 2 == 1 and int(vertical) <= 8:
    print("The chess piece is in a black square.")
  else:
    print("This is a invalid input.")
elif horizontal == "b" or horizontal == "d" or horizontal == "f" or horizontal == "h":
  if int(vertical) % 2 == 0 and int(vertical) <= 8:
    print("The chess piece is in a black square.")
  elif int(vertical) % 2 == 1 and int(vertical) <= 8:
    print("The chess piece is in a white square.")
  else:
    print("This is a invalid input.")
