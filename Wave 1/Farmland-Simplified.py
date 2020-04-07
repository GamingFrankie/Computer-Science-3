print("Welcome to the Farmland Calculator!")
print("-----------------------------------")

lenth = float(input("What is the LENTH of the farmland (feet)? "))
width = float(input("What is the WIDTH of the farmland (feet)? "))
print("-----------------------------------")
    
area = lenth * width
acres = area // 43560

print("The Area in SQUARE FEET is:", area )
print("The Area in ACRES is about:", acres)
