from tkinter import *
root = Tk()
root.geometry('400x180')
root.title('Calculator')

def execute():
    try:
        number1 = float(n1.get())
        number2 = float(n2.get())
        operation = op.get()
    
        if operation == '+':
            answer = f"{number1} + {number2} = {number1 + number2}"
        elif operation == '-':
            answer = f"{number1} - {number2} = {number1 - number2}"
        elif operation == '*':
            answer = f"{number1} * {number2} = {number1 * number2}"
        elif operation == '/':
            answer = f"{number1} / {number2} = {number1 / number2}"
        else:
            Label(root, text = 'Invalid Operation', fg = 'red').grid(row = 4, column = 1)
        Label(root, text = answer).grid(row = 4, column = 1)
    except:
        Label(root, text = 'Invalid Input', fg = 'red').grid(row = 4, column = 1)

Label(root, text = "Enter first number").grid(row = 0, column = 0, pady =5)
n1 = Entry(root, width= 30)
n1.grid(row = 0, column = 1)
Label(root, text = "Enter second number").grid(row = 1, column = 0, pady =5)
n2 = Entry(root, width= 30)
n2.grid(row = 1, column = 1)
Label(root, text = "Enter The Operation (+,-,*,/): ").grid(row = 2, column = 0, pady =5)
op = Entry(root, width= 30)
op.grid(row = 2, column = 1)

Button(root, text = 'Confirm',command = execute).grid(row = 3, column = 1, padx =10, pady =10)

root.mainloop()
