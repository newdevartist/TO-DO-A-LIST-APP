# Import the Tkinter library
import tkinter as tk

# Create a function to add tasks
def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_entry.delete(0, tk.END)
    update_listbox()

# Create a function to delete tasks
def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if len(selected_task_index) > 0:
        del tasks[selected_task_index[0]]
        update_listbox()

# Create a function to update the listbox
def update_listbox():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END, task)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a listbox to display tasks
tasks_listbox = tk.Listbox(root)
tasks_listbox.pack(pady=20)

# Create an entry field for adding tasks
task_entry = tk.Entry(root)
task_entry.pack()

# Create a button to add tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Create a button to delete tasks
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Initialize the tasks list
tasks = []

# Update the listbox with the initial tasks
update_listbox()

# Run the main loop
root.mainloop()

#This app has the following features:
#A listbox to display tasks
#An entry field for adding tasks
#A button to add tasks
#A button to delete tasks
#To run this app, save the code in a file with a .py extension (e.g., to_do_list.py) and execute it using a Python interpreter.