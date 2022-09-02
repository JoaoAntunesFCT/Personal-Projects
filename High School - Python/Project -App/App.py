#Import
from tkinter import *
root = Tk()
calc = Toplevel()
intel = Toplevel()
tino1 = Toplevel()
tino2 = Toplevel()
#Functions
#Abrir Calculadora
def open():
    root.withdraw()
    calc.deiconify()
    global bck
    bck = "Calculator"
#Abrir Info
def info():
    root.withdraw()
    intel.deiconify()
    global bck 
    bck = "Information"
#Abrir 3in1 (Introdução)
def open_tino1():
    root.withdraw()
    tino1.deiconify()
    global bck
    bck = "Tino1"
#Abrir 3in1 (Cálculo)
def open_tino2():
    tino1.withdraw()
    tino2.deiconify()
    global bck
    bck = "Tino2"
#Retroceder Entre Tinos
def open_tino3():
    tino2.withdraw()
    tino1.deiconify()
#Botões de 3in1
def clear():
    Ecra1.delete(0, END)
    Ecra2.delete(0, END)
    Ecra3.delete(0, END)
    Ecra4.delete(0, END)      
def calculate():
    Ecra4.delete(0, END)
    Ecra4.insert(0, int(Ecra3.get()) * int(Ecra2.get()) / int(Ecra1.get()))
#Botão de retroceder em todas as ocasiões
def back():
    if bck == "Calculator":
        calc.withdraw()
        root.deiconify()
    if bck == "Information":
        intel.withdraw()
        root.deiconify()
    if bck == "Tino1":
        tino1.withdraw()
        root.deiconify()
    if bck == "Tino2":
        tino2.withdraw()
        root.deiconify()

#Buttons definitions (Calculator)
def button_click(number):
    # e.delete(0,END)
    atual = Ecra.get() #inverter a ordem
    Ecra.delete(0, END) #para não somar sempre que clicarmos no próximo
    Ecra.insert(0,str(atual) + str(number))
    
def button_clear():
     Ecra.delete(0, END)
   
def button_add():
    # first_number = Ecra.get()
    global f_number
    global math
    math = "addition"
    f_number = int(first_number)
    Ecra.delete(0, END)
    
def button_subtract():
    first_number = Ecra.get()
    global f_number
    global math
    math = "subtraction"
    f_number = int(first_number)
    Ecra.delete(0, END)

def button_multiplier():
    first_number = Ecra.get()
    global f_number
    global math
    math = "multiplication"
    f_number = int(first_number)
    Ecra.delete(0, END)

def button_divide():
    first_number = Ecra.get()
    global f_number
    global math
    math = "division"
    f_number = int(first_number)
    Ecra.delete(0, END)

def button_module():
    first_number = Ecra.get()
    global f_number
    global math
    math = "module"
    f_number = int(first_number)
    Ecra.delete(0, END)
    
def button_equal():
    s_number = Ecra.get()
    Ecra.delete(0, END)
    if math == "addition":
        Ecra.insert(0, f_number + int(s_number))
    if math == "subtraction":
        Ecra.insert(0, f_number - int(s_number))
    if math == "multiplication":
        Ecra.insert(0, f_number * int(s_number))
    if math == "division":
        Ecra.insert(0, f_number / int(s_number))
    if math == "module":
        Ecra.insert(0, f_number % int(s_number))
    
#Button Retroceder da calculadora
NumberJ = Button(calc,text="Back",padx=15,pady=5,fg="green",command=back)
#Ecrã de Resultados
Ecra = Entry(calc, width=15,borderwidth=5,font=("Helvetica", 18))
Ecra.grid(row=2,column=4)
#Number Buttons (Calculator)
Number1 = Button(calc,text=1,padx=40,pady=20,fg="blue",command=lambda: button_click(1))
Number2 = Button(calc,text=2,padx=40,pady=20,fg="blue",command=lambda: button_click(2))
Number3 = Button(calc,text=3,padx=40,pady=20,fg="blue",command=lambda: button_click(3))
Number4 = Button(calc,text=4,padx=40,pady=20,fg="blue",command=lambda: button_click(4))
Number5 = Button(calc,text=5,padx=40,pady=20,fg="blue",command=lambda: button_click(5))
Number6 = Button(calc,text=6,padx=40,pady=20,fg="blue",command=lambda: button_click(6))
Number7 = Button(calc,text=7,padx=40,pady=20,fg="blue",command=lambda: button_click(7))
Number8 = Button(calc,text=8,padx=40,pady=20,fg="blue",command=lambda: button_click(8))
Number9 = Button(calc,text=9,padx=40,pady=20,fg="blue",command=lambda: button_click(9))
Number0 = Button(calc,text=0,padx=40,pady=20,fg="blue",command=lambda: button_click(0))
#Symbols (+,-,x,/,%,calculate, Clear)
NumberP = Button(calc,text="+",padx=39,pady=20,fg="blue",command=button_add)
NumberM = Button(calc,text="-",padx=40.50,pady=20,fg="blue",command=button_subtract)
NumberX = Button(calc,text="x",padx=40,pady=20,fg="blue",command=button_multiplier)
NumberD = Button(calc,text="/",padx=40,pady=20,fg="blue",command=button_divide)
NumberC = Button(calc,text="%",padx=38,pady=20,fg="blue",command=button_module)
NumberR = Button(calc,text="Calculate",padx=80,pady=20,fg="Orange",command=button_equal)
NumberV = Button(calc,text="Clear",padx=40,pady=10,command=button_clear)
#Number Buttons Location
Number1.grid(row=1,column=1)
Number2.grid(row=1,column=2)
Number3.grid(row=1,column=3)
Number4.grid(row=2,column=1)
Number5.grid(row=2,column=2)
Number6.grid(row=2,column=3)
Number7.grid(row=3,column=1)
Number8.grid(row=3,column=2)
Number9.grid(row=3,column=3)
Number0.grid(row=4,column=1)
NumberP.grid(row=4,column=2)
NumberM.grid(row=4,column=3)
NumberX.grid(row=5,column=1)
NumberD.grid(row=5,column=2)
NumberC.grid(row=5,column=3)
NumberR.grid(row=5,column=4)
NumberV.grid(row=4,column=4)
NumberJ.grid(row=1,column=4)        
#Window, Names, Size and Position
root.title("Application")
lbl = Label(root,text="Welcome to my App")
lbl.grid(row=1,column=2)
root.geometry("303x130+920+530")
root.resizable(False, False)
calc.title("Calculator")
calc.geometry("510x322+920+530")
calc.resizable(False, False)
calc.withdraw()
intel.title("Informations")
lbl1 = Label(intel,text="This application was created and developed by:")
lbl2 = Label(intel,text="João Antunes",fg="blue")
lbl3 = Label(intel,text="2021")
lbl1.grid(row=1,column=2)
lbl2.grid(row=2,column=2)
lbl3.grid(row=4,column=2)
intel.geometry("253x130+920+530")
intel.resizable(False, False)
intel.withdraw()
tino1.title("3-1 Intro")
lbl4 = Label(tino1,text="Enter the digits in the boxes and the math will do the rest")
lbl5 = Label(tino1,text="(Used for direct or inverse proportionality purposes).")
lbl4.grid(row=1,column=1,columnspan=2)
lbl5.grid(row=2,column=1,columnspan=2)
tino1.geometry("310x85+920+530")
tino1.resizable(False, False)
tino1.withdraw()
tino2.title("3-1 Math")
lbl6 = Label(tino2,text="is for")
lbl7 = Label(tino2,text="like,")
lbl8 = Label(tino2,text="is for")
lbl9 = Label(tino2,text= "X")
lbl10 = Label(tino2,text= "X =")
lbl6.grid(row=1,column=2)
lbl7.grid(row=2,column=2)
lbl8.grid(row=4,column=2)
lbl9.grid(row=4,column=3)
lbl10.grid(row=2,column=8)
tino2.geometry("480x140+920+530")
tino2.resizable(False, False)
tino2.withdraw()
#Botões do ecrã principal
NumberK = Button(root,text="Calculator",padx=15,pady=15,fg="green", command=open)
NumberK.grid(row=2,column=1)
NumberK = Button(root,text="Graph",padx=26,pady=15,fg="green")
NumberK.grid(row=3,column=1)
NumberK = Button(root,text="3-1",padx=33,pady=15,fg="green", command=open_tino1)
NumberK.grid(row=3,column=2)
NumberK = Button(root,text="Oscilloscope",padx=8,pady=15,fg="green")
NumberK.grid(row=2,column=2)
NumberK = Button(root,text="Info",padx=32,pady=3,fg="blue",command=info)
NumberK.grid(row=2,column=3)
NumberK = Button(root,text="Exit",padx=32,pady=3,fg="red", command=root.destroy)
NumberK.grid(row=3,column=3)
#Botão do Information
NumberM = Button (intel,text="Back",padx=15,pady=5,fg="green",command=back)
NumberM.grid(row=3,column=2)
#Botões de 3in1 Intro
NumberI = Button (tino1,text="Back",padx=15,pady=5,fg="green",command=back)
NumberI.grid(row=3,column=1)
NumberW = Button (tino1,text="Ok",padx=15,pady=5,fg="orange",command=open_tino2)
NumberW.grid(row=3,column=2)
#Botões de 3in1 Cálculo
NumberC = Button(tino2,text="Calculate",padx=40,pady=5,fg="Orange",command=calculate)
NumberC.grid(row=6,column=9)
NumberZ = Button (tino2,text="Back To Hub",padx=31,pady=5,fg="green",command=back)
NumberZ.grid(row=6,column=1)
NumberZ = Button (tino2,text="Return",padx=47,pady=5,fg="green",command=open_tino3)
NumberZ.grid(row=6,column=3)
NumberT = Button (tino2,text="Clear",padx=25,pady=5,command=clear)
NumberT.grid(row=4,column=9)
#Ecrãs de 3in1 Cálculo
Ecra1 = Entry(tino2, width=12,borderwidth=2,font=("Helvetica", 15))
Ecra1.grid(row=1,column=1)
Ecra2 = Entry(tino2, width=12,borderwidth=2,font=("Helvetica", 15))
Ecra2.grid(row=1,column=3, columnspan=3)
Ecra3 = Entry(tino2, width=12,borderwidth=2,font=("Helvetica", 15))
Ecra3.grid(row=3,column=1, rowspan=3)
Ecra4 = Entry(tino2, width=12,borderwidth=5,font=("Helvetica", 15))
Ecra4.grid(row=2,column=9)
root.mainloop()


