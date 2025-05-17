from tkinter import *

# Function to handle button clicks
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Create main window
root = Tk()
root.title("GUI Calculator")
root.geometry("300x420")
root.resizable(False, False)

# Input field
entry_var = StringVar()
entry = Entry(root, textvar=entry_var, font="Arial 20", bd=8, relief=SUNKEN, justify=RIGHT)
entry.pack(fill=X, padx=10, pady=10)

# Frame for buttons
button_frame = Frame(root)
button_frame.pack()

# Button layout with "." included
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["="]
]

# Create buttons dynamically
for row in buttons:
    frame = Frame(button_frame)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = Button(frame, text=btn_text, font="Arial 18", height=2, width=5)
        button.pack(side=LEFT, expand=True, fill="both", padx=2, pady=2)
        button.bind("<Button-1>", click)

# Run the app
root.mainloop()
