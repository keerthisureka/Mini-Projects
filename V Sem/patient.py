from tkinter import *
from tkinter import messagebox
from database import *


import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

class mlis_patient:
    def __init__(self, root, email):

        def fetch_data(details, details_table):
            if len(details) != 0:
                details_table.delete(*details_table.get_children())
                for i in details:
                    details_table.insert("", END, values=i)

        def on_search():
            DataframeIn=LabelFrame(DataframeBottom, bd=0,relief=RIDGE, font=("times new roman", 12, "bold"))
            DataframeIn.place(x=0, y=0, width=1530, height=430)
            scroll_x = ttk.Scrollbar(DataframeIn, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(DataframeIn, orient=VERTICAL)
            details_table = ttk.Treeview(DataframeIn, column=("id0", "id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8", "id9", "id10", "id11", "id12"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=details_table.xview)
            scroll_y.config(command=details_table.yview)
            details_table.heading("id0", text="Test Name")
            details_table.heading("id1", text="Lab Name")
            details_table.heading("id2", text="Contact No")
            details_table.heading("id3", text="Location")
            details_table.heading("id4", text="Price")
            details_table.heading("id5", text="Open Hrs")
            details_table.heading("id6", text="Yrs Of Experience")
            details_table.heading("id7", text="Description")
            details_table.heading("id8", text="Sample Type")
            details_table.heading("id9", text="Test Duration")
            details_table.heading("id10", text="Tests Per Day")
            details_table.heading("id11", text="Sensitivity")
            details_table.heading("id12", text="Specificity")
            details_table["show"] = "headings"
            details_table.pack(fill=BOTH, expand=1)

            if sel_option.get() == "":
                messagebox.showerror("Error", "Choose the test!")
            else:
                details_view = search(sel_option.get())
                fetch_data(details_view, details_table)

        def on_book():
            DataframeIn=LabelFrame(DataframeBottom, bd=0,relief=RIDGE, font=("times new roman", 12, "bold"))
            DataframeIn.place(x=0, y=0, width=1530, height=430)
            scroll_x = ttk.Scrollbar(DataframeIn, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(DataframeIn, orient=VERTICAL)
            details_table = ttk.Treeview(DataframeIn, column=("id0", "id1", "id2", "id3", "id4"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=details_table.xview)
            scroll_y.config(command=details_table.yview)
            details_table.heading("id0", text="Test Name")
            details_table.heading("id1", text="Lab Name")
            details_table.heading("id2", text="Location")
            details_table.heading("id3", text="Price")
            details_table.heading("id4", text="Appointment Date")
            details_table["show"] = "headings"
            details_table.pack(fill=BOTH, expand=1)

            if sel1_option.get() == "" or sel2_option.get() == "" or txtApptDate.get_date() == "":
                messagebox.showerror("Error", "Choose Test, Lab and Appointment Date Details!")
            else:
                details_view = book(email, sel1_option.get(), sel2_option.get(), txtApptDate.get_date())
                fetch_data(details_view, details_table)


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
        btnadd=Button(DataframeTop, text="Search", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=5, command=on_search)
        btnadd.place(x=400, y=7)

        # =================APPOINTMENT=============================
        lblTestName=Label(DataframeAppt, font=("times new roman", 15, "bold"), text="Test Name:", padx=20, pady=13)
        lblTestName.grid(row=0, column=0)
        options1 = testnames
        sel1_option=StringVar()
        txtTestName = OptionMenu(DataframeAppt, sel1_option, *options1)
        txtTestName.grid(row=0, column=1, padx=50, pady=0, sticky="w")

        lblLabName=Label(DataframeAppt, font=("times new roman", 15, "bold"), text="Lab Name:", padx=20, pady=13)
        lblLabName.grid(row=0, column=2)
        options2 = labnames
        sel2_option=StringVar()
        txtLabName = OptionMenu(DataframeAppt, sel2_option, *options2)
        txtLabName.grid(row=0, column=3, padx=50, pady=0, sticky="w")

        today = datetime.now().date()
        lblApptDate=Label(DataframeAppt, font=("times new roman", 15, "bold"), text="Appointment Date:", padx=20, pady=13)
        lblApptDate.grid(row=0, column=4)
        txtApptDate=DateEntry(DataframeAppt, font=("times new roman", 12, "bold"), width=20, date_pattern="yyyy/mm/dd", mindate=today)
        txtApptDate.grid(row=0, column=5)

        btnappt=Button(DataframeAppt, text="Book Appointment", bg="green", fg="white", font=("times new roman", 12, "bold"), width=20, padx=2, pady=5, command=on_book)
        btnappt.place(x=1200, y=7)

def main_window_patient(email):
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    mlis_patient(root, email)
    root.mainloop()
