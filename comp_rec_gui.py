from tkinter import *
import csv

root = Tk()
root.geometry("1500x1200")
root.configure(background="indigo")

lb1 = Label(root,text="Saved Record",bg='black',fg='white').place(x=600, y=100)

# open file
with open("slambook.csv", newline="") as file:
    reader = csv.reader(file)

    r = 0
    for col in reader:
        c = 0
        for row in col:
            label = Label(root, width=37, height=2,
                          text=row, relief=RAISED,font=("Arial Bold", 10),bg="indigo",fg="white")
            label.grid(row=r, column=c)
            c += 1
        r += 1


b1 = Button(root, text="Back", width=15, height=1, font=("Arial Bold", 10), bg='black', fg='white',
            command=root.destroy).place(x=690, y=750)

root.mainloop()
