from tkinter import *
from tkinter import ttk

# Функция для создания поля
def create_field(i=4):
    y = 0
    field = []
    while y < i:
        field.append([])
        x = 0
        while x < i:
            field[y].append(1)
            x += 1
        y += 1
    return field

field = create_field()
print(field)

root = Tk()     # создаем корневой объект - окно
root.title("2024")     # устанавливаем заголовок окна
root.geometry("500x600")    # устанавливаем размеры окна
root.resizable(False, False) # нельзя менять размеры окна  
icon = PhotoImage(file = "data/icon.png") # иконка игры
root.iconphoto(False, icon)


label = Label(text="Hello, it is 2024!") # создаем текстовую метку

def form_field(field=field):
    field_text = ""
    for x in field:
        field_text = field_text + '\n' + str(x)
    return field_text
    
field_text = StringVar(value=form_field())
label_field = Label(textvariable=field_text)


def click_button_right(_field = field):
    count_y = len(_field)
    count_x = len(_field[0])
    
    _y = 0
    _x = count_x - 1
    while _y < count_y:
        if _field[_y][_x] == _field[_y][_x-1]:
            _field[_y][_x] = _field[_y][_x] * 2
            for ix in range(_x-1,0,-1):
                if ix != 0:
                    _field[_y][ix] = _field[_y][ix-1]
                else:
                    _field[_y][ix] = 0
            _x = _x - 2
        else:
            _x = _x - 1 
    
    '''for y in range(count_y):
        stop_see = False
        for x in range(count_x-1,0,-1):
            if x != 0 and _field[y][x] ==_field[y][x-1] and stop_see == False:
                _field[y][x] = _field[y][x]*2
                stop_see = True
                for i in range(x-1,0,-1):
                    if i!=0:
                       _field[y][i] = _field[y][i-1] 
                    else:
                        _field[y][i] = 0
            else: 
                stop_see = False'''

    '''for i,x in enumerate(_field):
        print(x)
        x.reverse()
        
        for ii, num in enumerate(x):
            if ii < 3 and num == x[ii+1]:
                x[ii] = x[ii]*2
        x.reverse()
        _field[i] = x'''
    field_text.set(form_field(_field))
    print(_field)

    
btn = ttk.Button(text="Click Me", command=click_button_right)


btn.pack()
label.pack()    # размещаем метку в окне
label_field.pack()

 
root.mainloop()