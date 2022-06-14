#import
from tkinter import *
import pickle
import tkinter.messagebox

#Membuat Program
def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)
    else:
        tkinter.messagebox.showwarning(title= "Oops!", message="You Must Enter A Task!!")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Oops!", message="You Must Select A Task!!")

def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, END)
        for task in tasks:
            listbox_tasks.insert(END, task)
    except:
        tkinter.messagebox.showwarning(title="Oops!", message="Can't Find Tasks!!")

def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

def mark_task():
    try:
        listbox_tasks.itemconfig(listbox_tasks.curselection(), bg= "yellow")
        listbox_tasks.selection_clear(0, END)
    except:
        tkinter.messagebox.showwarning(title="Oops!", message="You Must Select A Task")

def unmark_task():
    try:
        listbox_tasks.itemconfig(listbox_tasks.curselection(), bg= "white")
        listbox_tasks.selection_clear(0,END)
    except:
        tkinter.messagebox.showwarning(title="Oops!", message="You Must Select A Task")

def del_all():
    deleteall = listbox_tasks.delete(0, END) 
    listbox_tasks.delete(deleteall)

#Membuat GUI
root = tkinter.Tk()
root.title("TO DO LIST APP")
root.geometry("600x550")
root.configure(bg="#082B59")
root.resizable(0,0)

label = Label(root, text = "WELCOME TO\nTO DO LIST APP\n================================================", 
              font = "Helvetica, 15 bold", width = 10, bd = 5, bg = "#082B59", fg = "white")      
label.pack(side = "top", fill = BOTH)

label2 = Label(root, text = "Your Current Task:", 
              font = "ariel, 10", bg = "#082B59", fg = "white")      
label2.pack()

frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=tkinter.Y)

listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=55, font="ariel, 10 bold")
listbox_tasks.pack()

listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

label2 = Label(root, text = "Write Your New Task Here:", font = "ariel, 10", fg = "white", bg= "#082B59") 
label2.pack()

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

space = Label(root, bg="#082B59")
space.pack()

button_add = tkinter.Button(root, text="Add Task", width=35, bg= "green", bd= 6,fg="white", command=add_task)
button_add.pack()

button_delete = tkinter.Button(root, text="Delete Task", width=35, bg= "red", bd= 6, fg="white",command=delete_task)
button_delete.pack()

button_mark = tkinter.Button(root, text= "Mark Task", width=35, bd=6, command=mark_task) 
button_mark.pack()

button_unmark = tkinter.Button(root, text= "UnMark Task", width=35, bd=6, command=unmark_task) 
button_unmark.pack()

button_load = tkinter.Button(root, text="Load", width=7, bd= 6, command=load_task)
button_load.place(x=15, y=145)

button_save = tkinter.Button(root, text="Save", width=7, bd=6, command=save_task)
button_save.place(x=15, y=106)

button_delall = tkinter.Button(root, text="Delete All Task", width=35, bd=6, command=del_all)
button_delall.pack()

root.mainloop()