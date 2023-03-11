# #Strings are immutable datatypes but could be updated using replace method and stored in a new variable.
# #Tuples are immutable form of List
# #Example to change the string value

# filename = '1.Raw Text.csv'

# print(filename.replace('.','-',1))

# #Coding Excercise

# dollar_input = input("How many dollars have you got? ")

# print("The amount in Euros is:\n" ,int(dollar_input)*0.95)

# #Coding Excercise-1

# ranking = ['John', 'Sen', 'Lisa']

# username_input = input("Enter a name: ")

# print(int(ranking.index(username_input))+1)

# #Learning List functions

# waiting_list = ['jan','feb','march','april','may','june']
# waiting_list.sort()

# for index, item in enumerate(waiting_list):
#     print(f"{index+1}-{item.capitalize()}")

# #Coding Execrcise-2

# filenames = ['document', 'report', 'presentation']

# for index, item in enumerate(filenames):
#     print(f"{index}-{item.capitalize()+'.txt'}")

# #Coding Exercise-3

# ips = ['100.122.133.105', '100.122.133.111']

# ip_print = int(input("Enter the index of the IP you want: "))
# print("You chose: ", ips.__getitem__(ip_print))

# #Change strings in list

# # Using List Comprehensions
#
# filenames = ["1.doc", "1.report", "1.presentation"]
#
# filenames = [filename.replace(".","-")+".txt" for filename in filenames]
#
# print(filenames)

# Coding Exercise

# #Bug Fixing Exercise
# def get_max():
#     grades = [9.6, 9.2, 9.7]
#     max_value = max(grades)
#     min_value = min(grades)
#     message = f"Max value: {max_value} and Min Value: {min_value}"
#     return message
#
# print(get_max())
#

# Bug Fixing Excercise

def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(
    100)
print(time)





