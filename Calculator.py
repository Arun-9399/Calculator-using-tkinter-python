from tkinter import *

import parser

root = Tk()
root.title("Calculator")

# get the user input and place it to text field

i = 0


def usr(num):
    global i
    display.insert(i, num)
    i += 1


# adding operators
def get_operators(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


# making clear all the input field(deleting the input field number)
def clear_all():
    display.delete(0, END)


# Deleting digit by digit
def SingleDelete():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")


# performing the logic for operators
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# adding the input field
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)

# Adding Button to the calculator
Button(root, text="1", command=lambda: usr(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: usr(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: usr(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: usr(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: usr(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: usr(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: usr(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: usr(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: usr(9)).grid(row=4, column=2)

# adding other button to calculator
Button(root, text="C", command=lambda: clear_all()).grid(row=5, column=0)
Button(root, text="0", command=lambda: usr(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

Button(root, text="+", command=lambda: get_operators("+")).grid(row=2, column=3)
Button(root, text="- ", command=lambda: get_operators("-")).grid(row=3, column=3)
Button(root, text="* ", command=lambda: get_operators("*")).grid(row=4, column=3)
Button(root, text="/ ", command=lambda: get_operators("/")).grid(row=5, column=3)

# Adding new operations
Button(root, text="pi", command=lambda: get_operators("3.14")).grid(row=2, column=4)
Button(root, text="%", command=lambda: get_operators("%")).grid(row=3, column=4)
Button(root, text="(", command=lambda: get_operators("(")).grid(row=4, column=4)
Button(root, text="exp", command=lambda: get_operators("**")).grid(row=5, column=4)

Button(root, text="<-", command=lambda: SingleDelete()).grid(row=2, column=5)
Button(root, text="x!").grid(row=3, column=5)
Button(root, text=")", command=lambda: get_operators(")")).grid(row=4, column=5)
Button(root, text="^2", command=lambda: get_operators("**2")).grid(row=5, column=5)

root.mainloop()
