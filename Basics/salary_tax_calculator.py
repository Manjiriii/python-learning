sal = int(input("Enter salary: "))
tax = 0

if sal < 0:
    print("Invalid salary")

elif sal <= 500000:
    tax = 0

elif sal <= 700000:
    tax = (sal - 500000) * 0.10

elif sal <= 900000:
    tax = (200000 * 0.10) + (sal - 700000) * 0.20

else:
    tax = (200000 * 0.10) + (200000 * 0.20) + (sal - 900000) * 0.30

net = sal - tax

print("Tax payable:", tax)
print("Net salary:", net)
