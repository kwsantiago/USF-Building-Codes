from tkinter import *
import tkinter.messagebox, tkinter.simpledialog
import webbrowser

HEIGHT = 400
WIDTH = 400

def getBuildingName(code):
    if(code.upper() == "RBE"):
        tkinter.messagebox.showinfo("Name", "Beta")
    elif(code.upper() == "BETA"):
        tkinter.messagebox.showinfo("Code", "RBE")
    elif(code.upper() == "RBC"):
        tkinter.messagebox.showinfo("Name", "Castor")
    elif(code.upper() == "CASTOR"):
        tkinter.messagebox.showinfo("Code", "RBC")
    elif(code.upper() == "RKO"):
        tkinter.messagebox.showinfo("Name", "Kosove")
    elif(code.upper() == "KOSOVE"):
        tkinter.messagebox.showinfo("Code", "RKO")
    elif(code.upper() == "RJH"):
        tkinter.messagebox.showinfo("Name", "Juniper")
    elif(code.upper() == "JUNIPER"):
        tkinter.messagebox.showinfo("Code", "RJH")
    elif(code.upper() == "RPH"):
        tkinter.messagebox.showinfo("Name", "Poplar")
    elif(code.upper() == "POPLAR"):
        tkinter.messagebox.showinfo("Code", "RPH")
    elif(code.upper() == "MAA"):
        tkinter.messagebox.showinfo("Name", "Magnolia A")
    elif(code.upper() == "MAGNOLIA A"):
        tkinter.messagebox.showinfo("Code", "MAA")
    elif(code.upper() == "MAB"):
        tkinter.messagebox.showinfo("Name", "Magnolia B")
    elif(code.upper() == "MAGNOLIA B"):
        tkinter.messagebox.showinfo("Code", "MAB")
    elif(code.upper() == "MAC"):
        tkinter.messagebox.showinfo("Name", "Magnolia C")
    elif(code.upper() == "MAGNOLIA C"):
        tkinter.messagebox.showinfo("Code", "MAC")
    elif(code.upper() == "MAD"):
        tkinter.messagebox.showinfo("Name", "Magnolia D")
    elif(code.upper() == "MAGNOLIA D"):
        tkinter.messagebox.showinfo("Code", "MAD")
    elif(code.upper() == "MAE"):
        tkinter.messagebox.showinfo("Name", "Magnolia E")
    elif(code.upper() == "MAGNOLIA E"):
        tkinter.messagebox.showinfo("Code", "MAE")
    elif(code.upper() == "MAF"):
        tkinter.messagebox.showinfo("Name", "Magnolia F")
    elif(code.upper() == "MAGNOLIA F"):
        tkinter.messagebox.showinfo("Code", "MAF")
    elif(code.upper() == "MAG"):
        tkinter.messagebox.showinfo("Name", "Magnolia G")
    elif(code.upper() == "MAGNOLIA G"):
        tkinter.messagebox.showinfo("Code", "MAG")
    elif(code.upper() == "HAA"):
        tkinter.messagebox.showinfo("Name", "Holly A")
    elif(code.upper() == "HOLLY A"):
        tkinter.messagebox.showinfo("Code", "HAA")
    elif(code.upper() == "HAB"):
        tkinter.messagebox.showinfo("Name", "Holly B")
    elif(code.upper() == "HOLLY B"):
        tkinter.messagebox.showinfo("Code", "HAB")
    elif(code.upper() == "HAC"):
        tkinter.messagebox.showinfo("Name", "Holly C")
    elif(code.upper() == "HOLLY C"):
        tkinter.messagebox.showinfo("Code", "HAC")
    elif(code.upper() == "HAD"):
        tkinter.messagebox.showinfo("Name", "Holly D")
    elif(code.upper() == "HOLLY D"):
        tkinter.messagebox.showinfo("Code", "HAD")
    elif(code.upper() == "HAE"):
        tkinter.messagebox.showinfo("Name", "Holly E")
    elif(code.upper() == "HOLLY E"):
        tkinter.messagebox.showinfo("Code", "HAE")
    elif(code.upper() == "HAF"):
        tkinter.messagebox.showinfo("Name", "Holly F")
    elif(code.upper() == "HOLLY F"):
        tkinter.messagebox.showinfo("Code", "HAF")
    elif(code.upper() == "HAG"):
        tkinter.messagebox.showinfo("Name", "Holly G")
    elif(code.upper() == "HOLLY G"):
        tkinter.messagebox.showinfo("Code", "HAG")
    elif(code.upper() == "RCA"):
        tkinter.messagebox.showinfo("Name", "Cypress A (Suites)")
    elif(code.upper() == "CYPRESS A" or code.upper() == "CYPRESS A (SUITES)"):
        tkinter.messagebox.showinfo("Code", "RCA")
    elif(code.upper() == "RCB"):
        tkinter.messagebox.showinfo("Name", "Cypress B (Suites)")
    elif(code.upper() == "CYPRESS B" or code.upper() == "CYPRESS B (SUITES)"):
        tkinter.messagebox.showinfo("Code", "RCB")
    elif(code.upper() == "RCC"):
        tkinter.messagebox.showinfo("Name", "Cypress C (Apartments)")
    elif(code.upper() == "CYPRESS C" or code.upper() == "CYPRESS C (SUITES)"):
        tkinter.messagebox.showinfo("Code", "RCC")
    elif(code.upper() == "RCD"):
        tkinter.messagebox.showinfo("Name", "Cypress D (Apartments)")
    elif(code.upper() == "CYPRESS D" or code.upper() == "CYPRESS D (SUITES)"):
        tkinter.messagebox.showinfo("Code", "RCD")
    elif(code.upper() == "MPA"):
        tkinter.messagebox.showinfo("Name", "Maple A")
    elif(code.upper() == "MAPLE A"):
        tkinter.messagebox.showinfo("Code", "MPA")
    elif(code.upper() == "MPB"):
        tkinter.messagebox.showinfo("Name", "Maple B")
    elif(code.upper() == "MAPLE B"):
        tkinter.messagebox.showinfo("Code", "MPB")
    elif(code.upper() == "RBN"):
        tkinter.messagebox.showinfo("Name", "Beacon")
    elif(code.upper() == "BEACON"):
        tkinter.messagebox.showinfo("Code", "RBN")
    elif(code.upper() == "RSU"):
        tkinter.messagebox.showinfo("Name", "Summit")
    elif(code.upper() == "SUMMIT"):
        tkinter.messagebox.showinfo("Code", "RSU")
    elif(code.upper() == "RPN"):
        tkinter.messagebox.showinfo("Name", "Pinnacle")
    elif(code.upper() == "PINNACLE"):
        tkinter.messagebox.showinfo("Code", "RPN")
    elif(code.upper() == "REN"):
        tkinter.messagebox.showinfo("Name", "Endeavor")
    elif(code.upper() == "ENDEAVOR"):
        tkinter.messagebox.showinfo("Code", "REN")
    elif(code.upper() == "RHN"):
        tkinter.messagebox.showinfo("Name", "Horizon")
    elif(code.upper() == "HORIZON"):
        tkinter.messagebox.showinfo("Code", "RHN")
    elif(code.upper() == "GVA"):
        tkinter.messagebox.showinfo("Name", "Alpa Delta Pi")
    elif(code.upper() == "ALPHA DELTA PI"):
        tkinter.messagebox.showinfo("Code", "GVA")
    elif(code.upper() == "GVB"):
        tkinter.messagebox.showinfo("Name", "Gamma Phi Beta")
    elif(code.upper() == "GAMMA PHI BETA"):
        tkinter.messagebox.showinfo("Code", "GVB")
    elif(code.upper() == "GVC"):
        tkinter.messagebox.showinfo("Name", "Sigma Delta Tau")
    elif(code.upper() == "SIGMA DELTA TAU"):
        tkinter.messagebox.showinfo("Code", "GVC")
    elif(code.upper() == "GVD"):
        tkinter.messagebox.showinfo("Name", "Zeta Tau Alpha")
    elif(code.upper() == "ZETA TAU ALPHA"):
        tkinter.messagebox.showinfo("Code", "GVD")
    elif(code.upper() == "GVE"):
        tkinter.messagebox.showinfo("Name", "Delta Chi")
    elif(code.upper() == "DELTA CHI"):
        tkinter.messagebox.showinfo("Code", "GVE")
    elif(code.upper() == "GVF"):
        tkinter.messagebox.showinfo("Name", "Sigma Chi")
    elif(code.upper() == "SIGMA CHI"):
        tkinter.messagebox.showinfo("Code", "GVF")
    elif(code.upper() == "GVG"):
        tkinter.messagebox.showinfo("Name", "Delta Gamma")
    elif(code.upper() == "DELTA GAMMA"):
        tkinter.messagebox.showinfo("Code", "GVG")
    elif(code.upper() == "GVH"):
        tkinter.messagebox.showinfo("Name", "Delta Delta Delta")
    elif(code.upper() == "DELTA DELTA DELTA"):
        tkinter.messagebox.showinfo("Code", "GVH")
    elif(code.upper() == "GVI"):
        tkinter.messagebox.showinfo("Name", "Sigma Nu")
    elif(code.upper() == "SIGMA NU"):
        tkinter.messagebox.showinfo("Code", "GVI")
    elif(code.upper() == "GVJ"):
        tkinter.messagebox.showinfo("Name", "Zeta Beta Tau")
    elif(code.upper() == "ZETA BETA TAU"):
        tkinter.messagebox.showinfo("Code", "GVJ")
    elif(code.upper() == "GVK"):
        tkinter.messagebox.showinfo("Name", "Chi Omega")
    elif(code.upper() == "CHI OMEGA"):
        tkinter.messagebox.showinfo("Code", "GVK")
    elif(code.upper() == "GVL"):
        tkinter.messagebox.showinfo("Name", "Sigma Phi Epsilon")
    elif(code.upper() == "SIGMA PHI EPSILON"):
        tkinter.messagebox.showinfo("Code", "GVL")
    elif(code.upper() == "GVM"):
        tkinter.messagebox.showinfo("Name", "Kappa Delta")
    elif(code.upper() == "KAPPA DELTA"):
        tkinter.messagebox.showinfo("Code", "GVM")
    elif(code.upper() == "GVN"):
        tkinter.messagebox.showinfo("Name", "Alpha Omicron Pi")
    elif(code.upper() == "ALPHA OMICRON PI"):
        tkinter.messagebox.showinfo("Code", "GVN")
    else:
        tkinter.messagebox.showinfo("Name", "Invalid building code.")
    return

def openMercury():
    webbrowser.open('https://jupiter.forest.usf.edu/')

def openVillageCodes():
    webbrowser.open('https://usflearn.instructure.com/courses/1143753/files?preview=91364484')

def openNorthSouthCodes():
    webbrowser.open('https://usflearn.instructure.com/courses/1143753/files?preview=91091270')

def openHelp():
    webbrowser.open('https://github.com/kwsantiago/USF-Building-Converter-GUI')

def menu(root):
    menu = Menu(root)
    root.config(menu=menu)

    menu.add_command(label="Help", command=lambda: openHelp().pack())

def canvas(root):
    canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

def initUI():
    root = Tk()
    root.title('Building Code to Name Converter - By Kyle Santiago')
    root.iconbitmap('usf.ico')

    menu(root)
    canvas(root)

    background_image = tkinter.PhotoImage(file='usf.gif')
    background_label = tkinter.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    frame = tkinter.Frame(root, bg='#006649', bd=5)
    frame.place(relx=0.5, rely=0.0, relwidth=1, relheight=0.1, anchor='n')

    entry = tkinter.Entry(frame, font=40)
    entry.bind("<Return>", lambda event: getBuildingName(entry.get()))
    entry.place(relwidth=0.65, relheight=1)

    answerButton = tkinter.Button(frame, text="Get Answer", font=40, command=lambda: getBuildingName(entry.get()))
    answerButton.place(relx=0.7, relheight=1, relwidth=0.3)

    temp = tkinter.Button(background_label, text="Mercury", font=40, command=lambda: openMercury().pack)
    temp.place(relx=0.01, rely=0.93, relheight=0.07, relwidth=0.225)

    temp = tkinter.Button(background_label, text="Village Codes", font=40, command=lambda: openVillageCodes())
    temp.place(relx=0.243, rely=0.93, relheight=0.07, relwidth=0.35)

    temp = tkinter.Button(background_label, text="Other Codes", font=40, command=lambda: openNorthSouthCodes())
    temp.place(relx=0.6, rely=0.93, relheight=0.07, relwidth=0.4)

    root.mainloop()

def main():
    initUI()

main()
