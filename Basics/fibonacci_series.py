n = int(input("Enter number of terms: "))

t1, t2 = 0, 1

print("Fibonacci Series up to", n, "terms:")

for i in range(n):
    print(t1, end=" ")

    next_term = t1 + t2
    t1 = t2
    t2 = next_term
