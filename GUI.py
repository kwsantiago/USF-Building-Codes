from tkinter import *
import tkinter.messagebox, tkinter.simpledialog
import requests

HEIGHT = 400
WIDTH = 400

def getBuildingName(code):
    if(code.upper() == "RBE"):
        tkinter.messagebox.showinfo("Name", "Beta")
    elif(code.upper() == "RBC"):
        tkinter.messagebox.showinfo("Name", "Castor")
    elif(code.upper() == "RKO"):
        tkinter.messagebox.showinfo("Name", "Kosove")
    elif(code.upper() == "RJH"):
        tkinter.messagebox.showinfo("Name", "Juniper")
    elif(code.upper() == "RPH"):
        tkinter.messagebox.showinfo("Name", "Poplar")
    elif(code.upper() == "MAA"):
        tkinter.messagebox.showinfo("Name", "Magnolia A")
    elif(code.upper() == "MAB"):
        tkinter.messagebox.showinfo("Name", "Magnolia B")
    elif(code.upper() == "MAC"):
        tkinter.messagebox.showinfo("Name", "Magnolia C")
    elif(code.upper() == "MAD"):
        tkinter.messagebox.showinfo("Name", "Magnolia D")
    elif(code.upper() == "MAE"):
        tkinter.messagebox.showinfo("Name", "Magnolia E")
    elif(code.upper() == "MAF"):
        tkinter.messagebox.showinfo("Name", "Magnolia F")
    elif(code.upper() == "MAG"):
        tkinter.messagebox.showinfo("Name", "Magnolia G")
    elif(code.upper() == "HAA"):
        tkinter.messagebox.showinfo("Name", "Holly A")
    elif(code.upper() == "HAB"):
        tkinter.messagebox.showinfo("Name", "Holly B")
    elif(code.upper() == "HAC"):
        tkinter.messagebox.showinfo("Name", "Holly C")
    elif(code.upper() == "HAD"):
        tkinter.messagebox.showinfo("Name", "Holly D")
    elif(code.upper() == "HAE"):
        tkinter.messagebox.showinfo("Name", "Holly E")
    elif(code.upper() == "HAF"):
        tkinter.messagebox.showinfo("Name", "Holly F")
    elif(code.upper() == "HAG"):
        tkinter.messagebox.showinfo("Name", "Holly G")
    elif(code.upper() == "RCA"):
        tkinter.messagebox.showinfo("Name", "Cypress A (Suites)")
    elif(code.upper() == "RCB"):
        tkinter.messagebox.showinfo("Name", "Cypress B (Suites)")
    elif(code.upper() == "RCC"):
        tkinter.messagebox.showinfo("Name", "Cypress C (Apartments)")
    elif(code.upper() == "RCD"):
        tkinter.messagebox.showinfo("Name", "Cypress D (Apartments)")
    elif(code.upper() == "MPA"):
        tkinter.messagebox.showinfo("Name", "Maple A")
    elif(code.upper() == "MPB"):
        tkinter.messagebox.showinfo("Name", "Maple B")
    elif(code.upper() == "RBN"):
        tkinter.messagebox.showinfo("Name", "Beacon")
    elif(code.upper() == "RSU"):
        tkinter.messagebox.showinfo("Name", "Summit")
    elif(code.upper() == "RPN"):
        tkinter.messagebox.showinfo("Name", "Pinnacle")
    elif(code.upper() == "REN"):
        tkinter.messagebox.showinfo("Name", "Endeavor")
    elif(code.upper() == "RHN"):
        tkinter.messagebox.showinfo("Name", "Horizon")
    elif(code.upper() == "GVA"):
        tkinter.messagebox.showinfo("Name", "Alpa Delta Pi")
    elif(code.upper() == "GVB"):
        tkinter.messagebox.showinfo("Name", "Gamma Phi Beta")
    elif(code.upper() == "GVC"):
        tkinter.messagebox.showinfo("Name", "Sigma Delta Tau")
    elif(code.upper() == "GVD"):
        tkinter.messagebox.showinfo("Name", "Zeta Tau Alpha")
    elif(code.upper() == "GVE"):
        tkinter.messagebox.showinfo("Name", "Delta Chi")
    elif(code.upper() == "GVF"):
        tkinter.messagebox.showinfo("Name", "Sigma Chi")
    elif(code.upper() == "GVG"):
        tkinter.messagebox.showinfo("Name", "Delta Gamma")
    elif(code.upper() == "GVH"):
        tkinter.messagebox.showinfo("Name", "Delta Delta Delta")
    elif(code.upper() == "GVI"):
        tkinter.messagebox.showinfo("Name", "Sigma Nu")
    elif(code.upper() == "GVJ"):
        tkinter.messagebox.showinfo("Name", "Zeta Beta Tau")
    elif(code.upper() == "GVK"):
        tkinter.messagebox.showinfo("Name", "Chi Omega")
    elif(code.upper() == "GVL"):
        tkinter.messagebox.showinfo("Name", "Sigma Phi Epsilon")
    elif(code.upper() == "GVM"):
        tkinter.messagebox.showinfo("Name", "Kappa Delta")
    elif(code.upper() == "GVN"):
        tkinter.messagebox.showinfo("Name", "Alpha Omicron Pi")
    else:
        tkinter.messagebox.showinfo("Name", "Invalid building code.")
    return

root = Tk()

canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tkinter.PhotoImage(file='usf.png')
background_label = tkinter.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tkinter.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.0, relwidth=1, relheight=0.1, anchor='n')

entry = tkinter.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tkinter.Button(frame, text="Get Name", font=40, command=lambda: getBuildingName(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()
