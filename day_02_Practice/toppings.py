# Available toppings in menu
Available_toppings = ['paneer', 'capsicum', 'corn', 'extra cheese', 'olive']
req_toppings = ['paneer', 'capsicum', 'corn']

# Loop to check requested toppings in available toppings
for req_toppings in Available_toppings:
    if req_toppings == 'corn':
        print(f"{req_toppings.title()} is not available")

    else:
        print(f"{req_toppings.title()} Added")
        
print("Your pizza will be ready soon")