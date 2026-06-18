n = int(input("Enter a number: "))

length = 0
rev = 0
temp = n

# Find length
if n == 0:
    length = 1
else:
    while temp != 0:
        temp = temp // 10
        length += 1

print("Length of the number:", length)

# Reverse the number
while n > 0:
    r = n % 10
    rev = rev * 10 + r
    n = n // 10

print("Reversed number:", rev)

# Example Output:
# Enter a number: 12345
# Length of the number: 5
# Reversed number: 54321
