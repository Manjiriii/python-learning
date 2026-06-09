n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

hcf = 0

if n1 < n2:
    minimum = n1
else:
    minimum = n2

print("Common factors:")

for i in range(1, minimum + 1):
    if n1 % i == 0 and n2 % i == 0:
        print(i, end=" ")
        hcf = i

print("\nHCF of", n1, "and", n2, "is:", hcf)

lcm = (n1 * n2) // hcf
print("LCM of", n1, "and", n2, "is:", lcm)
