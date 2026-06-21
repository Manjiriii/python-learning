x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x >= y and x >= z:
    print(x, "is the greatest")
elif y >= x and y >= z:
    print(y, "is the greatest")
else:
    print(z, "is the greatest")

#Output:
#Enter x: 5
#Enter y: 5
#Enter z: 2
#5 is the greatest
