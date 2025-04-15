
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    #strip removes the spaces on the answer, so if we add "add " with a space, it will remove the space.

    if user_action.startswith('add'):
        todo = user_action[4:]
        # with [4:] we are extracting the letters before index of 4 starting from 0, we do this to remove
        # the word add, so we only get the to do. Example: add take out the robbish, only take out... will be taken

        # we use "\n" to make a space everytime we insert a new to do, we have a separate line for the todos.txt


        # The whole next code its been replaced by the code below under the mark ****

        # The following code creates a file where the list will be storage
        #file = open('todos.txt', 'r')
        # 'r' it means we want only to read the item. We are opening this file in read mode.
        #todos = file.readlines()
        # with todos = file.readlines() we are getting in read mode all the previous entries to the to do list.
        #file.close()
        # we close the file, because if it stays open it may interfere with other files

        #****, reference from above, with these 2 lines of codes we avoid using the 3 lines of code above
        # and the result is the same.
        todos = functions.get_todos()

        todos.append(todo + '\n')

        #file = open('todos.txt', 'w')
        # we use file = open.... and one of the argument is 'w', because we want to write if we only
        # want to read we put 'r'
        #file.writelines(todos)
        #file.close()
        # after the file has been edited, we need to close it as well to avoid interferences.

        # here is the same situation as the block above mark with *****
        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]
        # the previous code is another way to get rid of the extra space between items on the list.

        for index, item in enumerate(todos):
            # enumerate, adds a number at the beginning of each item in the list.
            item = item.strip('\n')
            # .strip('\n) removes the extra space created between each item on the list
            item = item.title()
            row = f"{index + 1}-{item}"
            # f"..." allows us to manage the output text whatever way we want.
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            # int changes the number from string to integer
            # [5:] it takes only the number, deleting edit whit has index from 0 to 4.
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            # we use continue so the program starts again from the beginning, otherwise it will get stuck here
            # if an error happens.
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)
            # pop removes an element.

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is not item with that number")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid command")


print("bye!")
