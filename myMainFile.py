from tkinter import Tk, StringVar, ttk
from tkinter import *
from tkinter import messagebox
import time;
import datetime

root = Tk()
root.title("Attendance Register")
root.geometry('1350x650+0+0')
root.configure(background = "black")

############################Frames###############################################

LeftMayFrame = Frame(root, width =1000, height = 650, bd = 8, relief = "raise")
LeftMayFrame.pack(side = LEFT)
RightMayFrame = Frame(root, width =350, height = 650, bd = 8, relief = "raise")
RightMayFrame.pack(side = RIGHT)

LeftMayFrame1 = Frame(LeftMayFrame, width =1000, height = 100, bd = 8, relief = "raise")
LeftMayFrame1.pack(side = TOP)
LeftMayFrame2 = Frame(LeftMayFrame, width =1000, height = 550, bd = 8, relief = "raise")
LeftMayFrame2.pack(side = TOP)

RightMayFrame1 = Frame(RightMayFrame, width =350, height = 215, bd = 8, relief = "raise")
RightMayFrame1.pack(side = TOP)
RightMayFrame2 = Frame(RightMayFrame, width =350, height = 415, bd = 8, relief = "raise")
RightMayFrame2.pack(side = TOP)

#################################IMAGES############################################

cont1 = Canvas(RightMayFrame2, width = 350, height = 425, bg = "black")
cont1.grid(row = 0,column = 0)
img1 = PhotoImage(file = "1.png")
cont1.create_image(200, 200, image = img1)

cont = Canvas(RightMayFrame1, width = 400, height = 215, bg = "black")
cont.grid(row = 0,column = 0)
img2 = PhotoImage(file = "2.png")
cont.create_image(150, 100, image = img2)

##################################VARIABLES########################################

DateofOrder = StringVar()

value0 = StringVar()
value1 = StringVar()
value2 = StringVar()
value3 = StringVar()
value4 = StringVar()
value5 = StringVar()
value6 = StringVar()
value7 = StringVar()
value8 = StringVar()
value9 = StringVar()
value10 = StringVar()
value11 = StringVar()
value12 = StringVar()

def Fill():
    if value0.get() == 'P':
        value0.set("P")
        value1.set("P")
        value2.set("P")
        value3.set("P")
        value4.set("P")
        value5.set("P")
        value6.set("P")
        value7.set("P")
        value8.set("P")
        value9.set("P")
        value10.set("P")
    elif value0.get() == 'A':
        value0.set("A")
        value1.set("A")
        value2.set("A")
        value3.set("A")
        value4.set("A")
        value5.set("A")
        value6.set("A")
        value7.set("A")
        value8.set("A")
        value9.set("A")
        value10.set("A")
    elif value0.get() == 'L':
        value0.set("L")
        value1.set("L")
        value2.set("L")
        value3.set("L")
        value4.set("L")
        value5.set("L")
        value6.set("L")
        value7.set("L")
        value8.set("L")
        value9.set("L")
        value10.set("L")
    elif value0.get() == 'DL':
        value0.set("DL")
        value1.set("DL")
        value2.set("DL")
        value3.set("DL")
        value4.set("DL")
        value5.set("DL")
        value6.set("DL")
        value7.set("DL")
        value8.set("DL")
        value9.set("DL")
        value10.set("DL")
    elif value0.get() == 'ML':
        value0.set("ML")
        value1.set("ML")
        value2.set("ML")
        value3.set("ML")
        value4.set("ML")
        value5.set("ML")
        value6.set("ML")
        value7.set("ML")
        value8.set("ML")
        value9.set("ML")
        value10.set("ML")

def Reset():
    value0.set("")
    value1.set("")
    value2.set("")
    value3.set("")
    value4.set("")
    value5.set("")
    value6.set("")
    value7.set("")
    value8.set("")
    value9.set("")
    value10.set("")

def qExit():
    qExit = messagebox.askyesno("Exit System","Do You Want To Quit?")
    if qExit > 0:
        root.destroy()
        return

#########################COMPONENTS#################################################

DateofOrder.set(time.strftime("%d/%m/%y"))

###########################LeftMayFrame1###########################################

lblNo = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), text = "No.", bd = 16)
lblNo.grid(row = 0, column = 0, sticky = W)
lblStudentNo = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), text = "Student No.", bd = 16)
lblStudentNo.grid(row = 0, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), text = "Student Name", bd = 16)
lblStudentName.grid(row = 0, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), text = "Course Code", bd = 16)
lblCourseCode.grid(row = 0, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame1, textvariable = value0, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 0, column = 4)

btnFill = Button(LeftMayFrame1, text = 'Fill', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1, command = Fill).grid(row = 0, column = 5)
btnReset = Button(LeftMayFrame1, text = 'Reset', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1, command = Reset).grid(row = 0, column = 6)
btnExit = Button(LeftMayFrame1, text = 'Exit', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1, command=qExit).grid(row = 0, column = 7)

lblDateofOrder = Label(LeftMayFrame1, font = ('arial', 10, 'bold'), textvariable = DateofOrder, padx = 2,
                    pady = 2, bd = 2, fg = 'black', bg = 'white', relief = 'sunken')
lblDateofOrder.grid(row = 0, column = 8, sticky = W)

###########################LeftMayFrame2 Row 1###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "1.", bd = 16)
lblNo.grid(row = 0, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "1.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 0, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Sagar", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 0, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 0, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value1, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 0, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 0, column = 8)

###########################LeftMayFrame2 Row 2###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "2.", bd = 16)
lblNo.grid(row = 2, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "2.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 2, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Rohan", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 2, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 2, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value2, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 2, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 2, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 2, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 2, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 2, column = 8)

###########################LeftMayFrame2 Row 3###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "3.", bd = 16)
lblNo.grid(row = 3, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "3.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 3, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Ankush", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 3, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 3, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value3, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 3, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 3, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 3, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 3, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 3, column = 8)

###########################LeftMayFrame2 Row 4###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "4.", bd = 16)
lblNo.grid(row = 4, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "4.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 4, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Shubham", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 4, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 4, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value4, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 4, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 4, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 4, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 4, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 4, column = 8)

###########################LeftMayFrame2 Row 5###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "5.", bd = 16)
lblNo.grid(row = 5, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "5.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 5, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Samuel", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 5, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 5, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value5, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 5, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 5, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 5, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 5, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 5, column = 8)

###########################LeftMayFrame2 Row 6###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "6.", bd = 16)
lblNo.grid(row = 6, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "6.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 6, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Aditi", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 6, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 6, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value6, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 6, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 6, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 6, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 6, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 6, column = 8)
###########################LeftMayFrame2 Row 7###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "7.", bd = 16)
lblNo.grid(row = 7, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "7.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 7, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Pratibha", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 7, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 7, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value7, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 7, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 7, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 7, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 7, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 7, column = 8)
###########################LeftMayFrame2 Row 8###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "8.", bd = 16)
lblNo.grid(row = 8, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "8.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 8, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Sumit", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 8, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 8, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value8, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 8, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 8, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 8, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 8, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 8, column = 8)

###########################LeftMayFrame2 Row 9###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "9.", bd = 16)
lblNo.grid(row = 9, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "9.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 9, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Neha", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 9, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 9, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value9, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 9, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 9, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 9, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 9, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 9, column = 8)
###########################LeftMayFrame2 Row 10###########################################

lblNo = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "10.", bd = 16)
lblNo.grid(row = 10, column = 0, sticky = W)
lblStudentNo1 = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "10.", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 18)
lblStudentNo1.grid(row = 10, column = 1, sticky = W)
lblStudentName = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "Khushboo", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblStudentName.grid(row = 10, column = 2, sticky = W)
lblCourseCode = Label(LeftMayFrame2, font = ('arial', 10, 'bold'), text = "MCA LEET", padx = 2,
                    pady = 2, bd = 2, fg = 'black', width = 12)
lblCourseCode.grid(row = 10, column = 3, sticky = W)

box = ttk.Combobox(LeftMayFrame2, textvariable = value10, state = 'readonly')
box['values'] = (' ', 'P', 'L', 'ML', 'A', 'DL')
box.current(0)
box.grid(row = 10, column = 4)

btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 10, column = 5)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 10, column = 6)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 10, column = 7)
btnSpace = Button(LeftMayFrame2, text = '', padx = 2, pady = 2, bd = 2, fg = 'black',
                    font = ('arial', 10, 'bold'), width = 12, height = 1).grid(row = 10, column = 8)

root.mainloop()
