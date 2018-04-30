import random
import tkinter
def new_color():
    cmap = "#%02X%02X%02X" % (random.randint(0, 255),
                              random.randint(0, 255),
                              random.randint(0, 255))
    but["bg"] = cmap
root = tkinter.Tk()
but = tkinter.Button(root, width=20, text="Push", command=new_color)

but.pack()
root.mainloop()