# # 1st excerise
#
# menu = ["pasta", "pizza", "salad"]
#
# user_choice = int(input("Enter the index of the item: "))
#
# message = f"You chose {menu[user_choice]}."
# print(message)
#
# # 2nd Excerise
#
# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate(menu):
#     print(f"{i}.{j}")

# Bug fixing exercise 1

# try:
#
#     waiting_list = ["john", "marry"]
#     name = input("Enter name: ")
#
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
#
# except ValueError as v:
#     exit(v)


def speed(distance, time):
    return distance / time


print(speed(time=5, distance=300))
