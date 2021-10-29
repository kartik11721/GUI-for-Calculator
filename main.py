from tkinter import *

root = Tk()
root.geometry('170x260')
root.title('calculator')

e = Entry(root, borderwidth=6, width=26)
e.grid(row=0, column=0, ipady=5, columnspan=4)
expression = ''


def click(x):
    global expression
    e.delete(0, "end")
    expression = expression + str(x)
    e.get()
    e.insert(0, expression)


def equal():
    try:
        global expression
        e.delete(0, "end")
        solved = str(eval(expression))
        expression = solved
        e.insert(0, solved)
    except:
        e.insert(0, 'Error')


def cls():
    global expression
    expression = ''
    e.delete(0, "end")


def back():
    global expression
    try:
        expression = expression.rstrip(expression[-1])
    except:
        pass
    e.delete(0, "end")
    e.insert(0, expression)


button_1byx = Button(root, text='²√x', height=2, width=4,
                     bd=3, command=lambda: click('**(1/2)'))
button_x2 = Button(root, text='x²', height=2, width=4,
                   bd=3, command=lambda: click('**2'))
button_clear = Button(root, text='CE', height=2, width=4, bd=3, command=cls)
button_back = Button(root, text='<<', height=2, width=4, bd=3, command=back)

button_7 = Button(root, text='7', height=2, width=4,
                  bd=3, command=lambda: click(7))
button_8 = Button(root, text='8', height=2, width=4,
                  bd=3, command=lambda: click(8))
button_9 = Button(root, text='9', height=2, width=4,
                  bd=3, command=lambda: click(9))
button_divide = Button(root, text='/', height=2, width=4,
                       bd=3, command=lambda: click('/'))

button_4 = Button(root, text='4', height=2, width=4,
                  bd=3, command=lambda: click(4))
button_5 = Button(root, text='5', height=2, width=4,
                  bd=3, command=lambda: click(5))
button_6 = Button(root, text='6', height=2, width=4,
                  bd=3, command=lambda: click(6))
button_multiply = Button(root, text='*', height=2,
                         width=4, bd=3, command=lambda: click('*'))

button_1 = Button(root, text='1', height=2, width=4,
                  bd=3, command=lambda: click(1))
button_2 = Button(root, text='2', height=2, width=4,
                  bd=3, command=lambda: click(2))
button_3 = Button(root, text='3', height=2, width=4,
                  bd=3, command=lambda: click(3))
button_subtract = Button(root, text='-', height=2,
                         width=4, bd=3, command=lambda: click('-'))

button_0 = Button(root, text='0', height=2, width=4,
                  bd=3, command=lambda: click(0))
button_period = Button(root, text='.', height=2, width=4,
                       bd=3, command=lambda: click('.'))
button_equal = Button(root, text='=', height=2, width=4,
                      bd=3, command=lambda: equal())
button_add = Button(root, text='+', height=2, width=4,
                    bd=3, command=lambda: click('+'))

button_1byx.grid(row=1, column=0)
button_x2.grid(row=1, column=1)
button_clear.grid(row=1, column=2)
button_back.grid(row=1, column=3)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)
button_0.grid(row=5, column=0)
button_period.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_add.grid(row=5, column=3)

root.mainloop()
