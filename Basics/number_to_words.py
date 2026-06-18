n = int(input("Enter a number: "))

length = 0
thousands = 0
hundreds = 0

temp = n

# Find length
if n == 0:
    length = 1
else:
    while temp != 0:
        temp = temp // 10
        length += 1

print("Length of the number:", length)

# Thousands part
if length == 4:

    while n >= 1000 and n <= 9999:
        n = n - 1000
        thousands += 1000

    if thousands == 1000:
        print("One Thousand", end=" ")
    elif thousands == 2000:
        print("Two Thousand", end=" ")
    elif thousands == 3000:
        print("Three Thousand", end=" ")
    elif thousands == 4000:
        print("Four Thousand", end=" ")
    elif thousands == 5000:
        print("Five Thousand", end=" ")
    elif thousands == 6000:
        print("Six Thousand", end=" ")
    elif thousands == 7000:
        print("Seven Thousand", end=" ")
    elif thousands == 8000:
        print("Eight Thousand", end=" ")
    elif thousands == 9000:
        print("Nine Thousand", end=" ")

    length -= 1

# Hundreds part
if length == 3:

    while n >= 100:
        n = n - 100
        hundreds += 100

    if hundreds == 100:
        print("One Hundred", end=" ")
    elif hundreds == 200:
        print("Two Hundred", end=" ")
    elif hundreds == 300:
        print("Three Hundred", end=" ")
    elif hundreds == 400:
        print("Four Hundred", end=" ")
    elif hundreds == 500:
        print("Five Hundred", end=" ")
    elif hundreds == 600:
        print("Six Hundred", end=" ")
    elif hundreds == 700:
        print("Seven Hundred", end=" ")
    elif hundreds == 800:
        print("Eight Hundred", end=" ")
    elif hundreds == 900:
        print("Nine Hundred", end=" ")

# Ones and Tens
ones = ["", "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine"]

tens = ["", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

special = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
           "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

# Last two digits
if n == 0:
    print()

elif n < 10:
    print("&", ones[n])

elif n < 20:
    print("&", special[n - 10])

elif n <= 99:
    t = n // 10
    o = n % 10

    if o == 0:
        print("&", tens[t])
    else:
        print("&", tens[t], ones[o])

else:
    print("Max limit exceeded")
