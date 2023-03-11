# from functions import openfile_to_do, writefile

import functions

while True:
    user_input = input("Type add or show or edit or or complete or exit: ")
    user_input = user_input.strip()

    if user_input.startswith("add"):
        try:
            todo = user_input[4:]

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            todos = functions.openfile_to_do()

            todos.append(todo+"\n")

            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()
            functions.writefile('todos.txt', todos)

        except ValueError:
            print("You have an incorrect value")
            continue
    elif user_input.startswith("show"):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = functions.openfile_to_do()

        # new_todos = []

        # for item in todos:
        #     new_item = item.strip("\n")
        #     new_todos.append(new_item)

        new_todos = [item.strip("\n") for item in todos]

        for i, item in enumerate(new_todos):
            print(i+1, '-', item)

    elif user_input.startswith("edit"):
        try:

            edit_item = int(user_input[5:])
            edit_item = edit_item - 1

            todos = functions.openfile_to_do()

            new_todo = input("Enter a new To Do: ")
            todos[edit_item] = new_todo + "\n"

            functions.writefile('todos.txt', todos)

            print(new_todo)
        except (ValueError, IndexError):
            print("Invalid Edit input")
            continue
    elif user_input.startswith("complete"):
        try:
            completed_item = user_input[9:]

            todos = functions.openfile_to_do()

            item_removal = todos.pop(int(completed_item) - 1)
            print("You have completed: "+item_removal)

            functions.writefile('todos.txt', todos)
        except IndexError:
            print("Value not available in the To Do List")
            continue
    elif user_input.startswith("exit"):
        break
    else:
        print("Not a valid command! Please choose add/edit/show/complete/exit")

print("Bye!")
