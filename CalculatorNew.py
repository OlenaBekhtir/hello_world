# Импортируем библиотеку tkinter
from tkinter import *

# Создаем новое окно c названием и заданными размерами
root = Tk()
root.title("Калькулятор")
root.geometry("420x300")
root.update()

# создаем переменную, которую будем записывать в строку калькулятора
calc = StringVar()
calc.set("")

# создаем строку калькулятора, в которой будут отображаться введенные цифры и результаты расчета
label = Label(textvariable=calc, background="#828", foreground="#ccc", font=("Arial", 22, "bold italic"),
   padx="100", pady="15")

# Создаем список функций, которые будут "включать" кнопки калькулятора

def onePressed():
    global calc
    calc.set(calc.get() + "1")

def twoPressed():
    global calc
    calc.set(calc.get() + "2")

def threePressed():
    global calc
    calc.set(calc.get() + "3")

def fourPressed():
    global calc
    calc.set(calc.get() + "4")

def fivePressed():
    global calc
    calc.set(calc.get() + "5")

def sixPressed():
    global calc
    calc.set(calc.get() + "6")

def sevenPressed():
    global calc
    calc.set(calc.get() + "7")

def eigthPressed():
    global calc
    calc.set(calc.get() + "8")

def ninePressed():
    global calc
    calc.set(calc.get() + "9")

def zeroPressed():
    global calc
    calc.set(calc.get() + "0")

def plusPressed():
    global calc
    calc.set(calc.get() + "+")

def minusPressed():
    global calc
    calc.set(calc.get() + "-")

def multyplusPressed():
    global calc
    calc.set(calc.get() + "*")


def divisionPressed():
    global calc
    calc.set(calc.get() + "/")

def equalPressed():
    global calc
    result = eval(calc.get())
    calc.set('=' + ' ' + str(result))

def clearPressed():
    calc.set("")


# Создаем кнопки калькулятора

button0 = Button(
    text="0",
    command=zeroPressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button1 = Button(
    text="1",
    command=onePressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button2 = Button(
    text="2",
    command=twoPressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button3 = Button(
    text="3",
    command=threePressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button4 = Button(
    text="4",
    command=fourPressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button5 = Button(
    text="5",
    command=fivePressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button6 = Button(
    text="6",
    command=sixPressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button7 = Button(
    text="7",
    command=sevenPressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button8 = Button(
    text="8",
    command=eigthPressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button9 = Button(
    text="9",
    command=ninePressed,
    background="#7c8",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button_plus = Button(
    text="+",
    command=plusPressed,
    background="#28b",
    foreground="#ccc",
    font=("Arial", 20, "bold"),
    padx="15",
    pady="10"
)
button_minus = Button(
    text="-",
    command=minusPressed,
    background="#28b",
    foreground="#ccc",
    font=("Arial", 20, "bold"),
    padx="19",
    pady="10"
)
button_multiplus = Button(
    text="*",
    command=multyplusPressed,
    background="#28b",
    foreground="#ccc",
    font=("Arial", 20, "bold"),
    padx="19",
    pady="10"
)
button_division = Button(
    text="/",
    command=divisionPressed,
    background="#28b",
    foreground="#ccc",
    font=("Arial", 20, "bold"),
    padx="21",
    pady="10"
)
button_result = Button(
    text="=",
    command=equalPressed,
    background="#ed1",
    foreground="#555",
    font=("Arial", 20, "bold"),
    padx="17",
    pady="10"
)
button_clean = Button(
    text="C",
    command=clearPressed,
    padx="10",
    pady="84",
    background="#f80",
    foreground="#ccc",
    font=("Arial", 20, "bold"),
)

# Размещаем кнопки калькулятора в окне
# команда sticky "приклеивает" кнопки калькулятора друг к другу
label.grid(row=0, column=0, columnspan=7, sticky="ew")
button0.grid(row=1, column=4, sticky="ew")
button1.grid(row=1, column=1, sticky="ew")
button2.grid(row=1, column=2, sticky="ew")
button3.grid(row=1, column=3, sticky="ew")
button4.grid(row=2, column=1, sticky="ew")
button5.grid(row=2, column=2, sticky="ew")
button6.grid(row=2, column=3, sticky="ew")
button7.grid(row=3, column=1, sticky="ew")
button8.grid(row=3, column=2, sticky="ew")
button9.grid(row=3, column=3, sticky="ew")
button_plus.grid(row=2, column=4, sticky="ew")
button_minus.grid(row=3, column=4, sticky="ew")
button_multiplus.grid(row=1, column=5, sticky="ew")
button_division.grid(row=2, column=5, sticky="ew")
button_result.grid(row=3, column=5, sticky="ew")
button_clean.grid(row=1, column=6, rowspan=3, sticky="ew")

# Включаем постоянную отрисовку окна
root.mainloop()
