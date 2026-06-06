n = int(input("Enter a number: "))

if n == 0 or n == 1:
    print(n, "is not a prime number")

else:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print(n, "is not a prime number")
            break

    else:
        print(n, "is a prime number")
