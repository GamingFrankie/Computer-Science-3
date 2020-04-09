
percentage = float(input("What is the percentage of interest? "))
interest = percentage * 0.01
save = float(input("How much is your saving? "))

# A = P * (1 + r / n)^nt

# Year 1
yearOne = (1 + interest / 1)

# Year 2
yearTwo = (1 + interest / 1) * (1 + interest / 1)

# Year 3
yearThree = (1 + interest / 1) * (1 + interest / 1) * (1 + interest / 1)

print("The amount after first year is: "'%.2f' % round(save * yearOne, 2))
print("The amount after second year is: "'%.2f' % round(save * yearTwo, 2))
print("The amount after third year is: "'%.2f' % round(save * yearThree, 2))
