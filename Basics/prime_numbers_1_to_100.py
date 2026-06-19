print("Prime numbers from 1 to 100:")

for n in range(1, 101):

    if n < 2:
        continue

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            break

    else:
        print(n, end=" ")
        

# Output:
# Prime numbers from 1 to 100:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97


