from tkinter import *
from tkinter import ttk
import random

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

#field = create_field()
field = [[2,0,0,0],
         [0,0,2,0],
         [0,2,0,0],
         [0,0,0,2]]
print(field)

root = Tk()     # создаем корневой объект - окно
root.title("2024")     # устанавливаем заголовок окна
root.geometry("500x600")    # устанавливаем размеры окна
root.resizable(False, False) # нельзя менять размеры окна  
icon = PhotoImage(file = "data/icon.png") # иконка игры
root.iconphoto(False, icon)
frame_matrix = ttk.Frame(padding=[2, 2])
frame_buttom = ttk.Frame(padding=[2, 2])

label = Label(text="Hello, it is 2024!") # создаем текстовую метку

# Функция для отрисовки матрицы
def form_field(field=field):
    field_text = ""
    for x in field:
        field_text = field_text + '\n' + str(x)
    return field_text
    
field_text = StringVar(value=form_field())
label_field = Label(textvariable=field_text)

# Функция для случайного изменения в матрице нулей на 2 или 4
def new_number(field=field):
    zero_list = []
    for iy, y in enumerate(field):
        for ix, x in enumerate(y):
            if x == 0: zero_list.append((iy,ix))
    random_zero = random.choice(zero_list)
    
    print(f'Слчайное число: {random_zero[1]}')
    field[random_zero[0]][random_zero[1]] = random.choice([2,2,2,2,2,2,2,2,2,4,4,4,8])
    return field


# Функция для суммирования и смещения цифр вправо
def click_button_right(_field = field):
    count_y = len(_field)
    count_x = len(_field[0])
    check_new_number = False
    
    # Цикл чтобы суммировать одинаковые соседние цифры
    _y = 0
    _x = -1
    while _y < count_y:
        while _x > count_x*-1:
            if _x != 0 and _field[_y][_x] == _field[_y][_x-1]:
                _field[_y][_x] = _field[_y][_x] * 2
                _field[_y][_x-1] = 0
                _x = _x - 2
                check_new_number = True
            else:
                _x = _x - 1
        _y = _y + 1
        _x = -1 
    
    # Цикл чтобы сместить все отличные от нуля цифры вправо
    _y = 0
    _x = -1
    while _y < count_y:
        while _x > (count_x*-1)-1:
            if _x != -1 and _field[_y][_x+1] == 0 and _field[_y][_x] != 0:
                _field[_y][_x+1] = _field[_y][_x]
                _field[_y][_x] = 0
                _x =_x+1
            else:
                _x = _x-1
        _y = _y + 1
        _x = -1
    
    # Меняем случайный 0 на 2 или 4
    if check_new_number: _field=new_number(_field)
        
    # Вносим изменения в поле в интерфейсе
    field_text.set(form_field(_field))
    print(_field)

# Функция для суммирования и смещения цифр влево
def click_button_left(_field = field):
    count_y = len(_field)
    count_x = len(_field[0])
    check_new_number = False
    
    # Цикл чтобы суммировать одинаковые соседние цифры
    _y = 0
    _x = 0
    while _y < count_y:
        while _x < count_x:
            if _x != count_x-1 and _field[_y][_x] == _field[_y][_x+1]:
                _field[_y][_x] = _field[_y][_x] * 2
                _field[_y][_x+1] = 0
                _x = _x + 2
                check_new_number = True
            else:
                _x = _x + 1
        _y = _y + 1
        _x = 0 
    
    # Цикл чтобы сместить все отличные от нуля цифры влево
    _y = 0
    _x = 0
    while _y < count_y:
        while _x < count_x:
            if _x != 0 and _field[_y][_x-1] == 0 and _field[_y][_x] != 0:
                _field[_y][_x-1] = _field[_y][_x]
                _field[_y][_x] = 0
                _x =_x-1
            else:
                _x = _x+1
        _y = _y + 1
        _x = 0
    
    # Меняем случайный 0 на 2 или 4
    if check_new_number: new_number(_field)
    
    # Вносим изменения в поле в интерфейсе
    field_text.set(form_field(_field))
    print(_field)

# Функция для суммирования и смещения цифр вверх
def click_button_up(_field = field):
    count_y = len(_field)
    count_x = len(_field[0])
    check_new_number = False
    
    # Цикл чтобы суммировать одинаковые соседние цифры
    _y = 0
    _x = 0
    while _x < count_x:
        while _y < count_y:
            if _y != count_y-1 and _field[_y][_x] == _field[_y+1][_x]:
                _field[_y][_x] = _field[_y][_x] * 2
                _field[_y+1][_x] = 0
                _y = _y + 2
                check_new_number = True
            else:
                _y = _y + 1
        _x = _x + 1
        _y = 0 
    
    # Цикл чтобы сместить все отличные от нуля цифры вверх
    _y = 0
    _x = 0
    while _x < count_x:
        while _y < count_y:
            if _y != 0 and _field[_y-1][_x] == 0 and _field[_y][_x] != 0:
                _field[_y-1][_x] = _field[_y][_x]
                _field[_y][_x] = 0
                _y =_y-1
            else:
                _y = _y+1
        _x = _x + 1
        _y = 0
    
    # Меняем случайный 0 на 2 или 4
    if check_new_number: new_number(_field)
    
    # Вносим изменения в поле в интерфейсе
    field_text.set(form_field(_field))
    print(_field)

# Функция для суммирования и смещения цифр вниз
def click_button_down(_field = field):
    count_y = len(_field)
    count_x = len(_field[0])
    check_new_number = False
    
    # Цикл чтобы суммировать одинаковые соседние цифры
    _y = -1
    _x = 0
    while _x < count_x:
        while _y > count_y*-1:
            if _y != count_y*-1 and _field[_y][_x] == _field[_y-1][_x]:
                _field[_y][_x] = _field[_y][_x] * 2
                _field[_y-1][_x] = 0
                _y = _y - 2
                check_new_number = True
            else:
                _y = _y - 1
        _x = _x + 1
        _y = 0 
    
    # Цикл чтобы сместить все отличные от нуля цифры вниз
    _y = -1
    _x = 0
    while _x < count_x:
        while _y > (count_y*-1)-1:
            if _y != -1 and _field[_y+1][_x] == 0 and _field[_y][_x] != 0:
                _field[_y+1][_x] = _field[_y][_x]
                _field[_y][_x] = 0
                _y =_y+1
            else:
                _y =_y-1
        _x = _x + 1
        _y = -1
    
    # Меняем случайный 0 на 2 или 4
    if check_new_number: new_number(_field)
    
    # Вносим изменения в поле в интерфейсе
    field_text.set(form_field(_field))
    print(_field)        

# Создаем кнопки для перемещения цифр
btnr = ttk.Button(text="RIGHT", command=click_button_right)
btnl = ttk.Button(text="LEFT", command=click_button_left)
btnu = ttk.Button(text="UP", command=click_button_up)
btnd = ttk.Button(text="DOWN", command=click_button_down)

# Рисуем кнопки на окне
btnr.pack(side='right')
btnl.pack(side='left')
btnu.pack(side='top')
btnd.pack(side='bottom')

label.pack()    # размещаем метку в окне
label_field.pack( expand=True)

 
root.mainloop()