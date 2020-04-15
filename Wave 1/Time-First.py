# The calculations from units to seconds are

# second = output
# minute = 60 * second
# hour = 60 * minute
# day = 24 * hour

day = float(input("How many days? - Your Answer: ")) * 24 * 3600
hour = float(input("How many hours? - Your Answer: ")) * 60 * 60
minute = float(input("How many minutes? - Your Answer: ")) * 60
second = float(input("How many seconds? - Your Answer: "))
total = day + hour + minute + second

if total == 1 or total == 0:
  word = " second."
elif total != 1 and total != 0:
  word = " seconds."

print("The total is " + f"{total:.2f}" + word)
