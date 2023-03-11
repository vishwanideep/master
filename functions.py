def openfile_to_do(openfile='todos.txt'):
    with open(openfile, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def writefile(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)