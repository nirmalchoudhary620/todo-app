import time
import functions  # Custom module for reading/writing todos
import FreeSimpleGUI as sg  # GUI framework
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# ----- Set GUI Theme -----
sg.theme("Black")  # Set window appearance

# ----- Define GUI Elements -----
clock = sg.Text("", key='clock')  # Digital clock display
label = sg.Text("Type in a to-do")  # Label for input field
input_box = sg.InputText(tooltip="Enter todo", key='todo')  # Text input for new/edit todo
add_button = sg.Button(image_size=(80,40), image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add todo", key="Add")  # Button to add a new todo

# List box to show current todos with live selection
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(45, 10))

edit_button = sg.Button("Edit")  # Button to edit selected todo
complete_button = sg.Button(image_size=(80,50), image_source="complete.png", mouseover_colors="LightBlue2", tooltip="Complete todo", key="Complete")  # Button to remove selected todo
exit_button = sg.Button("Exit")  # Button to exit the application

# ----- Define Layout and Create Window -----
window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20),  # Global font setting
                   resizable=True)  # Make window resizable

# ----- Main Event Loop -----
while True:
    # Read user interaction or window timeout
    event, values = window.read(timeout=100)

    # Exit conditions: Exit button clicked or window closed
    if event in (None, 'Exit', sg.WIN_CLOSED):
        break

    # Update clock on screen
    window["clock"].update(value=time.strftime("%b, %d, %Y %H:%M:%S"))

    # Handle UI Events using match-case
    match event:

        # --- Add Button Clicked ---
        case "Add":
            new_todo = values['todo'].strip()  # Get and clean input
            if new_todo:
                todos = functions.get_todos()  # Load current todos
                todos.append(new_todo + '\n')  # Add new item
                functions.write_todos(todos)  # Save updated list
                window['todos'].update(values=todos)  # Refresh UI
                window['todo'].update(value="")  # Clear input field
            else:
                sg.popup("Please enter a todo.", font=("Helvetica", 20))

        # --- Edit Button Clicked ---
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]  # Get selected item
                new_todo = values['todo'] + '\n'  # Get new input text

                todos = functions.get_todos()  # Load todos
                index = todos.index(todo_to_edit)  # Find item to edit
                todos[index] = new_todo  # Replace with new text
                functions.write_todos(todos)  # Save updated list

                window['todos'].update(values=todos)  # Refresh UI
                window['todo'].update(value="")  # Clear input field

            except IndexError:
                # No item selected for editing
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        # --- Complete Button Clicked ---
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]  # Get selected item
                todos = functions.get_todos()  # Load todos
                todos.remove(todo_to_complete)  # Remove selected item
                functions.write_todos(todos)  # Save updated list

                window['todos'].update(values=todos)  # Refresh UI
                window['todo'].update(value="")  # Clear input field

            except IndexError:
                # No item selected for completion
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        # --- List Item Selected ---
        case "todos":
            # Update input field when an item is selected
            window['todo'].update(value=values['todos'][0])

# ----- Close Window Gracefully -----
window.close()
