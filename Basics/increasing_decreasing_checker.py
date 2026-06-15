a, b, c = map(float, input("Enter three numbers: ").split())

if a < b < c:
    print("Increasing")

elif a > b > c:
    print("Decreasing")

else:
    print("Neither")

# Example Output:
# Enter three numbers: 2 4 6
# Increasing
