FILEPATH = "todos.txt"

#todos.txt and main.py have to be on the same folder, otherwise the storage of our list won't work.

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items"""
    # by adding a default variable to filepath, then we don't need to specified it when we call the function,
    # unless we want to change the defarult file, then we can especify it when we call it.
    with open(filepath, 'r') as file_local:
        # using with open(.... this will close the file automatically, so that is why we don't use file.close()
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write a list of to-do items to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print("Hello from functions")
