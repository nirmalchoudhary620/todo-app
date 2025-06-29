FILEPATH = 'files/todos.txt'

# Function to read todos from a file
def get_todos(filepath = FILEPATH):
    """
       Reads and returns a list of todo items from the specified file.

       Args:
           filepath (str, optional): Path to the file containing todo items.
                                     Defaults to 'files/todos.txt'.

       Returns:
           list: A list of strings, each representing a todo item.
       """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # Read all lines into a list
    return todos_local  # Return the list of todos


# Function to write todos to a file
def write_todos(todos_arg, filepath = FILEPATH):
    """
        Writes a list of todo items to the specified file.

        Args:
            todos_arg (list): The list of todo items to write to the file.
            filepath (str, optional): Path to the file where the items will be written.
                                      Defaults to 'files/todos.txt'.
        """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)  # Write the list of todos to the file