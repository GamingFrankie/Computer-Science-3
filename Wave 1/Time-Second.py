# The calculations from seconds to units are

# second = input
# minute = 60 * second
# hour = 60 * minute
# day = 24 * hour

second = float(input("How many seconds? - Your Answer: "))

day = int(second // (24 * 3600))
# How many seconds remaining.
second = second % (24 * 3600)

hour = int(second // (60 * 60))
second = second % (60 * 60)

minute = int(second // 60)
second = second % 60
second = int(second)
hour = f"{hour:02}"
minute = f"{minute:02}"
second = f"{second:02}"
second = str(second)
minute = str(minute)
hour = str(hour)
day = str(day)
print("The time is: " + day + ":" + hour + ":" + minute + ":" + second)
