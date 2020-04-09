print("Welcome to Compound Interest Calculator!")

percentage = float(input("What is the percentage of interest? "))
interest = percentage * 0.01
time = float(input("Number of time compounded in one year? "))
save = float(input("How much is your saving? "))

# A = P * (1 + r / n)^nt

# Year 1
yearOne = (1 + interest / time)

# Year 2
yearTwo = (1 + interest / time) * (1 + interest / time)

# Year 3
yearThree = (1 + interest / time) * (1 + interest / time) * (1 + interest / time)

print("The amount after first year is: "'%.2f' % round(save * yearOne, 2))
print("The amount after second year is: "'%.2f' % round(save * yearTwo, 2))
print("The amount after third year is: "'%.2f' % round(save * yearThree, 2))
