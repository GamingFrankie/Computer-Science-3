print("What is the name of the month?")
date = input("Your answer (Eg: January/Jan): ")
if date == "February" or date == "Feb":
  print("The number of days in this month is 28 or 29.")
elif date == "January" or date == "Jan" or date == "March" or date == "Mar" or date == "May" or date == "July" or date == "Jul" or date == "August" or date == "Aug" or date == "October" or date == "Oct" or date == "December" or date == "Dec":
  print("The number of days in this month is 31.")
elif date == "April" or date == "Apr" or date == "June" or date == "Jun" or date == "September" or date == "Sep" or date == "November" or date == "Nov":
  print("The number of days in this month is 30.")
else:
  print("Syntax Error, Please Check The Spelling And The Initial.")
