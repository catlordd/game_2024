from tkinter import *
 
root = Tk()     # создаем корневой объект - окно
root.title("2024")     # устанавливаем заголовок окна
root.geometry("500x600")    # устанавливаем размеры окна
root.resizable(False, False) 
label = Label(text="Hello, it is 2024!") # создаем текстовую метку
label.pack()    # размещаем метку в окне
 
root.mainloop()