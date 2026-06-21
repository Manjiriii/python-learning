pct=int(input("Enter percentage: "))
if pct>100 or pct<0:
    print("Invalid percentage")
elif pct>=90:
    print("O grade")
elif pct>=85:
    print("A+ grade")
elif pct>=75:
    print("A grade")
elif pct>=60:
    print("B+ grade")
elif pct>=50:
    print("B grade")
else:
    print("Try again")

#Output:
#Enter percentage: 96
#O grade
