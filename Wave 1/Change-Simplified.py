
toonie = 200
loonie = 100
quarter = 25
dime = 10
nickle = 5
cent = int(input("How many cents do you have? "))
print("The number of toonies are:", cent // toonie)
cent = cent % toonie
print("The number of loonies are:", cent // loonie)
cent = cent % loonie
print("The number of quarters are:", cent // quarter)
cent = cent % quarter
print("The number of dimes are:", cent // dime)
remain = cent % dime
print("The number of nickles are:", cent // nickle)
cent = cent % nickle
print("The number of cents remain:", cent)
