# Code for todo list app.
from functions import get_todos, write_todo
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
print("HI!!!  Welcome to the todo list app!!!\n")
todos = []
while True:
    # takes the input about what the user wants to do.
    print("Enter the todo to be  added,updated or removed with the desired option in the same line ....")
    user_action = input("Select add,show,update,remove,exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        # todo = input("Enter the todo:-") + "\n"

        todos = get_todos()
        todos.append(todo + '\n')

        # writes the todo into the file todos.txt.
        write_todo(todos)


    elif user_action.startswith('show'):

        todos = get_todos()
        # new_todos = []                # to strip \n from the output.

        # for item in todos:
        #   new_item = item.strip('\n')
        #   new_todos.append(new_item)

        # new_todos = [item.strip('\n') for item in todos]
        # list comprehension........another way to strip \n from the output

        # shows the todo list.
        for index, items in enumerate(todos):
            items = items.title()
            items = items.strip('\n')
            better_version = f"{index + 1}-{items}"
            print(better_version)


    elif user_action.startswith('update'):
        try:
            # updates the existing todo with the new todo.
            print("Enter the number of todo to be updated.")
            # number = int(input("Enter the number:"))
            number = int(user_action[7:])
            number -= 1

            todos = get_todos()

            new_todo = input("Enter the new todo:-")
            todos[number] = new_todo + '\n'

            write_todo(todos)

        except ValueError:
            print("Your command is not valid. Try again....")
            continue


    elif user_action.startswith('remove'):
        try:
            # removes any todo user wants to remove
            # remv_todo = int(input("Enter the no.of todo to remove:-"))
            remv_todo = int(user_action[7:])

            todos = get_todos()

            index = remv_todo - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            write_todo(todos)

            message = f"Todo {todo_to_remove} has been removed!"
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue


    elif user_action.startswith('exit'):
        break

    else:
        print("You entered a wrong command, retry!!")

print("Thanks for using my app!!")
print("Bye, have a nice day!!!!")
