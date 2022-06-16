#import
import tkinter.messagebox
import pickle
from tkinter import *
 
#Membuat Tampilan GUI
root = tkinter.Tk()
root.title("TO DO LIST APP")
root.geometry("600x550")
root.configure(bg="#293462")
root.resizable(0,0)
 
label = Label(root, text = "WELCOME TO\nTO DO LIST APP\n================================================",
              font = "Helvetica, 15 bold", width = 10, bd = 5, fg = "white", bg = "#293462")      
label.pack(side = "top", fill = BOTH)
 
label2 = Label(root, text = "Your Current Task:",
              font = "ariel, 10 bold", fg = "white", bg = "#293462")      
label2.pack()
 
#Membuat Fungsi Program
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
        tkinter.messagebox.showwarning(title="Opps!", message="You Must Select A Task!!")
 
def load_task():
    try:
        tasks = pickle.load(open("tasks.dat", "rb"))
        listbox_tasks.delete(0, END)
        for task in tasks:
            listbox_tasks.insert(END, task)
    except:
        tkinter.messagebox.showwarning(title="Opps!", message="Can't Find Tasks!!")
 
def save_task():
    CONFIRM_SAVE = tkinter.messagebox.askokcancel(title= "Confirmation!", message= "Are You Sure To Save Your List??", icon= "warning")
    if CONFIRM_SAVE:
        tasks = listbox_tasks.get(0, listbox_tasks.size())
        pickle.dump(tasks, open("tasks.dat", "wb"))
        tkinter.messagebox.showinfo(title="Status", message="Your List Updated!!")
       
def mark_task():
    try:
        listbox_tasks.itemconfig(listbox_tasks.curselection(), bg= "#f3fc3a")
        listbox_tasks.selection_clear(0, END)
    except:
        tkinter.messagebox.showwarning(title="Oops!", message="You Must Select A Task" )
 
def unmark_task():
    try:
        listbox_tasks.itemconfig(listbox_tasks.curselection(), bg= "white")
        listbox_tasks.selection_clear(0,END)
    except:
        tkinter.messagebox.showwarning(title="Oops!", message="You Must Select A Task" )
 
def del_all():
    CONFIRM_DELALL = tkinter.messagebox.askokcancel(title= "Confirmation!", message= "Are You Sure To Delete All Your List??", icon= "warning")
    if CONFIRM_DELALL:
        deleteall = listbox_tasks.delete(0, END)
        tkinter.messagebox.showinfo(title="Status", message="Your List Deleted Successfully!!")
        listbox_tasks.delete(deleteall)
 
#Membuat Elemen pada
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()
 
scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=tkinter.Y)
 
listbox_tasks = tkinter.Listbox(frame_tasks, height=10, width=55, font="ariel, 10 bold")
listbox_tasks.pack()
 
listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)
 
label2 = Label(root, text = "Write Your New Task Here:", font = "ariel, 9 bold", fg = "white", bg= "#293462")
label2.pack()
 
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()
 
space = Label(root, bg="#293462")
space.pack()
 
button_add = tkinter.Button(root, text="Add Task", width=35, bg= "#bffcc6", bd= 6, command=add_task)
button_add.pack()
 
button_delete = tkinter.Button(root, text="Delete Task", width=35, bg= "#ffabab", bd= 6, command=delete_task)
button_delete.pack()
 
button_mark = tkinter.Button(root, text= "Mark Task",bg="#f4fa87", width=35, bd=6, command=mark_task)
button_mark.pack()
 
button_unmark = tkinter.Button(root, text= "UnMark Task", bg="white", width=35, bd=6, command=unmark_task)
button_unmark.pack()
 
button_load = tkinter.Button(root, text="Load", bg= "#cccccc", width=7, bd= 6, command=load_task)
button_load.place(x=15, y=145)
 
button_save = tkinter.Button(root, text="Save", bg= "#cccccc" ,width=7, bd=6, command=save_task)
button_save.place(x=15, y=106)
 
button_delall = tkinter.Button(root, text="Delete All Task", bg= "#cccccc", bd= 6, width=35, command=del_all)
button_delall.pack()
 
 
root.mainloop()