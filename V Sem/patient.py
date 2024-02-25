from tkinter import *
from tkinter import messagebox
from database import *


import tkinter as tk
from tkinter import ttk

class mlis_patient:

    def __init__(self, root, email):

        def fetch_data(details):
            if len(details) != 0:
                self.details_table.delete(*self.details_table.get_children())
                for i in details:
                    self.details_table.insert("", END, values=i)

        def on_search():
            scroll_x = ttk.Scrollbar(DataframeBottom, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(DataframeBottom, orient=VERTICAL)
            self.details_table = ttk.Treeview(DataframeBottom, column=("id0", "id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8", "id9", "id10", "id11", "id12"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.details_table.xview)
            scroll_y.config(command=self.details_table.yview)
            self.details_table.heading("id0", text="Test Name")
            self.details_table.heading("id1", text="Lab Name")
            self.details_table.heading("id2", text="Contact No")
            self.details_table.heading("id3", text="Location")
            self.details_table.heading("id4", text="Price")
            self.details_table.heading("id5", text="Open Hrs")
            self.details_table.heading("id6", text="Yrs Of Experience")
            self.details_table.heading("id7", text="Description")
            self.details_table.heading("id8", text="Sample Type")
            self.details_table.heading("id9", text="Test Duration")
            self.details_table.heading("id10", text="Tests Per Day")
            self.details_table.heading("id11", text="Sensitivity")
            self.details_table.heading("id12", text="Specificity")
            self.details_table["show"] = "headings"
            self.details_table.pack(fill=BOTH, expand=1)

            if sel_option.get() == "":
                messagebox.showerror("Error", "Choose the test!")
            else:
                details_view = search(sel_option.get())
                fetch_data(details_view)

        def on_book():
            scroll_x = ttk.Scrollbar(DataframeBottom, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(DataframeBottom, orient=VERTICAL)
            self.details_table = ttk.Treeview(DataframeBottom, column=("id0", "id1", "id2", "id3", "id4"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=self.details_table.xview)
            scroll_y.config(command=self.details_table.yview)
            self.details_table.heading("id0", text="Test Name")
            self.details_table.heading("id1", text="Lab Name")
            self.details_table.heading("id2", text="Location")
            self.details_table.heading("id3", text="Price")
            self.details_table.heading("id4", text="Appointment Date")
            self.details_table["show"] = "headings"
            self.details_table.pack(fill=BOTH, expand=1)

            if sel1_option.get() == "" or sel2_option.get() == "":
                messagebox.showerror("Error", "Choose Test, Lab and Appointment Date Details!")
            else:
                details_view = book(email, sel1_option.get(), sel2_option.get(), txtApptDate.get())
                fetch_data(details_view)


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

        #==================scroll bar for table====================
        # scroll_x = ttk.Scrollbar(DataframeBottom, orient=HORIZONTAL)
        # scroll_y = ttk.Scrollbar(DataframeBottom, orient=VERTICAL)
        # self.details_table = ttk.Treeview(DataframeBottom, column=("id0", "id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8", "id9", "id10", "id11", "id12"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        # scroll_x.pack(side=BOTTOM, fill=X)
        # scroll_y.pack(side=RIGHT, fill=Y)

        # scroll_x.config(command=self.details_table.xview)
        # scroll_y.config(command=self.details_table.yview)

        
        # =================APPOINTMENT=============================
        lblTestName=Label(DataframeAppt, font=("times new roman", 15, "bold"), text="Test Name:", padx=20, pady=13)
        lblTestName.grid(row=0, column=0)
        options = testnames
        sel2_option=StringVar()
        txtTestName = OptionMenu(DataframeAppt, sel2_option, *options)
        txtTestName.grid(row=0, column=1, padx=50, pady=0, sticky="w")

        lblLabName=Label(DataframeAppt, font=("times new roman", 15, "bold"), text="Lab Name:", padx=20, pady=13)
        lblLabName.grid(row=0, column=2)
        options = labnames
        sel1_option=StringVar()
        txtLabName = OptionMenu(DataframeAppt, sel1_option, *options)
        txtLabName.grid(row=0, column=3, padx=50, pady=0, sticky="w")

        lblApptDate=Label(DataframeAppt, font=("times new roman", 15, "bold"), text="Appointment Date:", padx=20, pady=13)
        lblApptDate.grid(row=0, column=4)
        txtApptDate=Entry(DataframeAppt, font=("times new roman", 12, "bold"), width=30)
        txtApptDate.grid(row=0, column=5)

        btnappt=Button(DataframeAppt, text="Book Appointment", bg="green", fg="white", font=("times new roman", 12, "bold"), width=20, padx=2, pady=5, command=on_book)
        btnappt.place(x=1200, y=7)

        #=========for lab table==========
        # scroll_x = ttk.Scrollbar(DataframeBottom, orient=HORIZONTAL)
        # scroll_y = ttk.Scrollbar(DataframeBottom, orient=VERTICAL)
        # self.medical_table = ttk.Treeview(DataframeBottom, column=("id", "id1", "id2", "id3", "id4","id5"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        # scroll_x.pack(side=BOTTOM, fill=X)
        # scroll_y.pack(side=RIGHT, fill=Y)

        # scroll_x.config(command=self.medical_table.xview)
        # scroll_y.config(command=self.medical_table.yview)

        # self.medical_table.heading("id", text="LabID")
        # self.medical_table.heading("id1", text="LabName")
        # self.medical_table.heading("id2", text="ContactNo")
        # self.medical_table.heading("id3", text="Location")
        # self.medical_table.heading("id4", text="OpenHrs")
        # self.medical_table.heading("id5", text="YrsOfExp")
        
        # self.medical_table["show"] = "headings"
        # self.medical_table.pack(fill=BOTH, expand=1)



def main_window_patient(email):
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    mlis_patient(root, email)
    root.mainloop()


main_window_patient("sharon@gmail.com")