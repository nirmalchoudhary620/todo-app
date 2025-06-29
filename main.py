#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

# Infinite loop to continuously accept user input
while True:
    # Prompt the user for an action
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  # Remove extra spaces from the input

    # ADD a new todo
    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'  # Extract the todo text and add newline

        todos = functions.get_todos()  # Read existing todos
        todos.append(todo)  # Add new todo to the list

        functions.write_todos(todos)  # Write updated list back to file

    # SHOW all todos
    elif user_action.startswith("show"):
        todos = functions.get_todos()  # Read todos from file

        # Display each todo with its number
        for index, item in enumerate(todos):
            item = item.strip('\n')  # Remove newline for clean output
            row = f"{index + 1}.{item}"  # Format with numbering
            print(row)

    # EDIT an existing todo
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])  # Get the todo number from input
            number = number - 1  # Convert to zero-based index

            todos = functions.get_todos()  # Read todos

            new_todo = input("Enter new todo: ")  # Ask for new text
            todos[number] = new_todo + '\n'  # Replace the old todo

            functions.write_todos(todos)  # Save updated todos

        except ValueError:
            print("Your command is not valid.")  # Handle invalid number input
            continue

    # COMPLETE (remove) a todo
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])  # Get the todo number
            todos = functions.get_todos()  # Read current todos

            index = number - 1  # Convert to zero-based index
            todo_to_remove = todos[index].strip('\n')  # Get todo text for message
            todos.pop(index)  # Remove the selected todo

            functions.write_todos(todos)  # Save updated list

            message = f"{todo_to_remove} todo was removed successfully"
            print(message)

        except IndexError:
            print("There is no item with that number.")  # Handle out-of-range input
            continue

    # EXIT the program
    elif user_action.startswith("exit"):
        break  # Exit the loop and end program

    else:
        print("Command is not valid.")  # Handle unrecognized commands

print("Bye!")  # Print farewell message
