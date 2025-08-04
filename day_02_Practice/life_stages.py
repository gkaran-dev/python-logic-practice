# Asking User to Input Age

print("\nThis program will tell you the person's current life stage")
persons_age = int(input("Enter the person's age please :\n"))

# Condition To Check Stage Of Life
if persons_age < 2:
    print("The person is a baby.")

elif persons_age < 4:
    print("The person is a toddler.")

elif persons_age < 13:
    print("The person is a kid.")

elif persons_age < 20:
    print("The person is a teenager.")

elif persons_age < 65:
    print("The person is an adult.")

else:
    print("The person is an elder")
