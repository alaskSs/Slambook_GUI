from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

row = []

root = Tk()

root.geometry("1500x1200")
root.configure(background="red")
root.title("ADD RECORD")

lbl = Label(root, text="DETAILS :", font=("helvetica", 30, "bold"), bg='black', fg='white')
lbl.place(x=200, y=80)


def to_save():
    row = [E1.get(), E2.get(), E3.get(), E4.get(), E5.get()]
    fo = open('slambook.csv', 'a')
    obj = csv.writer(fo)
    obj.writerow(row)
    fo.close()
    messagebox.askyesno("Option", "Do you want to save")
    root.destroy()


# *****************************NAME******************************

lbl1 = Label(root, text="NAME", font=("Arial Bold", 20),bg="red")
lbl1.place(x=350, y=220)
E1 = ttk.Entry(root, font=("Arial", 20), justify=CENTER)
E1.place(x=900, y=220)

lb1 = Label(root, text="::", font=("Arial Bold", 20),bg="red")
lb1.place(x=750, y=220)

# ***************************address****************************
lbl2 = Label(root, text="ADDRESS", font=("Arial Bold", 20),bg="red")
lbl2.place(x=350, y=270)
E2 = ttk.Entry(root, font=("Arial", 20), justify=CENTER)
E2.place(x=900, y=270)

lb2 = Label(root, text="::", font=("Arial Bold", 20),bg="red")
lb2.place(x=750, y=270)

# ****************************contact no.************************
lbl3 = Label(root, text="CONTACT NO.", font=("Arial Bold", 20),bg="red")
lbl3.place(x=350, y=320)
E3 = ttk.Entry(root, font=("Arial", 20), justify=CENTER)
E3.place(x=900, y=320)

lb3 = Label(root, text="::", font=("Arial Bold", 20),bg="red")
lb3.place(x=750, y=320)

# *******************************email*******************************
lbl4 = Label(root, text="EMAIL ID", font=("Arial Bold", 20),bg="red")
lbl4.place(x=350, y=370)
E4 = ttk.Entry(root, font=("Arial", 20), justify=CENTER)
E4.place(x=900, y=370)

lb4 = Label(root, text="::", font=("Arial Bold", 20),bg="red")
lb4.place(x=750, y=370)

# ***********************************DOB*************************

lbl5 = Label(root, text="D.O.B", font=("Arial Bold", 20),bg="red")
lbl5.place(x=350, y=420)
E5 = ttk.Entry(root, font=("Arial", 20), justify=CENTER)
E5.place(x=900, y=420)

lb5 = Label(root, text="::", font=("Arial Bold", 20),bg="red")
lb5.place(x=750, y=420)

# **************************Buttons***************************

b1 = Button(root, text="Back", width=15, height=1, font=("Arial Bold", 10), bg='black', fg='white',
            command=root.destroy).place(x=770, y=500)
b2 = Button(root, text="Save", width=15, height=1, font=("Arial Bold", 10), bg='black', fg='white',
            command=to_save).place(x=620, y=500)


root.mainloop()