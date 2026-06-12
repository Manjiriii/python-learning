rows = 5

for i in range(rows):

    num = i + 1
    add = rows - 1

    for j in range(i + 1):
        print(num, end=" ")

        num = num + add
        add -= 1

    print()

# Output:
# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15
