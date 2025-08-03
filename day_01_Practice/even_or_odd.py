# Ask user to input a number

numbers = int(input("Enter the number to check its even or odd ?"))

# checking the given number is even or odd
if numbers % 2 == 0:
    print(f" ✅ Result : The number {numbers} is even")

else:
    print(f" ✅ Result : The number {numbers} is odd")