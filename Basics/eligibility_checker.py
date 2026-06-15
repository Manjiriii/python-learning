age, country = input("Enter age and country: ").split()

age = int(age)

if age >= 18 and country == "India":
    print("Eligible")

else:
    print("Not Eligible")

# Example Output:
# Enter age and country: 20 India
# Eligible
