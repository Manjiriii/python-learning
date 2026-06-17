n = int(input("Enter a number: "))

length = 0
total = 0
temp = n

# Find number of digits
if n == 0:
    length = 1
else:
    while temp != 0:
        temp = temp // 10
        length += 1

print("Length of the number:", length)

temp = n

# Calculate Armstrong sum
while n > 0:
    r = n % 10
    total = total + (r ** length)
    n = n // 10

# Check Armstrong number
if total == temp:
    print(temp, "is an Armstrong Number")
else:
    print(temp, "is not an Armstrong Number")

# Example Output:
# Enter a number: 153
# Length of the number: 3
# 153 is an Armstrong Number
