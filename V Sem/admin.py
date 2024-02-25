from tkinter import *
from tkinter import messagebox
from database import *

def labs(tab):

    def clear():
        txtLabName.delete(0, END)
        txtContactNo.delete(0, END)
        txtLocation.delete(0, END)
        txtOpenHrs.delete(0, END)
        txtYrsOfExp.delete(0, END)

    def on_lab_addclick():
        data = {"LabName": txtLabName.get(), "ContactNo": txtContactNo.get(), "Location": txtLocation.get(), "OpenHrs": txtOpenHrs.get(), "YrsOfExp": txtYrsOfExp.get()}
        if data["LabName"] == "" or data["ContactNo"] == "" or data["Location"] == "" or data["OpenHrs"] == "" or data["YrsOfExp"] == "":
            messagebox.showerror("Error", "Lab Name, Contact No. and Location fields cannot be empty!")
        else:
            c = lab_add(data)
            if c == None:
                messagebox.showerror("Error", "Failed to add the details!")
            else:
                messagebox.showinfo("success", "Details added successfully!")
                clear()

    def on_lab_updateclick():
        data = {"LabName": txtLabName.get(), "ContactNo": txtContactNo.get(), "Location": txtLocation.get(), "OpenHrs": txtOpenHrs.get(), "YrsOfExp": txtYrsOfExp.get()}
        if data["LabName"] == "" or data["ContactNo"] == "" or data["Location"] == "" or data["OpenHrs"] == "" or data["YrsOfExp"] == "":
            messagebox.showerror("Error", "Lab Name cannot be empty!")
        else:
            c = lab_update(data)
            if c == None:
                messagebox.showerror("Error", "Failed to update the details!")
            else:
                messagebox.showinfo("success", "Details updated successfully!")
                clear()
    
    def on_lab_deleteclick():
        data = {"LabName": txtLabName.get(), "ContactNo": txtContactNo.get(), "Location": txtLocation.get(), "OpenHrs": txtOpenHrs.get(), "YrsOfExp": txtYrsOfExp.get()}
        if data["LabName"] == "":
            messagebox.showerror("Error", "Lab Name cannot be empty!")
        else:
            c = lab_delete(data)
            if c == None:
                messagebox.showerror("Error", "No such entry exists!")
            else:
                messagebox.showinfo("success", "Deleted successfully!")
                clear()

    lblLabName=Label(tab, font=("times new roman", 12, "bold"), text="Lab Name:", padx=3, pady=6)
    lblLabName.grid(row=0, column=0)
    txtLabName=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtLabName.grid(row=0, column=1)

    lblContactNo=Label(tab, font=("times new roman", 12, "bold"), text="Contact No:", padx=3, pady=6)
    lblContactNo.grid(row=1, column=0)
    txtContactNo=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtContactNo.grid(row=1, column=1)

    lblLocation=Label(tab, font=("times new roman", 12, "bold"), text="Location:", padx=3, pady=6)
    lblLocation.grid(row=2, column=0)
    txtLocation=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtLocation.grid(row=2, column=1)

    lblOpenHrs=Label(tab, font=("times new roman", 12, "bold"), text="Open Hrs:", padx=3, pady=6)
    lblOpenHrs.grid(row=3, column=0)
    txtOpenHrs=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtOpenHrs.grid(row=3, column=1)

    lblYrsOfExp=Label(tab, font=("times new roman", 12, "bold"), text="Experience (in yrs):", padx=3, pady=6)
    lblYrsOfExp.grid(row=4, column=0)
    txtYrsOfExp=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtYrsOfExp.grid(row=4, column=1)

    #================buttons==============
    btnadd=Button(tab, text="ADD", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=6, command=on_lab_addclick)
    btnadd.place(x=20, y=250)
    btnupdate=Button(tab,text="UPDATE", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=6, command=on_lab_updateclick)
    btnupdate.place(x=185, y=250)
    btndelete=Button(tab,text="DELETE", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=6, command=on_lab_deleteclick)
    btndelete.place(x=350, y=250)

    # ===============Lab Details================
    DataframeRight=LabelFrame(tab,bd=10,padx=10,relief=RIDGE,font=("times new roman", 12, "bold"),text="Labs Available")
    DataframeRight.place(x=530, y=10, width=970, height=600)



def tests(tab):

    def clear():
        txtTestName.delete(0, END)
        txtDescription.delete(0, END)
        txtSampleType.delete(0, END)
        txtTestDuration.delete(0, END)
        txtNormalRange.delete(0, END)


    def on_test_addclick():
        data = {"TestName": txtTestName.get(), "Description": txtDescription.get(), "SampleType": txtSampleType.get(), "TestDuration": txtTestDuration.get(), "NormalRange": txtNormalRange.get()}
        if data["TestName"] == "" or data["Description"] == "" or data["SampleType"] == "" or data["TestDuration"] == "" or data["NormalRange"] == "":
            messagebox.showerror("Error", "Test Name and Description cannot be empty!")
        else:
            c = test_add(data)
            if c == None:
                messagebox.showerror("Error", "Failed to add the details!")
            else:
                messagebox.showinfo("success", "Details added successfully!")
                clear()

    def on_test_updateclick():
        data = {"TestName": txtTestName.get(), "Description": txtDescription.get(), "SampleType": txtSampleType.get(), "TestDuration": txtTestDuration.get(), "NormalRange": txtNormalRange.get()}
        if data["TestName"] == "" or data["Description"] == "" or data["SampleType"] == "" or data["TestDuration"] == "" or data["NormalRange"] == "":
            messagebox.showerror("Error", "Test Name and Description cannot be empty!")
        else:
            c = test_update(data)
            if c == None:
                messagebox.showerror("Error", "Failed to update the details!")
            else:
                messagebox.showinfo("success", "Details updated successfully!")
                clear()
    
    def on_test_deleteclick():
        data = {"TestName": txtTestName.get(), "Description": txtDescription.get(), "SampleType": txtSampleType.get(), "TestDuration": txtTestDuration.get(), "NormalRange": txtNormalRange.get()}
        if data["TestName"] == "":
            messagebox.showerror("Error", "Test Name cannot be empty!")
        else:
            c = test_delete(data)
            if c == None:
                messagebox.showerror("Error", "No such entry exists!")
            else:
                messagebox.showinfo("success", "Deleted successfully!")
                clear()

    lblTestName=Label(tab, font=("times new roman", 12, "bold"), text="Test Name:", padx=3, pady=6)
    lblTestName.grid(row=0, column=0)
    txtTestName=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtTestName.grid(row=0, column=1)

    lblDescription=Label(tab, font=("times new roman", 12, "bold"), text="Description:", padx=3, pady=6)
    lblDescription.grid(row=1, column=0)
    txtDescription=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtDescription.grid(row=1, column=1)

    lblSampleType=Label(tab, font=("times new roman", 12, "bold"), text="Sample Type:", padx=3, pady=6)
    lblSampleType.grid(row=2, column=0)
    txtSampleType=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtSampleType.grid(row=2, column=1)

    lblTestDuration=Label(tab, font=("times new roman", 12, "bold"), text="Test Duration:", padx=3, pady=6)
    lblTestDuration.grid(row=3, column=0)
    txtTestDuration=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtTestDuration.grid(row=3, column=1)

    lblNormalRange=Label(tab, font=("times new roman", 12, "bold"), text="Normal Range:", padx=3, pady=6)
    lblNormalRange.grid(row=4, column=0)
    txtNormalRange=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtNormalRange.grid(row=4, column=1)

    #================buttons==============
    btnadd=Button(tab, text="ADD", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=6, command=on_test_addclick)
    btnadd.place(x=20, y=250)
    btnupdate=Button(tab,text="UPDATE", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=6, command=on_test_updateclick)
    btnupdate.place(x=185, y=250)
    btndelete=Button(tab,text="DELETE", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=6, command=on_test_deleteclick)
    btndelete.place(x=350, y=250)

    # ===============Lab Details================
    DataframeRight=LabelFrame(tab,bd=10,padx=10,relief=RIDGE,font=("times new roman", 12, "bold"),text="Tests Available")
    DataframeRight.place(x=530, y=10, width=970, height=600)



def efficiency(tab):

    def clear():
        sel1_option.set("")
        sel2_option.set("")
        txtPrice.delete(0, END)
        txtTestsPerDay.delete(0, END)
        txtSensitivity.delete(0, END)
        txtSpecificity.delete(0, END)

    def on_efficiency_addclick():
        data = {"Lab": sel1_option.get(), "Test": sel2_option.get(), "Price": txtPrice.get(), "TestsPerDay": txtTestsPerDay.get(), "Sensitivity": txtSensitivity.get(), "Specificity": txtSpecificity.get()}
        if data["Lab"] == "" or data["Test"] == "" or data["Price"] == "" or data["TestsPerDay"] == "" or data["Sensitivity"] == "" or data["Specificity"] == "":
            messagebox.showerror("Error", "Fields cannot be empty!")
        else:
            c = efficiency_add(data)
            if c == None:
                messagebox.showerror("Error", "Failed to add the details!")
            else:
                messagebox.showinfo("success", "Details added successfully!")
                clear()

    def on_efficiency_updateclick():
        data = {"Lab": sel1_option.get(), "Test": sel2_option.get(), "Price": txtPrice.get(), "TestsPerDay": txtTestsPerDay.get(), "Sensitivity": txtSensitivity.get(), "Specificity": txtSpecificity.get()}
        if data["Lab"] == "" or data["Test"] == "" or data["Price"] == "" or data["TestsPerDay"] == "" or data["Sensitivity"] == "" or data["Specificity"] == "":
            messagebox.showerror("Error", "Fields cannot be empty!")
        else:
            c = efficiency_update(data)
            if c == None:
                messagebox.showerror("Error", "Failed to update the details!")
            else:
                messagebox.showinfo("success", "Details updated successfully!")
                clear()
    
    def on_efficiency_deleteclick():
        data = {"Lab": sel1_option.get(), "Test": sel2_option.get(), "Price": txtPrice.get(), "TestsPerDay": txtTestsPerDay.get(), "Sensitivity": txtSensitivity.get(), "Specificity": txtSpecificity.get()}
        if data["Lab"] == "" or data["Test"] == "":
            messagebox.showerror("Error", "Lab Name and Test Name cannot be empty!")
        else:
            efficiency_delete(data)
            messagebox.showinfo("success", "Deleted successfully!")
            clear()

    lblLab=Label(tab, font=("times new roman", 12, "bold"), text="Lab:", padx=3, pady=6)
    lblLab.grid(row=0, column=0)
    options = labnames
    sel1_option=StringVar()
    lab = OptionMenu(tab, sel1_option, *options)
    lab.grid(row=0, column=1, padx=0, pady=0, sticky="w")

    lblTest=Label(tab, font=("times new roman", 12, "bold"), text="Test:", padx=3, pady=6)
    lblTest.grid(row=1, column=0)
    options = testnames
    sel2_option=StringVar()
    test = OptionMenu(tab, sel2_option, *options)
    test.grid(row=1, column=1, padx=0, pady=0, sticky="w")

    lblPrice=Label(tab, font=("times new roman", 12, "bold"), text="Price:", padx=3, pady=6)
    lblPrice.grid(row=2, column=0)
    txtPrice=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtPrice.grid(row=2, column=1)

    lblTestsPerDay=Label(tab, font=("times new roman", 12, "bold"), text="Tests per Day:", padx=3, pady=6)
    lblTestsPerDay.grid(row=3, column=0)
    txtTestsPerDay=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtTestsPerDay.grid(row=3, column=1)

    lblSensitivity=Label(tab, font=("times new roman", 12, "bold"), text="Sensitivity:", padx=3, pady=6)
    lblSensitivity.grid(row=4, column=0)
    txtSensitivity=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtSensitivity.grid(row=4, column=1)

    lblSpecificity=Label(tab, font=("times new roman", 12, "bold"), text="Specificity:", padx=3, pady=6)
    lblSpecificity.grid(row=5, column=0)
    txtSpecificity=Entry(tab, font=("times new roman", 12, "bold"), width=35)
    txtSpecificity.grid(row=5, column=1)

    #================buttons==============
    btnadd=Button(tab, text="ADD", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=6, command=on_efficiency_addclick)
    btnadd.place(x=20, y=250)
    btnupdate=Button(tab,text="UPDATE", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=6, command=on_efficiency_updateclick)
    btnupdate.place(x=185, y=250)
    btndelete=Button(tab,text="DELETE", bg="green", fg="white", font=("times new roman", 12, "bold"), width=15, padx=2, pady=6, command=on_efficiency_deleteclick)
    btndelete.place(x=350, y=250)

    # ===============Lab Details================
    DataframeRight=LabelFrame(tab,bd=10,padx=10,relief=RIDGE,font=("times new roman", 12, "bold"),text="Efficiencies")
    DataframeRight.place(x=530, y=10, width=970, height=600)




import tkinter as tk
from tkinter import ttk

conn, cursor = initialize_connection()

class mlis_admin:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Laboratory Information System")
        self.root.geometry("1540x800+0+0")
        self.root.configure(background="dark blue")

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Medical Laboratory Information System", fg="dark blue", bg="white", font=("times new roman", 50,"bold"))
        lbltitle.pack(side=TOP, fill=X)

        #======================DATAFRAMES======================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=120,width=1530,height=400)

        def on_tab_change(event):
            current_tab = notebook.index(notebook.select())
            if current_tab == 0:
                labs(tab1)
            elif current_tab == 1:
                tests(tab2)
            else:
                efficiency(tab3)
        notebook=ttk.Notebook(self.root)
        tab1 = tk.Frame(notebook, bd=10, relief=RIDGE)
        tab2 = tk.Frame(notebook, bd=10, relief=RIDGE)
        tab3 = tk.Frame(notebook, bd=10, relief=RIDGE)
        notebook.add(tab1, text="Labs")
        notebook.add(tab2, text="Tests")
        notebook.add(tab3, text="Efficiency")
        ttk.Style().configure("TNotebook.Tab", font=("times new roman",12,"bold"), padding=(5, 5))
        notebook.place(x=0, y=5, width=980, height=350)
        notebook.bind("<<NotebookTabChanged>>", on_tab_change)
        notebook.pack(fill="both", expand=True, padx=0, pady=0)

        # DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("times new roman", 12, "bold"),text="Lab Test Details")
        # DataframeLeft.place(x=0, y=5, width=980, height=350)
        # DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,font=("times new roman", 12, "bold"),text="Tests Available")
        # DataframeRight.place(x=990, y=5, width=460, height=350)

        # =========================button frames======================
        # buttonframe=Frame(self.root, bd=10, relief=RIDGE)
        # buttonframe.place(x=0, y=530, width=1530, height=70)

        # # =========================Details frames======================
        # Detailsframe=Frame(self.root, bd=10, relief=RIDGE)
        # Detailsframe.place(x=0, y=600, width=1530, height=190)

        # #====================Dataframeleft=============================

        # lblTestName=Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Test Name:", padx=2, pady=6)
        # lblTestName.grid(row=0, column=0)
        # txtTestname=Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        # txtTestname.grid(row=0, column=1)

        # lblDescription=Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Description:", padx=2, pady=6)
        # lblDescription.grid(row=1, column=0)
        # txtDescription=Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        # txtDescription.grid(row=1, column=1)

        # lblSampleType=Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Sample Type:", padx=2, pady=6)
        # lblSampleType.grid(row=2, column=0)
        # txtSampleType=Entry(DataframeLeft, font=("times new roman", 12, "bold"), width=35)
        # txtSampleType.grid(row=2, column=1)

        # comNameTablet=ttk.combobox(DataframeLeft,font=("times new roman",12,"bold"),width=33)

def main_window_admin():
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    mlis_admin(root)
    root.mainloop()

main_window_admin()