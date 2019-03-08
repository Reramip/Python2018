from tkinter import *

def changeColor():
    if btnCalculate["fg"] == "blue":
        btnCalculate["fg"] = "red"
    else:
        btnCalculate["fg"] ="blue"
    if entName["fg"] == "orange":
        entName["fg"] = "brown"
    else:
        entName["fg"] = "orange"

def convertToUpperCase(event):
    conOFentName.set(conOFentName.get().upper())

def convertToLowerCase(event):
    conOFentName.set(conOFentName.get().lower())

def changeBackgroundColor(event):
    lstColors["bg"] = lstColors.get(lstColors.curselection())

def sortItems(event):
    L.sort()
    conOFlstColors.set(tuple(L))


window = Tk()

##标题
window.title("abc")

##标签控件
lblPrincipal = Label(window, text="Principal:")
lblPrincipal.grid(padx=30, pady=0)

##按钮控件
btnCalculate = Button(window, text="Surprise!", fg="blue", bg="light grey", command=changeColor)
btnCalculate.grid(padx=30, pady=5, ipadx=20, ipady=10)

##输入控件
conOFentName = StringVar()
entName = Entry(window, width=20, fg="orange", textvariable=conOFentName)
entName.grid(padx=50, pady=5)
entName.bind("<Button-1>", convertToLowerCase)
entName.bind("<Button-3>", convertToUpperCase)

##只读输入控件
conOFentOutput = StringVar()
conOFentOutput.set("Hello world!")
entOutput = Entry(window, width=20, state="readonly", textvariable=conOFentOutput)
entOutput.grid(padx=50, pady=5)

##列表框控件
L = ["white", "yellow", "light blue", "pink"]
conOFlstColors = StringVar()
lstColors = Listbox(window, width=10, height=5, listvariable=conOFlstColors)
lstColors.grid(padx=100, pady=15)
conOFlstColors.set(tuple(L))
lstColors.bind("<<ListboxSelect>>", changeBackgroundColor)
lstColors.bind("<Button-3>", sortItems)

##滚动条控件
yscroll = Scrollbar(window, orient=VERTICAL)
yscroll.grid(padx=110, pady=15)


window.mainloop()