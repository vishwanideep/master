while True:
    user_input = input("Type add or show or edit or or complete or exit: ")
    user_input = user_input.strip()

    match user_input:
        case 'add':
            todo = input("Enter a To Do: ") + "\n"

            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open('todos.txt', 'w')
            # file.writelines(todos)
            # file.close()

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = []

            # for item in todos:
            #     new_item = item.strip("\n")
            #     new_todos.append(new_item)

            new_todos = [item.strip("\n") for item in todos]

            for i, item in enumerate(new_todos):
                print(i+1, '-', item)
        case 'edit':
            edit_item = int(input("Enter the value you want to edit: "))
            edit_item = edit_item - 1

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new To Do: ")
            todos[edit_item] = new_todo + "\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            print(new_todo)
        case 'complete':
            completed_item = int(input("Enter the value of the completed item: "))

            todos.pop(completed_item - 1)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break
        case unusual_character:
            print("Goli Betaaaa!!! Masti Naaaaaiiiii")

print("Bye!")
