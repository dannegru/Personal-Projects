from tkinter import *

root = Tk()
root.title('Calculator')
root.resizable(False, False)
root.config(background='#202020')
root.option_add("*font", "lucida 20 bold")


input = Entry(root, width=25, bd=0, bg='#202020',
              fg='#fff', insertbackground='#fff')
input.grid(row=0, column=0, columnspan=4, ipady=25)


# Calculus Vars
result = None
sign = None
sign_index = 0
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


# Functions
def get_current():
    global current
    try:
        if '.' in input.get():
            current = float(input.get())
        else:
            current = int(input.get())
    except ValueError:
        current = None


def operate(sign):
    global result, sign_index
    get_current()
    if current is not None:
        sign_index = 1
        if result is None:
            result = current
        else:
            result = operators[sign](result, current)


def btn_add():
    global sign
    if sign:
        operate(sign)
        sign = '+'
    else:
        sign = '+'
        operate(sign)


def btn_subtract():
    global sign
    if sign:
        operate(sign)
        sign = '-'
    else:
        sign = '-'
        operate(sign)


def btn_multiply():
    global sign
    if sign:
        operate(sign)
        sign = '*'
    else:
        sign = '*'
        operate(sign)


def btn_divide():
    global sign
    if sign:
        operate(sign)
        sign = '/'
    else:
        sign = '/'
        operate(sign)


def btn_equal():
    global result, sign
    if result:
        operate(sign)
        input.delete(0, END)
        input.insert(0, result)
        result = None


def num_clicked(num):
    global sign_index
    if sign_index:
        sign_index = 0
        input.delete(0, END)
    current = input.get()
    if len(current) > 0:
        if current[0] == '0' and '.' not in current:
            current = ''
    current += str(num)
    input.delete(0, END)
    input.insert(-1, current)


def btn_clear():
    global result
    result = None
    input.delete(0, END)


def change_sign():
    number = input.get()
    if number:
        if number[0] == '0' and len(number) == 1:
            pass
        elif number[0].isdigit():
            input.insert(0, '-')
        else:
            input.delete(0, 1)


def place_point():
    if '.' not in input.get():
        if len(input.get()) > 0:
            input.insert(END, '.')
        else:
            input.insert(END, '0.')


def delete_last():
    start_index = len(input.get()) - 1
    input.delete(start_index, END)


# Creating The Buttons Info List
btn_list = [
    # symbol, command, bg-color, row, col
    ['CE', btn_clear, '#181818', 1, 0],
    ['C', btn_clear, '#181818', 1, 1],
    ['⌫', delete_last, '#181818', 1, 2],
    ['/', btn_divide, '#181818', 1, 3],

    ['*', btn_multiply, '#181818', 2, 3],
    ['-', btn_subtract, '#181818', 3, 3],
    ['+', btn_add, '#181818', 4, 3],

    ['+/-', change_sign, '#000000', 5, 0],
    ['.', place_point, '#000000', 5, 2],
    ['=', btn_equal, '#006600', 5, 3],

    [0, lambda: num_clicked(0), '#000000', 5, 1],
]

column = 0
row = 4
for num in range(1, 10):
    btn_list.append(
        [num, lambda num=num: num_clicked(num), '#000000', row, column])
    column += 1
    if column == 3:
        column = 0
        row -= 1


# Creating And Displaying The Actual Buttons
buttons = dict()
for button in btn_list:
    symbol = button[0]
    command = button[1]
    color = button[2]
    row = button[3]
    col = button[4]

    buttons[symbol] = Button(root, padx=30, pady=20, bd=0, fg='#fff',
                             bg=color, text=symbol, command=command)
    buttons[symbol].grid(row=row, column=col, sticky="ew")


# MainLoop
root.mainloop()
