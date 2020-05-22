
# Reverse Lookup

def  reverseLookup(dictionary, lookup):
  result = []

  for key, value in dictionary.items():
    if value == lookup:
      result.append(key)
    elif result == []:
      result = "Absent"
      
  print(result)
  if result == "Absent":
    print("Term Not Found.")
    

# Demo

print("Number List")
# I copy and paste definations from the actual dictionary and formated into a python understandable format.
dictionary = {'a': 1, 'b': 3, 'c': 2, 'd': 1}
while True:
  lookup = int(input("please type in a number: "))
  reverseLookup(dictionary, lookup)
  print("")
