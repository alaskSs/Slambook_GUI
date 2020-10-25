from tkinter import *

from PIL import ImageTk, Image


def show_Img(file):
    img = Image.open(file)
    img = img.resize((30, 26), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(img)
    return pic


def call_add():
    import add_gui


def call_edit():
    import edit_gui


def call_delete():
    import delete_gui


def call_spe_rec():
    import spec_record_gui


def call_spec_col():
    import spec_column_gui


def call_comp_rec():
    import comp_rec_gui


if __name__ == '__main__':
    root = Tk()
    # Main Title
    root.geometry("1500x1200")
    root.title("Slambook")

    # Heading and layout
    lbl = Label(root, text="SLAMBOOK", font=("helvetica", 38, "bold"))
    lbl.pack(pady=10)

    # Sub Heading
    lbl = Label(root, text="Main Menu :", font=("Arial Bold", 28), bg='black', fg='white')
    lbl.pack(anchor="nw", padx=150, pady=5)

    # Options

    # *************************************TO ADD*******************************************

    lbl1 = Label(root, text="ADD RECORD", font=("Arial Bold", 20), bg='red')
    lbl1.place(x=350, y=200)
    lbl1.pack(fill=X, pady=15)

    pic_add = show_Img("add.png")

    btn = Button(lbl1, bd='5', font=("bold", 10)
                 , command=call_add, bg='red', image=pic_add)
    btn.pack(side=RIGHT, padx=120, pady=6)

    # ***********************************To EDIT*****************************************

    lbl2 = Label(root, text="EDIT RECORD", font=("Arial Bold italic", 20), bg='orange', fg='white')
    lbl2.place(x=350, y=250)
    lbl2.pack(fill=X, pady=15)

    pic_edit = show_Img("edit.png")

    btn = Button(lbl2, bd='5',
                 command=call_edit, bg='orange', image=pic_edit)
    btn.pack(side=RIGHT, padx=120, pady=6)

    # ************************************DELETE Record*******************************

    lbl3 = Label(root, text="DELETE RECORD", font=("Arial Bold", 20), bg='yellow')
    lbl3.place(x=350, y=300)
    lbl3.pack(fill=X, pady=15)

    pic_delete = show_Img("delete.png")

    btn = Button(lbl3, bd='5',
                 command=call_delete, bg='yellow', image=pic_delete)
    btn.pack(side=RIGHT, padx=120, pady=6)

    # **********************************Specific Record***********************************

    lbl4 = Label(root, text="DISPLAY SPECIFIC RECORD", font=("Arial Bold italic", 20), bg='green', fg='white')
    lbl4.place(x=350, y=350)
    lbl4.pack(fill=X, pady=15)

    pic_srec = show_Img("display.png")

    btn = Button(lbl4, bd='5',
                 command=call_spe_rec, bg='green', image=pic_srec)
    btn.pack(side=RIGHT, padx=120, pady=6)

    # ***************************************Specific Column************************************

    lbl5 = Label(root, text="DISPLAY SPECIFIC CATEGORY", font=("Arial Bold", 20), bg='blue')
    lbl5.place(x=350, y=400)
    lbl5.pack(fill=X, pady=15)

    pic_screc = show_Img("display.png")

    btn = Button(lbl5, bd='5',
                 command=call_spec_col, bg='blue', image=pic_screc)
    btn.pack(side=RIGHT, padx=120, pady=6)

    # ****************************************Complete Record***********************************

    lbl6 = Label(root, text="DISPLAY COMPLETE RECORD", font=("Arial Bold italic", 20), bg='indigo', fg='white')
    lbl6.place(x=350, y=450)
    lbl6.pack(fill=X, pady=15)

    pic_crec = show_Img("display.png")

    btn = Button(lbl6, bd='5',
                 command=call_comp_rec, bg='indigo', image=pic_crec)
    btn.pack(side=RIGHT, padx=120, pady=6)

    # Exit
    lbl7 = Label(root, text="EXIT", font=("Arial Bold", 20), bg='violet')
    lbl7.place(x=350, y=500)
    lbl7.pack(fill=X, pady=15)

    pic_exit = show_Img("exit.png")

    btn = Button(lbl7, bd='5',
                 command=root.destroy, bg='violet', image=pic_exit)
    btn.pack(side=RIGHT, padx=120, pady=6)

    root.mainloop()
