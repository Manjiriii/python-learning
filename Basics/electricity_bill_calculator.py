unit = int(input("Enter unit: "))
total = 0

if unit >= 0 and unit <= 100:
    total = unit * 3

elif unit <= 200:
    r = unit - 100
    total = 100 * 3 + r * 5

else:
    r = unit - 200
    total = 100 * 3 + 100 * 5 + r * 10

print("Total amount payable:", total, "rupees")
