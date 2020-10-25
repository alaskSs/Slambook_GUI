from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv


def on_click():
    with open("slambook.csv", "r") as f:
        data = f.read()
        text.insert("1.0", data)


def to_save():
    edited_data = text.get(1.0, "end")
    with open("slambook.csv", "w") as f:
        f.write(str(edited_data)+"\n")
    messagebox.askyesno("Option", "Do you want to save")
    root.destroy()


root = Tk()
root.geometry("1500x1200")
root.configure(background="orange")

Label(root, text="Editor : ", font=("Arial Bold", 28), bg='black', fg='white').place(x=300, y=130)

# buttons
search = Button(root, text="Search", width=15, height=1, font=("Arial Bold", 12),
                bg='black', fg='white', command=on_click).place(x=500, y=550)
back = Button(root, text="Back", width=15, height=1, font=("Arial Bold", 12), bg='black', fg='white',
              command=root.destroy).place(x=900, y=550)

save = Button(root, text="Save", width=15, height=1, font=("Arial Bold", 12), bg='black', fg='white',
              command=to_save).place(x=700, y=550)

# text box
text = Text(root, width=150, height=20)
text.pack(anchor="se", padx=320, pady=200)
root.mainloop()
