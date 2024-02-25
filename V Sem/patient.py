from tkinter import *
from tkinter import messagebox
from database import *



import tkinter as tk
from tkinter import ttk

class mlis_patient:

    def __init__(self, root):

        def on_search():
            if sel_option.get() == "":
                messagebox.showerror("Error", "Choose the test!")
            else:
                search(sel_option.get())

        self.root = root
        self.root.title("Medical Laboratory Information System")
        self.root.geometry("1540x800+0+0")
        self.root.configure(background="dark blue")

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Medical Laboratory Information System", fg="dark blue", bg="white", font=("times new roman", 50,"bold"))
        lbltitle.pack(side=TOP, fill=X)

        #======================DATAFRAMES======================
        DataframeTop=LabelFrame(self.root, bd=10, relief=RIDGE, font=("times new roman", 12, "bold"), text="SEARCH")
        DataframeTop.place(x=0, y=120, width=1530, height=90)

        DataframeAppt=LabelFrame(self.root, bd=10, relief=RIDGE, font=("times new roman", 12, "bold"), text="APPOINTMENT DETAILS")
        DataframeAppt.place(x=0, y=210, width=1530, height=120)

        DataframeBottom=LabelFrame(self.root, bd=10,relief=RIDGE, font=("times new roman", 12, "bold"), text="DETAILS")
        DataframeBottom.place(x=0, y=330, width=1530, height=460)

        # =====================SEARCH=============================
        lblTest=Label(DataframeTop, font=("times new roman", 15, "bold"), text="Test Name:", padx=50, pady=13)
        lblTest.grid(row=0, column=0)
        options = testnames
        sel_option=StringVar()
        txtTest = OptionMenu(DataframeTop, sel_option, *options)
        txtTest.grid(row=0, column=1, padx=50, pady=0, sticky="w")
        btnadd=Button(DataframeTop, text="SEARCH", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=5, command=on_search)
        btnadd.place(x=400, y=7)


def main_window_patient():
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    mlis_patient(root)
    root.mainloop()

main_window_patient()