words = str(input("Original Sentence:  "))
words = words.lower()
note = ",?.!/;:"
for char in note:
  words = words.replace(char, "")

string = words.split()
print("Pig Latin Sentence: ", end=" ")

for letter in string:
  vowel = ["a", "e", "i", "o", "u"]

  if letter[0] == vowel[0] or letter[0] == vowel[1] or letter[0] == vowel[2] or letter[0] == vowel[3] or letter[0] == vowel[4]:
    print(letter + "way", end = " ")

  else:
    print(letter[1:] + letter[0] + "ay", end = " ")

