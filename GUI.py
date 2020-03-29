from tkinter import *
import tkinter.messagebox, tkinter.simpledialog

def getBuildingName(code):
    if(code.upper() == "RBE"):
        tkinter.messagebox.showinfo("Code", "Beta")
    elif(code.upper() == "RBC"):
        tkinter.messagebox.showinfo("Code", "Castor")
    elif(code.upper() == "RKO"):
        tkinter.messagebox.showinfo("Code", "Kosove")
    elif(code.upper() == "RJH"):
        tkinter.messagebox.showinfo("Code", "Juniper")
    elif(code.upper() == "RPH"):
        tkinter.messagebox.showinfo("Code", "Poplar")
    elif(code.upper() == "MAA"):
        tkinter.messagebox.showinfo("Code", "Magnolia A")
    elif(code.upper() == "MAB"):
        tkinter.messagebox.showinfo("Code", "Magnolia B")
    elif(code.upper() == "MAC"):
        tkinter.messagebox.showinfo("Code", "Magnolia C")
    elif(code.upper() == "MAD"):
        tkinter.messagebox.showinfo("Code", "Magnolia D")
    elif(code.upper() == "MAE"):
        tkinter.messagebox.showinfo("Code", "Magnolia E")
    elif(code.upper() == "MAF"):
        tkinter.messagebox.showinfo("Code", "Magnolia F")
    elif(code.upper() == "MAG"):
        tkinter.messagebox.showinfo("Code", "Magnolia G")
    elif(code.upper() == "HAA"):
        tkinter.messagebox.showinfo("Code", "Holly A")
    elif(code.upper() == "HAB"):
        tkinter.messagebox.showinfo("Code", "Holly B")
    elif(code.upper() == "HAC"):
        tkinter.messagebox.showinfo("Code", "Holly C")
    elif(code.upper() == "HAD"):
        tkinter.messagebox.showinfo("Code", "Holly D")
    elif(code.upper() == "HAE"):
        tkinter.messagebox.showinfo("Code", "Holly E")
    elif(code.upper() == "HAF"):
        tkinter.messagebox.showinfo("Code", "Holly F")
    elif(code.upper() == "HAG"):
        tkinter.messagebox.showinfo("Code", "Holly G")
    elif(code.upper() == "RCA"):
        tkinter.messagebox.showinfo("Code", "Cypress A (Suites)")
    elif(code.upper() == "RCB"):
        tkinter.messagebox.showinfo("Code", "Cypress B (Suites)")
    elif(code.upper() == "RCC"):
        tkinter.messagebox.showinfo("Code", "Cypress C (Apartments)")
    elif(code.upper() == "RCD"):
        tkinter.messagebox.showinfo("Code", "Cypress D (Apartments)")
    elif(code.upper() == "MPA"):
        tkinter.messagebox.showinfo("Code", "Maple A")
    elif(code.upper() == "MPB"):
        tkinter.messagebox.showinfo("Code", "Maple B")
    elif(code.upper() == "RBN"):
        tkinter.messagebox.showinfo("Code", "Beacon")
    elif(code.upper() == "RSU"):
        tkinter.messagebox.showinfo("Code", "Summit")
    elif(code.upper() == "RPN"):
        tkinter.messagebox.showinfo("Code", "Pinnacle")
    elif(code.upper() == "REN"):
        tkinter.messagebox.showinfo("Code", "Endeavor")
    elif(code.upper() == "RHN"):
        tkinter.messagebox.showinfo("Code", "Horizon")
    elif(code.upper() == "GVA"):
        tkinter.messagebox.showinfo("Code", "Alpa Delta Pi")
    elif(code.upper() == "GVB"):
        tkinter.messagebox.showinfo("Code", "Gamma Phi Beta")
    elif(code.upper() == "GVC"):
        tkinter.messagebox.showinfo("Code", "Sigma Delta Tau")
    elif(code.upper() == "GVD"):
        tkinter.messagebox.showinfo("Code", "Zeta Tau Alpha")
    elif(code.upper() == "GVE"):
        tkinter.messagebox.showinfo("Code", "Delta Chi")
    elif(code.upper() == "GVF"):
        tkinter.messagebox.showinfo("Code", "Sigma Chi")
    elif(code.upper() == "GVG"):
        tkinter.messagebox.showinfo("Code", "Delta Gamma")
    elif(code.upper() == "GVH"):
        tkinter.messagebox.showinfo("Code", "Delta Delta Delta")
    elif(code.upper() == "GVI"):
        tkinter.messagebox.showinfo("Code", "Sigma Nu")
    elif(code.upper() == "GVJ"):
        tkinter.messagebox.showinfo("Code", "Zeta Beta Tau")
    elif(code.upper() == "GVK"):
        tkinter.messagebox.showinfo("Code", "Chi Omega")
    elif(code.upper() == "GVL"):
        tkinter.messagebox.showinfo("Code", "Sigma Phi Epsilon")
    elif(code.upper() == "GVM"):
        tkinter.messagebox.showinfo("Code", "Kappa Delta")
    elif(code.upper() == "GVN"):
        tkinter.messagebox.showinfo("Code", "Alpha Omicron Pi")
    else:
        tkinter.messagebox.showinfo("Code", "Invalid building code.")
    return

root = Tk()

code = tkinter.simpledialog.askstring("code", "Enter a code: ")

getBuildingName(code)

root.mainloop()
