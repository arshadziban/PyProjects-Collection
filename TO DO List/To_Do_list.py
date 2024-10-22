import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("TO DO List")
root.geometry("400x650+400+100")
root.resizable(False, False)

#colors
header_bg = "#1F5741"  
button_bg = "#14755C"  
task_bg = "#D3D3D3" 
add_text_button = "#FFFFFF"

# remove button image
#please use your path
remove_icon = Image.open(r"C:\Users\USER\Desktop\Progmming\Python Projects\TO DO list\remove.png") 
remove_icon = remove_icon.resize((20, 20), Image.Resampling.LANCZOS)  
remove_photo = ImageTk.PhotoImage(remove_icon)  

# Header frame
header_frame = Canvas(root, bg=header_bg, height=60, width=400, highlightthickness=0)
header_frame.create_rectangle(20, 20, 380, 60, outline="", fill=header_bg, width=2)  #
header_frame.pack(fill=BOTH)
header_label = Label(root, text="TASKS", bg=header_bg, fg="white", font=("Arial", 18, "bold"))
header_label.place(relx=0.5, y=30, anchor=CENTER) 

# entry field frame 
task_frame = Frame(root, bg=task_bg, bd=0, highlightthickness=0)
task_frame.pack(fill=BOTH, pady=5)

# Task input box
task_entry = Entry(task_frame, width=20, font=("Arial", 16), bg=add_text_button, bd=0, highlightthickness=0, relief=FLAT)
task_entry.grid(row=0, column=0, padx=20, pady=10)

# Add button
add_button = Button(task_frame, text="ADD", width=5, bg=button_bg, fg="white", font=("Arial", 12), command=lambda: add_task())
add_button.grid(row=0, column=1, padx=10)

# Task list frame
task_list_frame = Frame(root, bg=task_bg)
task_list_frame.pack(fill=BOTH, expand=True, pady=10)

# Task list data
task_list = []

#display tasks
def display_tasks():
    for widget in task_list_frame.winfo_children():
        widget.destroy() 

    for index, task in enumerate(task_list):
        task_frame = Frame(task_list_frame, bg=task_bg)
        task_frame.pack(fill=X, pady=5)

        # Task label
        task_label = Label(task_frame, text=task, font=("Arial", 14), bg=task_bg, anchor="w")
        task_label.pack(side=LEFT, fill=X, expand=True, padx=10)

        # Remove button
        remove_button = Button(task_frame, image=remove_photo, bd=0, bg=task_bg, 
                               command=lambda i=index: remove_task(i))  # Command to remove the specific task
        remove_button.pack(side=RIGHT, padx=10)

#add a task
def add_task():
    task = task_entry.get()
    if task:
        task_list.append(task)
        task_entry.delete(0, END)
        display_tasks()

#remove a specific task by index
def remove_task(index):
    if index < len(task_list):
        task_list.pop(index) 
        display_tasks()

# Display tasks
display_tasks()

root.mainloop()
