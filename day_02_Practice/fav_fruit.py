# Asking users fav_fruit
fav_fruits = ['apple', 'banana', 'pineapple', 'mango', 'orange']
users_fav = input("\nChoose your favorite fruit : ").lower()

# Condition to check if user fav_fruit in our list or not
if users_fav in fav_fruits:
    print(f"Oh you really like {users_fav}, me too")

else:
    print(f"You like {users_fav} but I dont ")