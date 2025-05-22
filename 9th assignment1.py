from tkinter import *
window = Tk()

photo1 = PhotoImage(file="C:\\Users\\user\\Desktop\\9th\\dog.gif")
label1 = Label(window, image= photo1)
label1.pack(side=LEFT)

photo2 = PhotoImage(file="C:\\Users\\user\\Desktop\\9th\\cat.gif")
label2 = Label(window, image= photo2)
label2.pack(side=LEFT)

label1.pack()
window.mainloop()