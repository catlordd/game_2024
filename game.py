from tkinter import *
from tkinter import ttk
import random


field = []
print(field)

# Функция для создания поля
def create_field(i=4, field=field):
    y = 0
    field.clear()
    while y < i:
        field.append([])
        x = 0
        while x < i:
            field[y].append(random.choice([0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,4]))
            x += 1
        y += 1
    field_text.set(form_field())
    print("START\n" + str(field))

#field = create_field()

root = Tk()     # создаем корневой объект - окно
root.title("2024")     # устанавливаем заголовок окна
#root.geometry("500x600")    # устанавливаем размеры окна
root.resizable(False, False) # нельзя менять размеры окна  
icon = PhotoImage(file = "data/icon.png") # иконка игры
root.iconphoto(False, icon)

'''#
y = 0
str_matrix = []
while y < 4:
    str_matrix.append([])
    x = 0
    while x < 4:
        str_matrix[y].append(StringVar(value=field[y][x]))
        x = x + 1
    y = y + 1
#
frame_matrixx = Frame( relief=RIDGE)
y = 0
label_matrix = []
while y < 4:
    label_matrix.append([])
    x = 0
    while x < 4:
        label_matrix[y].append(Label(frame_matrixx, width=5, relief=RIDGE,textvariable = str_matrix[y][x]))
        label_matrix[y][x].pack(anchor=W)
        x = x + 1
    y = y + 1

frame_matrixx.pack(anchor=W)'''

# Функция для отрисовки матрицы
def form_field(field=field):
    field_text = ""
    for y in field:
        y_string = ""
        for x in y:
            y_string = y_string + " "*(4-len(str(x))) + str(x) +"  "

        if field_text=="":
            field_text = str(y_string)
        else:
            field_text= field_text + '\n' + str(y_string)
            
    return field_text

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
                check_new_number = True
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
                check_new_number = True
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
                check_new_number = True
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
                check_new_number = True
            else:
                _y =_y-1
        _x = _x + 1
        _y = -1
    
    # Меняем случайный 0 на 2 или 4
    if check_new_number: new_number(_field)
    
    # Вносим изменения в поле в интерфейсе
    field_text.set(form_field(_field))
    print(_field)        

# Контейнеры для матрицы и кнопок
frame_start = ttk.Frame()
frame_matrix = ttk.Frame()
frame_buttom = ttk.Frame(padding=[2, 2])

# Создаем текстовую метку, приветствие
label = Label(text="Hello, it is 2024!") 
label.pack()    # размещаем метку в окне


# Создаем переменную, которая конвертируют матрицу(list) в StringVar
field_text = StringVar(value=form_field())

# Список с выбором сложности игры
diff = {'easy':6, 'normal':5, 'hard':4}
select_diff = StringVar(value=list(diff.keys())[0])
combobox = ttk.Combobox(frame_start, textvariable=select_diff, values=list(diff.keys()), state="readonly")

def create_fieldd():
    create_field(i = select_diff.get())
#
btnstart = ttk.Button(frame_start, text="New game", command=create_fieldd)
# Рисуем контейнер для старта
frame_start.pack()
combobox.pack(side='left')
btnstart.pack(side='right')


# Создаем слой с матрицой
label_field = Label(frame_matrix, relief=RIDGE, textvariable=field_text)
# Рисуем контейнер для матрицы
frame_matrix.pack()
# Рисуем матрицу в контейнере
label_field.pack()

# Создаем кнопки для перемещения цифр
btnr = ttk.Button(frame_buttom, text="RIGHT", command=click_button_right)
btnl = ttk.Button(frame_buttom, text="LEFT", command=click_button_left)
btnu = ttk.Button(frame_buttom, text="UP", command=click_button_up)
btnd = ttk.Button(frame_buttom, text="DOWN", command=click_button_down)

# Рисуем контейнер для кнопок на окне
frame_buttom.pack(padx=5, pady=5)
# Рисуем кнопки в контейнере
btnr.pack(side='right')
btnl.pack(side='left')
btnu.pack(side='top')
btnd.pack(side='bottom')

# Запуск окна 
root.mainloop()