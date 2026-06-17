n = int(input("Enter a number: "))

length = 0
total = 0
temp = n

if n == 0:
    length = 1
else:
    while temp != 0:
        temp = temp // 10
        length += 1

print("Length of the number:", length)

temp = n

while n > 0:
    r = n % 10

    fact = 1
    for i in range(1, r + 1):
        fact = fact * i

    total = total + fact
    n = n // 10

if total == temp:
    print(temp, "is a Strong Number")
else:
    print(temp, "is not a Strong Number")

# Example Output:
# Enter a number: 145
# Length of the number: 3
# 145 is a Strong Number
