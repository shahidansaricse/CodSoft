import tkinter as tk
from tkinter import messagebox
import json
import os

TASK_FILE = 'tasks.json'

# Load existing tasks
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

# Save current tasks
def save_tasks():
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file)

# Add a new task
def add_task():
    task = entry.get()
    if task:
        tasks.append({'description': task, 'done': False})
        entry.delete(0, tk.END)
        update_task_list()
        save_tasks()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# Mark selected task as done
def mark_done():
    selected = listbox.curselection()
    if selected:
        tasks[selected[0]]['done'] = True
        update_task_list()
        save_tasks()

# Delete selected task
def delete_task():
    selected = listbox.curselection()
    if selected:
        del tasks[selected[0]]
        update_task_list()
        save_tasks()

# Update the task list in the GUI
def update_task_list():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task['done'] else "✘"
        listbox.insert(tk.END, f"{task['description']} [{status}]")

# Main App Window
app = tk.Tk()
app.title("To-Do List")

tasks = load_tasks()

entry = tk.Entry(app, width=40)
entry.pack(pady=10)

btn_frame = tk.Frame(app)
btn_frame.pack()

tk.Button(btn_frame, text="Add Task", width=12, command=add_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Mark Done", width=12, command=mark_done).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Delete Task", width=12, command=delete_task).pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(app, width=50, height=10)
listbox.pack(pady=10)

update_task_list()

app.mainloop()
