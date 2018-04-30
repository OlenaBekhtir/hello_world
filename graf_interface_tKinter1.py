from tkinter import *
# Создаем новое окно
root = Tk()
# Название окна
root.title("Моя первая графическая программа")
# Указываем размер окна в пикселях (ширина х высота)
root.geometry("400x300")

button_text = StringVar()
button_text.set("Это старый текст!")

def button_func():
    global button_text
    if button_text.get() == "Это старый текст!":
        button_text.set("Это новый текст!")
    else:
        button_text.set("Это старый текст!")

# Создаем кнопку
hello_button = Button(
    textvariable=button_text,
    background="#555",
    foreground="#ccc",
    padx="20",
    pady="10",
    font=("Verdana", 20, "bold italic"),
    command=button_func
)

goodbuy_button = Button(
    text="CoodBuy",
    padx="30",
    pady="20"
)

Ok_button = Button(
    text="Ok",
    padx="30",
    pady="20"
)

cancel_button = Button(
    text="Cancel",
    padx="30",
    pady="20"
)


hello_button.grid(row=1, column=0)
goodbuy_button.grid(row=2, column=1)
Ok_button.grid(row=1, column=1)
cancel_button.grid(row=2, column=2)





# Включение постоянной отрисовки окна, всегда в конце программы
root.mainloop()

