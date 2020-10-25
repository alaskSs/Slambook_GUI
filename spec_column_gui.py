from tkinter import *
from tkinter import ttk
import csv


def on_click():
    value = ent_cat.get()
    d_col = value

    f = open("slambook.csv")
    reader = csv.reader(f)

    headers = None
    results = []
    for row in reader:
        if not headers:
            headers = []
            for i, col in enumerate(row):
                if col in d_col:
                    headers.append(i)

        else:
            print("\n")
            results.append(tuple([row[i] for i in headers]))

    text.insert(INSERT, results)


root = Tk()
root.geometry("1500x1200")
root.configure(background="blue")

# labels
Label(root, text="Enter Category :", font=("Arial Bold", 28), bg='black', fg='white').place(x=300, y=130)
Label(root, text="(in caps)", font=("Arial italic", 15),bg="blue").place(x=500, y=180)
Label(root, text="Output : ", font=("Arial Bold", 28), bg='black', fg='white').place(x=300, y=250)

# entry box
ent_cat = ttk.Entry(root, font=("helvetica", 20), justify=CENTER)
ent_cat.pack(anchor="ne", padx=300, pady=130)

# buttons
search = Button(root, text="Seacrh", width=15, height=1, font=("Arial Bold", 12),
              bg='black', fg='white', command=on_click).place(x=550, y=500)
back = Button(root, text="Back", width=15, height=1, font=("Arial Bold", 12), bg='black', fg='white',
              command=root.destroy).place(x=750, y=500)

# text box
text = Text(root, width=150, height=6)
text.pack(anchor="se", padx=320, pady=20)
root.mainloop()
