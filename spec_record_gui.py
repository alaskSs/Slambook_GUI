from tkinter import *
from tkinter import ttk


def on_click():
    idx = ent_name.get()
    with open('slambook.csv', 'r') as f:
        data = f.readlines()
    for d in data:
        if d.find(str(idx)) != -1:
            text.insert(INSERT, d)
            break


root = Tk()
root.geometry("1500x1200")
root.configure(background="green")

Label(root, text="Enter Name :", font=("Arial Bold", 28), bg='black', fg='white').place(x=300, y=130)
Label(root, text="(in caps)", font=("Arial italic", 15),bg="green").place(x=450, y=180)
Label(root, text="Output : ", font=("Arial Bold", 28), bg='black', fg='white').place(x=300, y=250)

# entry box
ent_name = ttk.Entry(root, font=("helvetica", 20, "bold"), justify=CENTER)
ent_name.pack(anchor="ne", padx=300, pady=140)

# buttons
show = Button(root, text="Show", width=15, height=1, font=("Arial Bold", 12),
              bg='black', fg='white', command=on_click).place(x=550, y=500)
back = Button(root, text="Back", width=15, height=1, font=("Arial Bold", 12), bg='black', fg='white',
              command=root.destroy).place(x=750, y=500)

# text box
text = Text(root, width=150, height=6)
text.pack(anchor="se", padx=320, pady=20)
root.mainloop()
