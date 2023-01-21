todos = []


while True:
    user_input = input("Type add or show or edit or or complete or exit: ")
    user_input = user_input.strip()

    match user_input:
        case 'add':
            todo = input("Enter a To Do: ")
            todos.append(todo)
        case 'show':
            for i, item in enumerate(todos):
                print(i+1, '-',item)
        case 'edit':
            edit_item = int(input("Enter the value you want to edit: "))
            edit_item = edit_item -1 
            new_todo = input("Enter a new To Do: ")
            todos[edit_item] = new_todo
            print(new_todo)
        case 'complete':
            completed_item = int(input("Enter the value of the completed item: "))
            todos.pop(completed_item - 1)
        case 'exit':
            break
        
        case unusual_character:
            print("Goli Betaaaa!!! Masti Naaaaaiiiii")

print("Bye!")

