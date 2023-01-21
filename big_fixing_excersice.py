# 1st excerise

menu = ["pasta", "pizza", "salad"]
 
user_choice = int(input("Enter the index of the item: "))
 
message = f"You chose {menu[user_choice]}."
print(message)

# 2nd Excerise

menu = ["pasta", "pizza", "salad"]
 
for i, j in enumerate(menu):
    print(f"{i}.{j}")